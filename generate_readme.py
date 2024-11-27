import os
import json


class MarkdownGenerator:

    def __init__(self, data_file):
        self._readme_filename = "README.md"
        self._readme_template_filename = "README.template"
        with open(data_file, "r") as f:
            data = json.load(f)
            self._year = int(data["year"])
            self._repository_url = data["repository_url"]
            self._challenge_titles = {}
            for day, challenge_title in data["challenge_titles"].items():
                self._challenge_titles[int(day)] = challenge_title


    def get_repository_url(self) -> str:
        return self._repository_url()

    def get_year(self) -> int:
        return self._year

    def get_challenge_titles(self) -> dict[str:str]:
        return self._challenge_titles

    def get_challenge_slug(self, day: int) -> str:
        challenge_title = self.get_challenge_titles()[day]
        slug = challenge_title.lower().replace(" ", "_")
        slug = "".join(c for c in slug if c.isalnum() or c == "_")
        return slug

    def get_solution_filename(self, day: int) -> str:
        challenge_slug = self.get_challenge_slug(day)
        day_zerofill = str(day).zfill(2)
        return f"{day_zerofill}_{challenge_slug}.py"

    def get_markdown_filename(self, day: int) -> str:
        challenge_slug = self.get_challenge_slug(day)
        day_zerofill = str(day).zfill(2)
        return f"{day_zerofill}_{challenge_slug}.ipynb"

    def get_aoc_challenge_link(self, day: int) -> str:
        return f"https://adventofcode.com/{self._year}/day/{day}"

    def get_aoc_solution_github_link(self, day: int) -> str:
        filename = self.get_solution_filename(day)
        return f"{self.get_repository_url()}/blob/main/solutions/{filename}"

    def get_aoc_dialogue_github_link(self, day: int) -> str:
        filename = self.get_markdown_filename(day)
        return f"{self.get_repository_url()}/blob/main/dialogues/{filename}"

    def get_path_to_local_solution_filename(self, day: int) -> str:
        challenge_slug = self.get_challenge_slug(day)
        day_zerofill = str(day).zfill(2)
        return f"solutions/{day_zerofill}_{challenge_slug}.py"

    def get_end_of_line_starting_with(self, filename: str, startswith: str, default: str) -> str:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                while line.startswith("#"):  # remove leading comment indicators
                    line = line[1:].strip()
                if line.lower().startswith(startswith.lower()):
                    return line[len(startswith):].strip()
        return default

    def get_space_complexity(self, day: int) -> str:
        filename = self.get_path_to_local_solution_filename(day)
        return self.get_end_of_line_starting_with(filename, "Space complexity: ", "O(...)")

    def get_time_complexity(self, day: int) -> str:
        filename = self.get_path_to_local_solution_filename(day)
        return self.get_end_of_line_starting_with(filename, "Time complexity: ", "O(...)")

    def has_been_solved(self, day: int) -> bool:
        def contains_python_code(filename: str) -> bool:
            """
            Check if a file contains non-empty lines that are not comments
            :param filename:
            :return:
            """
            with open(filename, "r") as f:
                in_comment = False
                for line in f:
                    line = line.strip()
                    # ignore empty lines
                    if not line:
                        continue

                    # ignore single line comments
                    if line.startswith('#'):
                        continue

                    # ignore multi-line comments
                    if line.startswith('"""'):
                        in_comment = not in_comment
                        continue
                    if line.endswith('"""'):
                        in_comment = not in_comment
                        continue
                    if in_comment:
                        continue

                    # We found a non-empty line that is not a comment
                    print("FOUND CODE LINE", line)
                    return True

        solution_filename = self.get_path_to_local_solution_filename(day)
        if os.path.exists(solution_filename):
            return contains_python_code(solution_filename)
        return False

    def generate_markdown_table(self) -> str:
        def generate_table_header() -> str:
            return "Day | Challenge	| Solution Code | Solution Dialog | Time Complexity | Space Complexity | Challenge Link"

        def generate_row(day: int) -> str:
            day_zerofill = str(day).zfill(2)
            challenge_title = self.get_challenge_titles()[day]
            challenge_link = self.get_aoc_challenge_link(day)
            if self.has_been_solved(day):
                solution_link = f"[link]({self.get_aoc_solution_github_link(day)})"
                dialogue_link = f"[link]({self.get_aoc_dialogue_github_link(day)})"
                time_complexity = self.get_time_complexity(day)
                space_complexity = self.get_space_complexity(day)
            else:
                solution_link = "Unsolved"
                dialogue_link = "-"
                time_complexity = "-"
                space_complexity = "-"
            return f"{day} | {challenge_title} | {solution_link} | {dialogue_link} | {time_complexity} | {space_complexity} | [adventofcode.com]({challenge_link})"

        def format_markdown_table(table: list[str]) -> list[str]:
            # Find the maximum width of each column
            max_column_width = []
            for row in table:
                cols = row.split("|")
                for i, col in enumerate(cols):
                    col = col.strip()  # here we remove leading and training whitespaces from the cell
                    if len(max_column_width) <= i:
                        max_column_width.append(0)
                    max_column_width[i] = int(max(max_column_width[i], len(col)))
            formatted_table = []

            # Format the table
            for row_nr, row in enumerate(table):
                cols = row.split("|")
                for i, col in enumerate(cols):
                    cols[i] = ' ' + col.strip().ljust(
                        max_column_width[i]) + ' '  # here we add a leading and a trailing whitespace to the cell
                formatted_table.append('| ' + "|".join(cols).strip() + " |")
                if row_nr == 0:
                    # add separator row after the header
                    separator_row = "|".join(['-' * (max_column_width[i] + 2) for i in range(len(cols))])
                    formatted_table.append('|' + separator_row + "|")

            return formatted_table

        markdown_table = [generate_table_header()]
        for day in range(1, 25 + 1):
            markdown_table.append(generate_row(day))
        markdown_table = format_markdown_table(markdown_table)

        markdown = "\n".join(markdown_table)
        return markdown

    def generate_readme(self) -> None:

        if not os.path.exists(self._readme_template_filename):
            raise FileNotFoundError(f"File {self._readme_template_filename} not found.")

        table = self.generate_markdown_table()

        generated_readme = []
        inserted_table_flag = False
        with open(self._readme_template_filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() == "<!-- INSERT CHALLENGE TABLE HERE -->":
                    generated_readme.append(table)
                    inserted_table_flag = True
                else:
                    generated_readme.append(line.rstrip())
        if not inserted_table_flag:
            raise ValueError("Could not find the placeholder for the challenge table in the README template.")

        with open(self._readme_filename, "w") as f:
            f.write("\n".join(generated_readme))


if __name__ == '__main__':
    generator = MarkdownGenerator("challenges.json")
    generator.generate_readme()

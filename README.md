# About

In December 2024, I joined [Jeremy Howard's](https://jeremy.fast.ai) new course, [Solve It With Code](https://solveit.fast.ai), by [fast.ai](https://www.fast.ai). This unique program introduces a fresh approach to coding that combines iterative problem-solving with AI. It emphasizes building foundational skills without requiring a background in data structures or computer science. The course focuses on using Python (with minimal external libraries) and teaches an engineering technique that integrates AI as a collaborative tool ([source](https://solveit.fast.ai/course-details)).

This repository contains my solutions to the Advent of Code 2023 challenges, crafted using the engineering process taught in the course.
Beyond the solutions, you can see how each solution was developed in dialog with the AI. The solutions are organized in the [solutions](./solutions) folder, the dialogues in the [dialogues](./dialogues) folder, and the input data for each challenge is stored in the [data](./data) folder.

__Note:__ The input data for each challenge differs by user. If you are using this project as a template for your own solutions, you will need to log in to the [Advent of Code](https://adventofcode.com) website to download your personal puzzle input data and use it to replace the existing files in the [./data/](./data/) folder. To update the [table of challenges](#table-of-challenges), read these [instructions](#generating-this-readme) below.

## Table of Challenges

| Day | Challenge                       | Solution Code | Solution Dialog | Time Complexity | Space Complexity | Challenge Link |
|-----|---------------------------------|---------------|-----------------|-----------------|------------------|----------------------------------------------------------|
| 1   | Trebuchet?!                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/1) |
| 2   | Cube Conundrum                  | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/2) |
| 3   | Gear Ratios                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/3) |
| 4   | Scratchcards                    | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/4) |
| 5   | If You Give A Seed A Fertilizer | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/5) |
| 6   | Wait For It                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/6) |
| 7   | Camel Cards                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/7) |
| 8   | Haunted Wasteland               | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/8) |
| 9   | Mirage Maintenance              | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/9) |
| 10  | Pipe Maze                       | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/10) |
| 11  | Cosmic Expansion                | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/11) |
| 12  | Hot Springs                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/12) |
| 13  | Point of Incidence              | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/13) |
| 14  | Parabolic Reflector Dish        | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/14) |
| 15  | Lens Library                    | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/15) |
| 16  | The Floor Will Be Lava          | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/16) |
| 17  | Clumsy Crucible                 | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/17) |
| 18  | Lavaduct Lagoon                 | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/18) |
| 19  | Aplenty                         | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/19) |
| 20  | Pulse Propagation               | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/20) |
| 21  | Step Counter                    | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/21) |
| 22  | Sand Slabs                      | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/22) |
| 23  | A Long Walk                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/23) |
| 24  | Never Tell Me The Odds          | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/24) |
| 25  | Snowverload                     | Unsolved      | -               | -               | -                | [adventofcode.com](https://adventofcode.com/2023/day/25) |

## Repository Structure

```bash
.
├── Dockerfile.readme               <- Defines the Docker environment for generating this README.md file
├── Dockerfile.data                 <- Defines the Docker environment for downloading the advent of code data
├── README.md                       <- You are reading this right now
├── README.template                 <- Template for dynamically generating the README file
├── challenges.json                 <- Metadata about Advent of Code 2023 challenges
├── download_data.py                <- Script to download the Advent of Code data
├── download_data_using_docker.sh   <- Runs download_data.py inside a Docker container
├── generate_readme.py              <- Script to generate the README dynamically
├── generate_readme_using_docker.sh <- Runs generate_readme.py inside a Docker container
├── requirements.txt                <- Lists the Python dependencies for the project
├── data                            <- Contains input and sample data for challenges
│   ├── dayXX_input.txt             <- Main input data for each challenge, downloaded using the downloader
│   ├── dayXX_sample.txt            <- Sample input manually extracted from the challenge description for testing
│   └── dayXX_test.txt              <- Additional test data you may want to add yourself
├── dialogues                       <- Contains the solution dialog as Juptyer notebooks
│   ├── XX_*.ipynb                  <- Juptyer notebooks for each challenge day XX=01,...,25
└── solutions                       <- Contains Python solution scripts for each challenge
    └── XX_*.py                     <- Python scripts containing the solutions for each challenge day XX=01,...,25
```

---
# Setup

To set up the project on your local machine, follow these steps:

- Clone this repository.
- Ensure that Docker is installed and running on your system.

## How to Run the Advent of Code Data Downloader

Advent of code has different input data for each user. This means you need to download your personal input data to solve the challenges.
The following describes how you can download the data for all 26 days almost automatically. You need to do this only once.

### Preparation

- Create a `.env` file in the project root and add the following line to it:

```plaintext
AOC_SESSION=<insert_your_session_key_here>
```

This file holds your session key, which is required to download the data.
The next section describes how you can get the session key to insert into the `.env` file.

### How to Obtain Your Session Key

1. Log in to the [Advent of Code website](https://adventofcode.com).
2. Open your browser's developer tools (right-click anywhere on the page and select "Inspect" or press `F12`).
3. Navigate to the "Application" tab (in Chrome) or "Storage" tab (in Firefox).
4. Locate the "Cookies" section and click on `adventofcode.com`.
5. Find the cookie named `session` and copy its value.
6. Paste this value into your `.env` file as the `AOC_SESSION` variable.

### Running the Data Downloader

#### 1. Make the Bash Script Executable

Run the following command to make the script executable:

```bash
chmod +x ./download_data_using_docker.sh
```

#### 2. Build and Run the Docker Container

Run the following command:

```bash
./download_data_using_docker.sh
```

- This will build the Docker image and run the `download_data.py` script inside the container.
- The script will download the Advent of Code data for the specified day and year.

#### 3. Verify the Output

Once the container execution is finished, the downloaded data files `day*_input.txt` will be available in `./data/` folder.


---
## Generating this README

Generating the `README.md` file updates the cells of the challenges table based on the metadata from the `challenges.json` file the content (!) of the solution files automatically.

__Note:__ The time and space complexity are extracted from the solution files by looking for lines that start with `Time complexity:` and `Space complexity:` respectively. Please ensure that these lines are present in your solution files as well. Here are some valid examples:
```python
"""
...
Time complexity: O(...)
Space complexity: O(...)
...
"""
```
or
```python
...
# Time complexity: O(...)
...
# Space complexity: O(...)
...
```

To generate the `README.md` file, follow these steps:

#### 1. Make the Bash Script Executable

Run the following command to make the script executable:

```bash
chmod +x ./generate_readme_using_docker.sh
```

#### 2. Build and Run the Docker Container

```bash
./generate_readme_using_docker.sh
```

- This will build the Docker image each time it is run to avoid file caching issues.
- It will then run the Docker container to execute the `generate_readme.py` script, which generates the `README.md` file and overwrites the exiting `README.md` file in your local directory.

#### 3. Verify the Output

Once the container execution is finished, you should see the updated `README.md` file in the same directory where you ran the script.
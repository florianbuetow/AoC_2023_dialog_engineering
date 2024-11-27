import os
import sys
from time import sleep

from dotenv import load_dotenv
from aocd import get_data

def download_aoc_inputs(year, output_dir):
    """
    Downloads Advent of Code inputs for all 25 days of the specified year
    and saves them to the specified output directory.

    Args:
        year (int): The year of the Advent of Code event.
        output_dir (str): The directory where input files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    for day in range(1, 26):
        try:
            if day != 1:
                sleep(2)  # To avoid rate limiting from the server
            data = get_data(day=day, year=year)
            file_path = os.path.join(output_dir, f"day{day:02d}_input.txt")
            with open(file_path, 'w') as f:
                f.write(data)
            print(f"Downloaded input for Day {day}")
        except Exception as e:
            print(f"Failed to download input for Day {day}: {e}")

if __name__ == "__main__":
    load_dotenv()
    session_token = os.getenv('AOC_SESSION')

    if not session_token:
        print("Error: AOC_SESSION token not found. Please create a .env file that contains \"AOC_SESSION=<your session token>\"")
        sys.exit(1)
    else:
        # Set the session token for aocd
        os.environ['AOC_SESSION'] = session_token
        year = 2023
        output_dir = "data"
        download_aoc_inputs(year, output_dir)

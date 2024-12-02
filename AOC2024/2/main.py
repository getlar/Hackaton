import argparse
import logging
import sys
import pandas as pd
from collections import Counter

logger = logging.getLogger(__name__)

def setup_logging():
    """
    Configures the logging settings for the application.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s',
        handlers=[
            logging.StreamHandler(sys.stderr)
        ]
    )
    stream_handler = [h for h in logging.root.handlers if isinstance(h, logging.StreamHandler)]
    if stream_handler:
        stream_handler[0].setLevel(logging.INFO)

def parse_args():
    """
    Parses command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(description="Advent of Code solution script.")
    parser.add_argument(
        "--input-path", type=str, help="Path to the input file containing puzzle data."
    )
    return parser.parse_args()

def read_input(file_path):
    """
    Reads the input file and returns the content.
    Supports line-by-line reading or pandas dataframe loading.
    """
    try:
        with open(file_path, 'r') as f:
            data = f.readlines()
        return [line.strip() for line in data]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)

def process_input(data):
    """
    Processes the input data for the problem.
    Can convert it into a pandas DataFrame or another suitable format.
    """
    df = pd.DataFrame([line.split(',') for line in data])
    return df

def is_ascending(sequence):
    return all(sequence[i] < sequence[i+1] and (1 <= abs(sequence[i] - sequence[i+1]) < 4) for i in range(len(sequence) - 1))

def is_descending(sequence):
    return all(sequence[i] > sequence[i+1] and (1 <= abs(sequence[i] - sequence[i+1]) < 4) for i in range(len(sequence) - 1))

def is_removing_valid(sequence):
    for i in range(len(sequence)):
        modified_sequence = sequence[:i] + sequence[i + 1:]
        if is_ascending(modified_sequence) or is_descending(modified_sequence):
            return True
    return False
    

def part_one(data):
    """
    Solution for Part 1 of the puzzle.
    """
    safe = 0
    sequences = [list(map(int, line.split())) for line in data]
    for sequence in sequences:
        if is_ascending(sequence) or is_descending(sequence):
            safe += 1
    return safe

def part_two(data):
    """
    Solution for Part 2 of the puzzle.
    """
    safe = 0
    sequences = [list(map(int, line.split())) for line in data]
    for sequence in sequences:
        if is_ascending(sequence) or is_descending(sequence):
            safe += 1
        elif is_removing_valid(sequence):
            safe += 1
    return safe

def main():
    setup_logging()
    args = parse_args()
    raw_data = read_input(args.input_path)

    result_one = part_one(raw_data)
    print(f"Part 1: {result_one}")

    result_two = part_two(raw_data)
    print(f"Part 2: {result_two}")

if __name__ == "__main__":
    main()

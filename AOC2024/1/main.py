import argparse
import logging
import sys
import pandas as pd
from collections import Counter

logger = logging.getLogger(__name__)

def setup_logging():
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
    parser = argparse.ArgumentParser(description="Advent of Code solution script.")
    parser.add_argument(
        "--input-path", type=str, help="Path to the input file containing puzzle data."
    )
    return parser.parse_args()

def read_input(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.readlines()
        return [line.strip() for line in data]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)

def part_one(data):
    left_ids, right_ids = zip(*[map(int, line.split()) for line in data])
    left_ids = sorted(left_ids, reverse=True)
    right_ids = sorted(right_ids, reverse=True)
    result = sum(abs(l - r) for l, r in zip(left_ids, right_ids))
    return result

def part_two(data):
    left_ids, right_ids = zip(*[map(int, line.split()) for line in data])
    right_id_counts = Counter(right_ids)
    result = {l: right_id_counts.get(l, 0) for l in left_ids}
    result = sum(key * value for key, value in result.items())
    return result

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

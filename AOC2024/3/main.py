import argparse
import logging
import sys
import re
from functools import reduce

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
    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = [re.findall(pattern, line) for line in data]
    matches_merged = sum(matches, [])
    multiplies = [list(map(int, match.strip("mul()").split(","))) for match in matches_merged]
    return sum([a * b for a, b in multiplies])

def part_two(data):
    
    class State:
        CALCULATE = "calculate"
        SKIP = "skip"

    def handle_state(acc, match):
        current_state, result = acc
        if match == "do()":
            return State.CALCULATE, result
        elif match == "don't()":
            return State.SKIP, result
        return current_state, result

    def handle_mul(acc, match):
        current_state, result = acc
        if current_state == State.CALCULATE:
            a, b = map(int, match.strip("mul()").split(","))
            return current_state, result + a * b
        return current_state, result

    def process_match(acc, match):
        if match in {"do()", "don't()"}:
            return handle_state(acc, match)
        return handle_mul(acc, match)

    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    matches = [re.findall(pattern, line) for line in data]
    matches_merged = sum(matches, [])

    _, result = reduce(process_match, matches_merged, (State.CALCULATE, 0))
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

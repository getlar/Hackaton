import argparse
import logging
import sys
import numpy as np
from typing import List

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

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Advent of Code solution script.")
    parser.add_argument(
        "--input-path", type=str, help="Path to the input file containing puzzle data."
    )
    return parser.parse_args()

def read_input(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as f:
            data = f.readlines()
        return [line.strip() for line in data]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)
        
def get_all_diagonals(data: np.ndarray) -> List[np.ndarray]:
    diagonals = [np.diagonal(data, offset) for offset in range(-data.shape[0] + 1, data.shape[1])]
    flipped_data = np.fliplr(data)
    diagonals += [np.diagonal(flipped_data, offset) for offset in range(-flipped_data.shape[0] + 1, flipped_data.shape[1])]
    return diagonals
    
def count_xmas(data: np.ndarray, search: str = "XMAS") -> int:
    count = 0
    for line in data:
        raw_line = "".join(line)
        count += raw_line.count(search)
        count += raw_line[::-1].count(search)
    return count

def count_x_mas_cross(data: np.ndarray) -> int:
    count = 0
    rows, cols = data.shape
    for r in range(rows):
        for c in range(cols):
            if (r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols and 
                (
                    (data[r - 1, c - 1] == 'M' and data[r, c] == 'A' and data[r + 1, c + 1] == 'S'
                     and (data[r - 1, c + 1] == 'M' and data[r + 1, c - 1] == 'S' or data[r - 1, c + 1] == 'S' and data[r + 1, c - 1] == 'M')) 
                    or
                    (data[r - 1, c - 1] == 'S' and data[r, c] == 'A' and data[r + 1, c + 1] == 'M'
                     and (data[r - 1, c + 1] == 'S' and data[r + 1, c - 1] == 'M' or data[r - 1, c + 1] == 'M' and data[r + 1, c - 1] == 'S'))
                )
            ):
                count += 1
    return count

def part_one(data: List[str]) -> int:
    list_data = [list(row) for row in data]
    np_data = np.char.array(list_data)
    c_h = count_xmas(np_data)
    c_v = count_xmas(np_data.T)
    c_d = count_xmas(get_all_diagonals(np_data))
    return c_h + c_v + c_d

def part_two(data: List[str]) -> int:
    list_data = [list(row) for row in data]
    np_data = np.char.array(list_data)
    return count_x_mas_cross(np_data)

    
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

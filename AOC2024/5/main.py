import argparse
import logging
import sys
import networkx as nx
from typing import List
from collections import defaultdict, deque
import matplotlib.pyplot as plt

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
        "--input-path", type=str, nargs='+', help="Path to the input file containing puzzle data."
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
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values):
        self.head = None
        self._create_list(values)

    def _create_list(self, values):
        if not values:
            return
        self.head = Node(values[0])
        current = self.head
        for value in values[1:]:
            current.next = Node(value)
            current = current.next
            
    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return " -> ".join(map(str, values))
    
def build_global_linked_list(data: List[str]) -> LinkedList:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for data_pair in data:
        x, y = map(int, data_pair.split("|"))
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0 

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return LinkedList(sorted_order)

def is_update_valid(update: List[int], global_linked_list: LinkedList) -> bool:
    current = global_linked_list.head
    update_index = 0

    while current and update_index < len(update):
        if current.value == update[update_index]:
            update_index += 1
        current = current.next

    return update_index == len(update)

def find_middle(update: List[int]) -> int:
    mid_idx = len(update) // 2
    return update[mid_idx]

def part_one(list_data: List[str], eval_date: List[str]) -> int:
    global_linked_list = build_global_linked_list(list_data)
    print(global_linked_list)
    c_t = 0
    for eval_sequence in eval_date:
        eval_sequence = list(map(int, eval_sequence.split(",")))
        if is_update_valid(eval_sequence, global_linked_list):
            c_t += find_middle(eval_sequence)
    return c_t

#############################################################################################

def parse_rules_to_hashmap(rules):
    ordering_map = {}
    for rule_pair in rules:
        x, y = map(int, rule_pair.split("|"))
        if x not in ordering_map:
            ordering_map[x] = set()
        ordering_map[x].add(y)
    return ordering_map

def is_update_valid_with_hashmap(update, ordering_map):
    seen = set()
    for page in update:
        if page in ordering_map:
            for must_follow in ordering_map[page]:
                if must_follow in seen:
                    return False
        seen.add(page)
    return True

def find_middle(update):
    mid_idx = len(update) // 2
    return update[mid_idx]

def simplify_graph(graph):
    cycles = list(nx.simple_cycles(graph))
    for cycle in cycles:
        for i in range(len(cycle)):
            u, v = cycle[i], cycle[(i + 1) % len(cycle)]
            if graph.has_edge(u, v):
                graph.remove_edge(u, v)
                break
    return graph

def part_one_real(list_data: List[str], eval_date: List[str], plot_graph: False) -> int:
    ordering_map = parse_rules_to_hashmap(list_data)
    
    ####################
    if plot_graph:
        G = nx.DiGraph()
        for key, values in ordering_map.items():
            for value in values:
                G.add_edge(key, value)
        
        simplified_graph = simplify_graph(G)
        plt.figure(figsize=(12, 8))
        pos = nx.circular_layout(simplified_graph)  # Circular layout since it's a circular graph
        nx.draw(
            simplified_graph,
            pos,
            with_labels=True,
            node_size=700,
            node_color="lightblue",
            font_size=10,
            font_color="black",
            edge_color="gray",
        )
        plt.title("Simplified Circular Graph")
        plt.show()
    ###################
    
    c_t = 0
    for eval_sequence in eval_date:
        eval_sequence = list(map(int, eval_sequence.split(",")))
        if is_update_valid_with_hashmap(eval_sequence, ordering_map):
            c_t += find_middle(eval_sequence)
    return c_t

def fix_eval_sequence(eval_sequence, ordering_map):
    relevant_rules = {page: ordering_map[page] for page in eval_sequence if page in ordering_map}
    
    in_degree = defaultdict(int)
    for page, dependencies in relevant_rules.items():
        for dependent in dependencies:
            if dependent in eval_sequence:
                in_degree[dependent] += 1
        if page not in in_degree:
            in_degree[page] = 0

    queue = deque([page for page in eval_sequence if in_degree[page] == 0])
    sorted_sequence = []
    
    while queue:
        current = queue.popleft()
        sorted_sequence.append(current)
        if current in relevant_rules:
            for dependent in relevant_rules[current]:
                if dependent in eval_sequence:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        queue.append(dependent)

    if len(sorted_sequence) != len(eval_sequence):
        logger.error("Cycle detected in the dependencies!")
        return eval_sequence

    return sorted_sequence

def part_two(list_data: List[str], eval_date: List[str]) -> int:
    ordering_map = parse_rules_to_hashmap(list_data)

    c_t = 0
    for eval_sequence in eval_date:
        eval_sequence = list(map(int, eval_sequence.split(",")))
        if not is_update_valid_with_hashmap(eval_sequence, ordering_map):
            fixed_sequence = fix_eval_sequence(eval_sequence, ordering_map)
            c_t += find_middle(fixed_sequence)
    return c_t
    
def main():
    setup_logging()
    args = parse_args()
    list_data = read_input(args.input_path[0])
    eval_data = read_input(args.input_path[1])
    
    result_one = part_one_real(list_data, eval_data, plot_graph=True)
    print(f"Part 1: {result_one}")

    result_two = part_two(list_data, eval_data)
    print(f"Part 2: {result_two}")

if __name__ == "__main__":
    main()

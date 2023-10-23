from __future__ import annotations
import pandas as pd
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, node: str, cumulative_value: int, remaining_edges: int, ancestors: List[str] = None) -> None:
        self.node = node
        self.cumulative_value = cumulative_value
        self.remaining_edges = remaining_edges
        self.ancestors = ancestors or []
        self.children: List[TreeNode] = []

def build_tree(df_nodes: pd.DataFrame, df_edges: pd.DataFrame, start_node: str, remaining_edges: int) -> TreeNode:
    root = TreeNode(start_node, 0, remaining_edges)
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()

        if remaining_edges == 0:
            continue
        
        for _, edge in df_edges[df_edges['start'] == current_node.node].iterrows():
            dest = edge['dest']
            weight = edge['weight']
            node_weight = df_nodes.loc[df_nodes['node'] == dest, 'value'].iloc[0]
            
            if weight <= current_node.remaining_edges:
                if dest in current_node.ancestors:
                    new_value = current_node.cumulative_value
                else:
                    new_value = current_node.cumulative_value + node_weight
                
                new_node = TreeNode(dest, new_value, current_node.remaining_edges - weight, current_node.ancestors + [current_node.node])
                current_node.children.append(new_node)
                queue.append(new_node)
    
    return root

def print_tree(node: TreeNode, depth: int = 0) -> None:
    print("  " * depth + f"{node.node}: value={node.cumulative_value}, edges={node.remaining_edges}, ancestors={node.ancestors}")
    for child in node.children:
        print_tree(child, depth + 1)

def find_paths_with_largest_value(root: TreeNode) -> List[TreeNode]:
    if not root.children:
        return [root]
    
    largest_paths: List[TreeNode] = []
    largest_value = max(root.children, key=lambda node: node.cumulative_value).cumulative_value
    
    for child in root.children:
        if child.cumulative_value == largest_value:
            largest_paths.extend(find_paths_with_largest_value(child))
    
    return largest_paths

def main() -> str:
    xls = pd.ExcelFile("oitm_tour.xlsx")
    
    df_beers = pd.read_excel(xls, "TOUR_BEERS", header=None)
    df_beers.columns = ['node', 'value']
    
    df_roads = pd.read_excel(xls, "TOUR_ROADS", header=None)
    df_roads.columns = ['start', 'dest', 'weight']

    df_swapped = df_roads.copy()
    df_swapped['start'], df_swapped['dest'] = df_roads['dest'], df_roads['start']
    df_swapped = df_swapped.iloc[3:]
    df_bidirectional = pd.concat([df_roads, df_swapped])

    root = build_tree(df_beers, df_bidirectional, "FL", 24)
    print_tree(root)
    largest_path = find_paths_with_largest_value(root)
    return f'[{largest_path[0].cumulative_value},{",".join(largest_path[0].ancestors)}]'

if __name__ == "__main__":
    print(main())
    
from collections import deque


def route_between_nodes_v1(graph: list, node1: str, node2: str):
    """Given a directed graph, design an algorithm to find out whether there is a route between two nodes (node1 to node2 or node2 to node1)

    Input:
        - the graph is represented as an adjacency list:
            adj_list = {
                "A": ["B"],
                "B": ["A", "C"],
                "C": ["D"],
                "D": []
            }
        - node1, node2
        - a directed graph (a unidirected graph where one node can only travel in one direction along the edge). a node cannot direct to itself.
        - valid graphs: A -> B -> C -> D, A -> B -> C -> D -> A and invalid graphs: A <- (node A pointing to itself)
        - the values of the nodes are strings and they are not necessarily ordered in an alphabetical order.
        - the values of the nodes are also distinct (no duplicates)
    Output: boolean (T/F)
        - route is counted as an edge or edges connected together by nodes that connect node1 and node2
        - for example, in the graph A -> B -> C -> D, there is a route between A and B (direct), and there is a route between A and D (indirect via B -> C)

    Algorithm:
    - Create a set called visited to avoid re-visiting a node: visited = set()
    - Check the node1's neighbors: neighbors = adj_list[node1]
        - Add node1 to the visited set
    - If node2 in neighbors, return True (direct route)
    - If node2 is not in neighbors:
        - Loop through each neighbor in neighbors:
            - If neighbor is not in visited:
                - Check if adj_list[neighbor] has node2:
                    - If yes: return True
    - Return false after checking every route
    """
    to_visit = deque([node1])
    visited = set([node1])

    while to_visit:
        node = to_visit.popleft()
        for nei in graph[node]:
            if nei == node2:
                return True
            else:
                if nei not in visited:
                    visited.add(nei)
                    to_visit.append(nei)
    return False

def test(func, graph, pairs: list):
    for u, v in pairs:
        print(func(graph, u, v))
        
graph = {"A": ["B"], "B": ["A", "C"], "C": ["D"], "D": []}
pairs = [["A", "B"], ["A", "D"], ["A", "C"], ["C", "A"], ["B", "A"]]
test(route_between_nodes_v1, graph, pairs)

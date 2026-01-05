from collections import deque

def build_order(projects, dependencies):
    """You are given a list of projects and a list of dependencies (which is a list of pairs of
       projects, where the second project is dependent on the first project). All of a project's dependencies
       must be built before the project is. Find a build order that will allow the projects to be built. If there
       is no valid build order, return an error.
       
       Input:
       - projects: [a, b, c, d, e, f]
       - dependencies: [(a, d), (f, b), (b, d), (f, a), (d, c)]
       Output: [f, e, a, b, d, c]
       
    Algorithm: using an adjacency list and queue
    Build an adjacency list where key is the prereq project and value is the list of projects that depend on the prereq
    adj_list = {
        a: ["d"],
        b: ["d"],
        c: [],
        d: ["c"],
        e: 0, [],
        f: 0, ["a", "b"]
    }
    - visited = set()
    - to_visit = [adj_list.keys()[0]]
    - Loop through each project in the to_visit list:
        - If the project has not been visited, add it to the visited set(): visited.add(project)
        - If the project has any value, add those value to the to_visit list: to_visit.append(value)
        - Check if the project is in the dependency list 
    """
    adj_list = {proj: [] for proj in projects}
    in_degree = {proj: 0 for proj in projects}
    
    for prereq, dep in dependencies:
        adj_list[prereq].append(dep)
        in_degree[dep] += 1
    
    queue = [proj for proj in projects if in_degree[proj] == 0]
    build_order_result = []
    
    while queue:
        current = queue.pop(0)
        build_order_result.append(current)
        for nei in adj_list[current]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    if len(build_order_result) != len(projects):
        raise Exception("Error: No valid build order (circular dependency)")
    
    return build_order_result


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
print(build_order(projects, dependencies))
            
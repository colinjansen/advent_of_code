from collections import defaultdict, deque
from functools import lru_cache

def parse():
    D = defaultdict(list)
    with open("_input/day11.txt") as f:
        for line in f.readlines():
            parts = line.strip().split(': ')
            D[parts[0]] = parts[1].split(" ")
    return D

def condense_graph(graph, sccs):
    """Build a DAG where each SCC collapses to a single node."""
    node_to_scc = {}
    for i, scc in enumerate(sccs):
        for node in scc:
            node_to_scc[node] = i

    dag = defaultdict(set)
    for u, vs in graph.items():
        for v in vs:
            if node_to_scc[u] != node_to_scc[v]:
                dag[node_to_scc[u]].add(node_to_scc[v])

    return dag, node_to_scc

def count_paths(graph, start, end, required_nodes=[]):
    """
    Count paths by first condensing SCCs, then doing a DAG DP where a bitmask
    tracks which required nodes have been visited so far.
    """
    sccs = tarjan_scc(graph)
    dag, node_to_scc = condense_graph(graph, sccs)

    start_scc = node_to_scc[start]
    end_scc = node_to_scc[end]

    req = list(required_nodes)
    req_index = {n: i for i, n in enumerate(req)}
    FULL = (1 << len(req)) - 1

    # Required mask per SCC
    scc_mask = [0] * len(sccs)
    for node, idx in req_index.items():
        scc_mask[node_to_scc[node]] |= 1 << idx

    @lru_cache(None)
    def dfs(scc, mask):
        mask |= scc_mask[scc]

        if scc == end_scc:
            return 1 if mask == FULL else 0

        total = 0
        for nxt in dag.get(scc, []):
            total += dfs(nxt, mask)
        return total

    return dfs(start_scc, 0)

def tarjan_scc(graph):
    """
    Tarjan's algorithm: single DFS that assigns each node an index and a
    lowlink (earliest reachable index). When a node is the root of an SCC
    (lowlink == index), pop the stack to form that component.
    """
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in indices:
            strongconnect(node)

    return sccs

def compute_reachable(graph, targets):
    """Reverse-BFS to find all nodes that can reach any target node."""
    reverse = defaultdict(list)
    for u, vs in graph.items():
        for v in vs:
            reverse[v].append(u)

    reachable = set()
    q = deque(targets)
    reachable.update(targets)

    while q:
        node = q.popleft()
        for prev in reverse[node]:
            if prev not in reachable:
                reachable.add(prev)
                q.append(prev)

    return reachable


d = parse()
print('part 1:', count_paths(d, 'you', 'out'))
print('part 2:', count_paths(d, 'svr', 'out', ['dac', 'fft']))

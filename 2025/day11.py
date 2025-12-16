from collections import defaultdict, deque
from functools import lru_cache

def parse():
    D = defaultdict(list)
    with open("_input/day11.txt") as f:
        for line in f.readlines():
            parts = line.strip().split(': ')
            D[parts[0]] = parts[1].split(" ")
    return D

def count_paths(graph, start, end, required_nodes=[]):
    req = list(required_nodes)
    req_index = {n: i for i, n in enumerate(req)}
    FULL = (1 << len(req)) - 1

    # Reachability pruning sets
    can_reach_end = compute_reachable(graph, [end])
    can_reach_req = [
        compute_reachable(graph, [r]) for r in req
    ]

    @lru_cache(None)
    def dfs(node, seen_mask, visited):
        # Prune: can't reach end
        if node not in can_reach_end:
            return 0

        # Prune: missing required nodes unreachable
        for i in range(len(req)):
            if not (seen_mask & (1 << i)) and node not in can_reach_req[i]:
                return 0

        # Update mask
        if node in req_index:
            seen_mask |= 1 << req_index[node]

        if node == end:
            return 1 if seen_mask == FULL else 0

        total = 0
        for nxt in graph.get(node, []):
            if nxt not in visited:
                total += dfs(
                    nxt,
                    seen_mask,
                    visited | {nxt}
                )
        return total

    return dfs(start, 0, frozenset([start]))

def condense_graph(graph, sccs):
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

def count_paths_scc(graph, start, end, required_nodes=[]):
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
print(count_paths_scc(d, 'you', 'out'))
print(count_paths_scc(d, 'svr', 'out', ['dac', 'fft']))

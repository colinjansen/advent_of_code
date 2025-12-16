from collections import defaultdict
from sympy import Matrix, eye


def parse():
    graph = defaultdict(list)
    with open("_input/day11.txt") as f:
        for line in f:
            node, neighbors = line.strip().split(": ")
            graph[node] = neighbors.split()
    return graph


def tarjan_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs = []

    def visit(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph.get(v, []):
            if w not in indices:
                visit(w)
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
            visit(node)

    return sccs


def condense_graph(graph, sccs):
    node_to_scc = {}
    for i, scc in enumerate(sccs):
        for node in scc:
            node_to_scc[node] = i

    dag = defaultdict(set)
    for u, vs in graph.items():
        for v in vs:
            su, sv = node_to_scc[u], node_to_scc[v]
            if su != sv:
                dag[su].add(sv)

    return dag, node_to_scc


def path_count_matrix(dag, nodes, start, end, blocked=None):
    blocked = set() if blocked is None else set(blocked)
    keep = [n for n in nodes if n not in blocked or n in (start, end)]
    if start not in keep or end not in keep:
        return 0

    index = {node: i for i, node in enumerate(keep)}
    size = len(keep)
    adj = Matrix.zeros(size)
    for u in keep:
        ui = index[u]
        for v in dag.get(u, []):
            if v in index:
                adj[ui, index[v]] += 1

    fundamental = (eye(size) - adj).inv()
    return int(fundamental[index[start], index[end]])


def count_paths_linear_algebra(graph, start, end, required=None):
    required = required or []
    sccs = tarjan_scc(graph)
    dag, node_to_scc = condense_graph(graph, sccs)

    start_scc = node_to_scc[start]
    end_scc = node_to_scc[end]
    req_scc = []
    seen_req = set()
    for r in required:
        scc_id = node_to_scc[r]
        if scc_id not in seen_req:
            seen_req.add(scc_id)
            req_scc.append(scc_id)

    all_nodes = list(range(len(sccs)))
    important = set(req_scc) | {start_scc, end_scc}

    pair_counts = {}
    for u in important:
        for v in important:
            if u == v:
                continue
            blocked = important - {u, v}
            # Exclude other important nodes so each segment is disjoint with respect to them.
            pair_counts[(u, v)] = path_count_matrix(dag, all_nodes, u, v, blocked)

    if not req_scc:
        return pair_counts.get((start_scc, end_scc), 0)

    n = len(req_scc)
    full_mask = (1 << n) - 1
    dp = [dict() for _ in range(1 << n)]

    for i, scc_id in enumerate(req_scc):
        ways = pair_counts.get((start_scc, scc_id), 0)
        if ways:
            dp[1 << i][i] = ways

    for mask in range(1 << n):
        for i, ways in dp[mask].items():
            if not ways:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                transition = pair_counts.get((req_scc[i], req_scc[j]), 0)
                if transition:
                    next_mask = mask | (1 << j)
                    dp[next_mask][j] = dp[next_mask].get(j, 0) + ways * transition

    total = 0
    for i, ways in dp[full_mask].items():
        finish = pair_counts.get((req_scc[i], end_scc), 0)
        total += ways * finish
    return total


if __name__ == "__main__":
    graph = parse()
    print(count_paths_linear_algebra(graph, "you", "out"))
    print(count_paths_linear_algebra(graph, "svr", "out", ["dac", "fft"]))

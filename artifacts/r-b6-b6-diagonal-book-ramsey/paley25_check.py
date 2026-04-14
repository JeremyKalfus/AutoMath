from itertools import combinations

ELTS = [(a, b) for a in range(5) for b in range(5)]


def sub(x, y):
    return ((x[0] - y[0]) % 5, (x[1] - y[1]) % 5)


def mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)


nonzero = [x for x in ELTS if x != (0, 0)]
squares = {mul(x, x) for x in nonzero}

adj = {x: set() for x in ELTS}
for x, y in combinations(ELTS, 2):
    if sub(x, y) in squares:
        adj[x].add(y)
        adj[y].add(x)

comp = {x: set(ELTS) - {x} - adj[x] for x in ELTS}

red_counts = {len(adj[x] & adj[y]) for x, y in combinations(ELTS, 2) if y in adj[x]}
blue_counts = {len(comp[x] & comp[y]) for x, y in combinations(ELTS, 2) if y in comp[x]}

print("square_set =", sorted(squares))
print("degree_set =", sorted({len(adj[x]) for x in ELTS}))
print("red_edge_common_counts =", sorted(red_counts))
print("blue_edge_common_counts =", sorted(blue_counts))
print("max_red_book =", max(len(adj[x] & adj[y]) for x, y in combinations(ELTS, 2) if y in adj[x]))
print("max_blue_book =", max(len(comp[x] & comp[y]) for x, y in combinations(ELTS, 2) if y in comp[x]))

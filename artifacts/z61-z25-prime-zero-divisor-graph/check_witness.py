import math
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_vertex(a, b):
    return (a, b) != (0, 0) and (a == 0 or b % 5 == 0)


def is_edge(x, y):
    return (x[0] * y[0]) % 61 == 0 and (x[1] * y[1]) % 25 == 0


def class_name(v):
    a, b = v
    if a == 0 and b % 5 != 0:
        return "A"
    if a == 0:
        return "B"
    if b == 0:
        return "C"
    return "D"


vertices = [(a, b) for a in range(61) for b in range(25) if is_vertex(a, b)]
assert len(vertices) == 324

A_vertices = [(0, b) for b in range(1, 25) if b % 5 != 0]
B_vertices = [(0, b) for b in (5, 10, 15, 20)]
C_vertices = [(a, 0) for a in range(1, 61)]
D_vertices = [(a, b) for a in range(1, 61) for b in (5, 10, 15, 20)]

A_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28]
B_labels = [1, 163, 167, 173]
C_labels = [n for n in range(11, 325) if is_prime(n) and n not in {163, 167, 173}] + [121]

assert len(C_labels) == 60

used_labels = set(A_labels) | set(B_labels) | set(C_labels)
D_labels = [n for n in range(1, 325) if n not in used_labels]
assert len(D_labels) == 240

labeling = {}
for vs, ls in [
    (A_vertices, A_labels),
    (B_vertices, B_labels),
    (C_vertices, C_labels),
    (D_vertices, D_labels),
]:
    for v, label in zip(vs, ls):
        labeling[v] = label

assert set(labeling) == set(vertices)
assert set(labeling.values()) == set(range(1, 325))

edge_type_counts = {}
bad_edges = []
for x, y in combinations(vertices, 2):
    if is_edge(x, y):
        key = "-".join(sorted([class_name(x), class_name(y)]))
        edge_type_counts[key] = edge_type_counts.get(key, 0) + 1
        if math.gcd(labeling[x], labeling[y]) != 1:
            bad_edges.append((x, labeling[x], y, labeling[y]))

if bad_edges:
    raise SystemExit(f"bad_edges={bad_edges}")

print("vertex_count=324")
print(f"edge_count={sum(edge_type_counts.values())}")
print(f"edge_type_counts={edge_type_counts}")
print("label_bijection_ok=1")
print("edge_coprime_ok=1")

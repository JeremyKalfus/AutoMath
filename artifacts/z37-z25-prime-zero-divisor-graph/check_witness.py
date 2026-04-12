import math
from itertools import combinations


def is_vertex(a, b):
    return (a, b) != (0, 0) and (a == 0 or b % 5 == 0)


def is_edge(x, y):
    return (x[0] * y[0]) % 37 == 0 and (x[1] * y[1]) % 25 == 0


def class_name(v):
    a, b = v
    if a == 0 and b % 5 != 0:
        return "A"
    if a == 0:
        return "B"
    if b == 0:
        return "C"
    return "D"


vertices = [(a, b) for a in range(37) for b in range(25) if is_vertex(a, b)]
assert len(vertices) == 204

A_vertices = [(0, b) for b in range(1, 25) if b % 5 != 0]
B_vertices = [(0, b) for b in (5, 10, 15, 20)]
C_vertices = [(a, 0) for a in range(1, 37)]
D_vertices = [(a, b) for a in range(1, 37) for b in (5, 10, 15, 20)]

A_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 86, 94, 106, 129, 141, 159, 172, 188]
B_labels = [1, 43, 47, 53]
C_labels = [
    11, 13, 17, 19, 23, 29, 31, 37, 41, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191,
]

used_labels = set(A_labels) | set(B_labels) | set(C_labels)
D_labels = [n for n in range(1, 205) if n not in used_labels]
assert len(D_labels) == 144

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
assert set(labeling.values()) == set(range(1, 205))

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

print("vertex_count=204")
print(f"edge_count={sum(edge_type_counts.values())}")
print(f"edge_type_counts={edge_type_counts}")
print("label_bijection_ok=1")
print("edge_coprime_ok=1")

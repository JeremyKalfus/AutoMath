import math
from itertools import combinations


P = 101
LABEL_BOUND = 5 * P + 19
A_LABELS = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108]
B_LABELS = [1, 263, 269, 271]
C_LABELS = [n for n in range(1, 312) if math.gcd(n, 6) == 1 and n not in {1, 263, 269, 271}]


def is_vertex(a, b):
    return (a, b) != (0, 0) and (a == 0 or b % 5 == 0)


def is_edge(x, y):
    return (x[0] * y[0]) % P == 0 and (x[1] * y[1]) % 25 == 0


def class_name(v):
    a, b = v
    if a == 0 and b % 5 != 0:
        return "A"
    if a == 0:
        return "B"
    if b == 0:
        return "C"
    return "D"


vertices = [(a, b) for a in range(P) for b in range(25) if is_vertex(a, b)]
assert len(vertices) == LABEL_BOUND

A_vertices = [(0, b) for b in range(1, 25) if b % 5 != 0]
B_vertices = [(0, b) for b in (5, 10, 15, 20)]
C_vertices = [(a, 0) for a in range(1, P)]
D_vertices = [(a, b) for a in range(1, P) for b in (5, 10, 15, 20)]

assert len(A_LABELS) == len(A_vertices) == 20
assert len(B_LABELS) == len(B_vertices) == 4
assert len(C_LABELS) == len(C_vertices) == 100

used_labels = set(A_LABELS) | set(B_LABELS) | set(C_LABELS)
D_LABELS = [n for n in range(1, LABEL_BOUND + 1) if n not in used_labels]
assert len(D_LABELS) == len(D_vertices) == 400

labeling = {}
for vs, ls in [
    (A_vertices, A_LABELS),
    (B_vertices, B_LABELS),
    (C_vertices, C_LABELS),
    (D_vertices, D_LABELS),
]:
    for v, label in zip(vs, ls):
        labeling[v] = label

assert set(labeling) == set(vertices)
assert set(labeling.values()) == set(range(1, LABEL_BOUND + 1))

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

print("vertex_count=524")
print(f"edge_count={sum(edge_type_counts.values())}")
print(f"edge_type_counts={edge_type_counts}")
print("label_bijection_ok=1")
print("edge_coprime_ok=1")

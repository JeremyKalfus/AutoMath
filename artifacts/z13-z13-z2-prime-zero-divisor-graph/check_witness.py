import math
from itertools import combinations


P = 13


def is_vertex(a, b, c):
    return (a, b, c) != (0, 0, 0) and not (a != 0 and b != 0 and c != 0)


def is_edge(x, y):
    return (
        (x[0] * y[0]) % P == 0
        and (x[1] * y[1]) % P == 0
        and (x[2] * y[2]) % 2 == 0
    )


def class_name(v):
    a, b, c = v
    if (a != 0, b != 0, c != 0) == (True, False, False):
        return "A"
    if (a != 0, b != 0, c != 0) == (False, True, False):
        return "B"
    if (a != 0, b != 0, c != 0) == (False, False, True):
        return "C"
    if (a != 0, b != 0, c != 0) == (True, True, False):
        return "D"
    if (a != 0, b != 0, c != 0) == (True, False, True):
        return "E"
    if (a != 0, b != 0, c != 0) == (False, True, True):
        return "F"
    raise ValueError(f"unexpected support pattern: {v}")


vertices = [(a, b, c) for a in range(P) for b in range(P) for c in range(2) if is_vertex(a, b, c)]
assert len(vertices) == 193

A_vertices = [(a, 0, 0) for a in range(1, P)]
B_vertices = [(0, b, 0) for b in range(1, P)]
C_vertices = [(0, 0, 1)]
D_vertices = [(a, b, 0) for a in range(1, P) for b in range(1, P)]
E_vertices = [(a, 0, 1) for a in range(1, P)]
F_vertices = [(0, b, 1) for b in range(1, P)]

A_labels = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32]
E_labels = [36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192]
C_labels = [1]
B_labels = [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37]
F_labels = [41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73]

used_labels = set(A_labels) | set(B_labels) | set(C_labels) | set(E_labels) | set(F_labels)
D_labels = [label for label in range(1, 194) if label not in used_labels]

labeling = {}
for vs, ls in [
    (A_vertices, A_labels),
    (B_vertices, B_labels),
    (C_vertices, C_labels),
    (D_vertices, D_labels),
    (E_vertices, E_labels),
    (F_vertices, F_labels),
]:
    assert len(vs) == len(ls)
    for v, label in zip(vs, ls):
        labeling[v] = label

assert set(labeling) == set(vertices)
assert set(labeling.values()) == set(range(1, 194))

class_sizes = {
    "A": len(A_vertices),
    "B": len(B_vertices),
    "C": len(C_vertices),
    "D": len(D_vertices),
    "E": len(E_vertices),
    "F": len(F_vertices),
}
assert class_sizes == {"A": 12, "B": 12, "C": 1, "D": 144, "E": 12, "F": 12}

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

expected_edge_type_counts = {
    "A-B": 144,
    "A-C": 12,
    "A-F": 144,
    "B-C": 12,
    "B-E": 144,
    "C-D": 144,
}
assert edge_type_counts == expected_edge_type_counts

print("vertex_count=193")
print(f"class_sizes={class_sizes}")
print(f"edge_count={sum(edge_type_counts.values())}")
print(f"edge_type_counts={edge_type_counts}")
print("label_bijection_ok=1")
print("edge_coprime_ok=1")

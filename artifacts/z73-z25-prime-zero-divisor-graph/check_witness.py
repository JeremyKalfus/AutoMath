from math import gcd


P = 73
Q = 25
N = 5 * P + 19

A_LABELS = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108]
B_LABELS = [1, 193, 197, 199]
C_LABELS = [
    5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
    89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
    181, 191, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
]


def classify(vertex):
    a, b = vertex
    if a == 0:
        return "A" if b % 5 != 0 else "B"
    return "C" if b == 0 else "D"


def is_zero_divisor(vertex):
    a, b = vertex
    return (a, b) != (0, 0) and (a == 0 or b % 5 == 0)


vertices = [(a, b) for a in range(P) for b in range(Q) if is_zero_divisor((a, b))]
class_vertices = {name: [] for name in "ABCD"}
for vertex in vertices:
    class_vertices[classify(vertex)].append(vertex)
for bucket in class_vertices.values():
    bucket.sort()

D_LABELS = sorted(set(range(1, N + 1)) - set(A_LABELS) - set(B_LABELS) - set(C_LABELS))
label_sets = {"A": A_LABELS, "B": B_LABELS, "C": C_LABELS, "D": D_LABELS}

expected_sizes = {"A": 20, "B": 4, "C": 72, "D": 288}
for name, expected in expected_sizes.items():
    actual = len(class_vertices[name])
    if actual != expected:
        raise SystemExit(f"class {name} size mismatch: {actual} != {expected}")
    if len(label_sets[name]) != expected:
        raise SystemExit(f"label set {name} size mismatch: {len(label_sets[name])} != {expected}")

labels = {}
for name in "ABCD":
    for vertex, label in zip(class_vertices[name], sorted(label_sets[name])):
        labels[vertex] = label

if set(labels.values()) != set(range(1, N + 1)):
    raise SystemExit("labels are not a bijection onto {1,...,N}")

edge_type_counts = {}
edge_count = 0
for i, u in enumerate(vertices):
    a, b = u
    for v in vertices[i + 1:]:
        c, d = v
        if (a * c) % P == 0 and (b * d) % Q == 0:
            edge_count += 1
            edge_type = "-".join(sorted((classify(u), classify(v))))
            edge_type_counts[edge_type] = edge_type_counts.get(edge_type, 0) + 1
            if gcd(labels[u], labels[v]) != 1:
                raise SystemExit(f"non-coprime edge found: {u}={labels[u]}, {v}={labels[v]}")

print(f"vertex_count = {len(vertices)}")
print(f"edge_count = {edge_count}")
print(f"edge_type_counts = {edge_type_counts}")
print("label_bijection_ok = 1")
print("edge_coprime_ok = 1")

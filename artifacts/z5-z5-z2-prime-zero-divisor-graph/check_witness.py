from math import gcd


def is_adjacent(x, y):
    return all(a == 0 or b == 0 for a, b in zip(x, y))


u = [1, 2, 3, 4]
vertices = []
labels = {}

c = (0, 0, 1)
vertices.append(c)
labels[c] = 1

for v, label in zip([(i, 0, 0) for i in u], [2, 4, 8, 16]):
    vertices.append(v)
    labels[v] = label

for v, label in zip([(0, i, 0) for i in u], [3, 5, 9, 25]):
    vertices.append(v)
    labels[v] = label

for v, label in zip([(i, 0, 1) for i in u], [14, 22, 26, 32]):
    vertices.append(v)
    labels[v] = label

for v, label in zip([(0, i, 1) for i in u], [7, 11, 13, 17]):
    vertices.append(v)
    labels[v] = label

remaining = [6, 10, 12, 15, 18, 19, 20, 21, 23, 24, 27, 28, 29, 30, 31, 33]
for v, label in zip([(i, j, 0) for i in u for j in u], remaining):
    vertices.append(v)
    labels[v] = label

assert len(vertices) == 33
assert sorted(labels.values()) == list(range(1, 34))

edges = []
violations = []
for i, x in enumerate(vertices):
    for y in vertices[i + 1 :]:
        if is_adjacent(x, y):
            edges.append((x, y))
            if gcd(labels[x], labels[y]) != 1:
                violations.append((x, y, labels[x], labels[y]))

print({"vertex_count": len(vertices), "edge_count": len(edges), "violations": violations})

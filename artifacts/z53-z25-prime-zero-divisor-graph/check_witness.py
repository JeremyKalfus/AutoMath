from math import gcd


P = 53
N = 5 * P + 19

A_LABELS = {
    4,
    8,
    9,
    16,
    25,
    27,
    86,
    94,
    106,
    129,
    141,
    159,
    172,
    188,
    212,
    215,
    235,
    258,
    265,
    282,
}
B_LABELS = {1, 43, 47, 53}
C_LABELS = {
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
}


def vertex_class(v):
    a, b = v
    if a == 0 and b % 5 != 0:
        return "A"
    if a == 0 and b % 5 == 0:
        return "B"
    if a != 0 and b == 0:
        return "C"
    if a != 0 and b % 5 == 0:
        return "D"
    raise ValueError(f"not a nonzero zero-divisor: {v}")


def zero_divisors():
    out = []
    for a in range(P):
        for b in range(25):
            if a == 0 and b == 0:
                continue
            if a == 0 or b % 5 == 0:
                out.append((a, b))
    return out


def edge(u, v):
    (a, b), (c, d) = u, v
    return (a * c) % P == 0 and (b * d) % 25 == 0


def main():
    vertices = sorted(zero_divisors())
    by_class = {"A": [], "B": [], "C": [], "D": []}
    for v in vertices:
        by_class[vertex_class(v)].append(v)

    d_labels = set(range(1, N + 1)) - A_LABELS - B_LABELS - C_LABELS
    labels_by_class = {
        "A": sorted(A_LABELS),
        "B": sorted(B_LABELS),
        "C": sorted(C_LABELS),
        "D": sorted(d_labels),
    }

    expected_sizes = {"A": 20, "B": 4, "C": 52, "D": 208}
    for key, size in expected_sizes.items():
        assert len(by_class[key]) == size, (key, len(by_class[key]), size)
        assert len(labels_by_class[key]) == size, (key, len(labels_by_class[key]), size)

    label_of = {}
    for key in ["A", "B", "C", "D"]:
        for v, lab in zip(by_class[key], labels_by_class[key]):
            label_of[v] = lab

    used_labels = set(label_of.values())
    edge_count = 0
    edge_type_counts = {"A-C": 0, "B-B": 0, "B-C": 0, "B-D": 0}
    bad_edges = []

    for i, u in enumerate(vertices):
        for v in vertices[i + 1 :]:
            if not edge(u, v):
                continue
            edge_count += 1
            cu = vertex_class(u)
            cv = vertex_class(v)
            pair = "-".join(sorted((cu, cv)))
            edge_type_counts[pair] = edge_type_counts.get(pair, 0) + 1
            if gcd(label_of[u], label_of[v]) != 1:
                bad_edges.append((u, v, label_of[u], label_of[v]))

    print("vertex_count =", len(vertices))
    print("class_sizes =", {k: len(v) for k, v in by_class.items()})
    print("edge_count =", edge_count)
    print("edge_type_counts =", edge_type_counts)
    print("label_bijection_ok =", int(used_labels == set(range(1, N + 1))))
    print("edge_coprime_ok =", int(not bad_edges))
    if bad_edges:
        print("first_bad_edge =", bad_edges[0])


if __name__ == "__main__":
    main()

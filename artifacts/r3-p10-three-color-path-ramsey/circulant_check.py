from functools import lru_cache
from itertools import product


TARGET = 10
COLORS = ("red", "blue", "green")


def build_adj(n, edge_color_fn):
    adj = [[0] * n for _ in COLORS]
    for i in range(n):
        for j in range(i + 1, n):
            color = edge_color_fn(i, j)
            cidx = COLORS.index(color)
            adj[cidx][i] |= 1 << j
            adj[cidx][j] |= 1 << i
    return adj


def has_p10(adj_bits):
    n = len(adj_bits)

    @lru_cache(maxsize=None)
    def dfs(v, used_mask, length):
        if length >= TARGET:
            return True
        candidates = adj_bits[v] & ~used_mask
        while candidates:
            bit = candidates & -candidates
            u = bit.bit_length() - 1
            if dfs(u, used_mask | bit, length + 1):
                return True
            candidates ^= bit
        return False

    for start in range(n):
        if dfs(start, 1 << start, 1):
            return True
    return False


def check_three_coloring(adj_by_color):
    return {color: has_p10(adj_by_color[idx]) for idx, color in enumerate(COLORS)}


def k17_lower_bound_coloring():
    groups = {
        "A": list(range(0, 5)),
        "B": list(range(5, 9)),
        "C": list(range(9, 13)),
        "D": list(range(13, 17)),
    }
    pair_color = {
        ("A", "B"): "red",
        ("C", "D"): "red",
        ("A", "C"): "blue",
        ("B", "D"): "blue",
        ("A", "D"): "green",
        ("B", "C"): "green",
    }
    vertex_group = {}
    for g, vs in groups.items():
        for v in vs:
            vertex_group[v] = g

    def edge_color(i, j):
        gi = vertex_group[i]
        gj = vertex_group[j]
        if gi == gj:
            return "red"
        key = tuple(sorted((gi, gj)))
        return pair_color[key]

    return build_adj(17, edge_color)


def circulant_adj_18(distance_colors):
    def edge_color(i, j):
        d = (j - i) % 18
        d = min(d, 18 - d)
        return distance_colors[d]

    return build_adj(18, edge_color)


def circulant_has_p10_from_zero(adj_bits):
    @lru_cache(maxsize=None)
    def dfs(v, used_mask, length):
        if length >= TARGET:
            return True
        candidates = adj_bits[v] & ~used_mask
        while candidates:
            bit = candidates & -candidates
            u = bit.bit_length() - 1
            if dfs(u, used_mask | bit, length + 1):
                return True
            candidates ^= bit
        return False

    return dfs(0, 1, 1)


def search_circulants():
    winners = []
    for assignment in product(COLORS, repeat=9):
        distance_colors = {d: assignment[d - 1] for d in range(1, 10)}
        adj = circulant_adj_18(distance_colors)
        if not any(circulant_has_p10_from_zero(adj[idx]) for idx in range(3)):
            winners.append(distance_colors)
    return winners


if __name__ == "__main__":
    lower = check_three_coloring(k17_lower_bound_coloring())
    print("k17_lower_bound_no_p10:", lower)
    winners = search_circulants()
    print("circulant_k18_counterexamples:", len(winners))
    for winner in winners[:10]:
        print(winner)

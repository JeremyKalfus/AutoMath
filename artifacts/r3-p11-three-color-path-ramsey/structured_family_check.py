from itertools import product


TARGET = 11
COLORS = (0, 1, 2)  # red, blue, green


def bit_iter(mask):
    while mask:
        lsb = mask & -mask
        yield lsb.bit_length() - 1
        mask ^= lsb


def component_masks(adj):
    n = len(adj)
    unseen = (1 << n) - 1
    comps = []
    while unseen:
        lsb = unseen & -unseen
        start = lsb.bit_length() - 1
        stack = [start]
        comp = 0
        unseen ^= lsb
        while stack:
            v = stack.pop()
            bit = 1 << v
            if comp & bit:
                continue
            comp |= bit
            nbrs = adj[v] & unseen
            unseen &= ~nbrs
            stack.extend(bit_iter(nbrs))
        comps.append(comp)
    return comps


def has_path_of_order(adj, target=TARGET):
    n = len(adj)
    comps = [c for c in component_masks(adj) if c.bit_count() >= target]
    if not comps:
        return False

    comp_of = [0] * n
    for comp in comps:
        for v in bit_iter(comp):
            comp_of[v] = comp

    failed = set()

    def dfs(v, used, depth, comp):
        if depth >= target:
            return True
        key = (v, used)
        if key in failed:
            return False
        remaining = comp & ~used
        if depth + remaining.bit_count() < target:
            failed.add(key)
            return False
        nxt = adj[v] & remaining
        for u in bit_iter(nxt):
            if dfs(u, used | (1 << u), depth + 1, comp):
                return True
        failed.add(key)
        return False

    for comp in comps:
        for v in bit_iter(comp):
            if dfs(v, 1 << v, 1, comp):
                return True
    return False


def build_graph(block_sizes, intra_colors, extra_block_colors=None):
    # Canonical 4-block inter-coloring:
    # AB, CD red; AC, BD blue; AD, BC green.
    blocks = []
    idx = 0
    for sz in block_sizes:
        blocks.append(list(range(idx, idx + sz)))
        idx += sz
    n = idx
    adj = [[0] * n for _ in COLORS]

    def add_edge(u, v, c):
        adj[c][u] |= 1 << v
        adj[c][v] |= 1 << u

    canonical = {
        (0, 1): 0,
        (2, 3): 0,
        (0, 2): 1,
        (1, 3): 1,
        (0, 3): 2,
        (1, 2): 2,
    }

    for i, block in enumerate(blocks[:4]):
        c = intra_colors[i]
        for a in range(len(block)):
            for b in range(a + 1, len(block)):
                add_edge(block[a], block[b], c)

    if len(blocks) == 5:
        c = intra_colors[4]
        block = blocks[4]
        for a in range(len(block)):
            for b in range(a + 1, len(block)):
                add_edge(block[a], block[b], c)

    for i in range(4):
        for j in range(i + 1, 4):
            c = canonical[(i, j)]
            for u in blocks[i]:
                for v in blocks[j]:
                    add_edge(u, v, c)

    if len(blocks) == 5:
        for i in range(4):
            c = extra_block_colors[i]
            for u in blocks[i]:
                for v in blocks[4]:
                    add_edge(u, v, c)

    return adj


def is_counterexample(adj):
    return all(not has_path_of_order(adj[c]) for c in COLORS)


def family_four_block():
    total = 0
    survivors = []
    for a in range(1, 19):
        for b in range(1, 20 - a):
            for c in range(1, 21 - a - b):
                d = 21 - a - b - c
                if d < 1:
                    continue
                sizes = (a, b, c, d)
                for intra in product(COLORS, repeat=4):
                    total += 1
                    adj = build_graph(sizes, intra)
                    if is_counterexample(adj):
                        survivors.append((sizes, intra))
    return total, survivors


def family_singleton_extension():
    total = 0
    survivors = []
    sizes = (5, 5, 5, 5, 1)
    for intra in product(COLORS, repeat=5):
        for extra in product(COLORS, repeat=4):
            total += 1
            adj = build_graph(sizes, intra, extra)
            if is_counterexample(adj):
                survivors.append((sizes, intra, extra))
    return total, survivors


def main():
    total4, survivors4 = family_four_block()
    total5, survivors5 = family_singleton_extension()

    print("family_four_block_total", total4)
    print("family_four_block_survivors", len(survivors4))
    if survivors4:
        print("family_four_block_example", survivors4[0])

    print("family_singleton_extension_total", total5)
    print("family_singleton_extension_survivors", len(survivors5))
    if survivors5:
        print("family_singleton_extension_example", survivors5[0])


if __name__ == "__main__":
    main()

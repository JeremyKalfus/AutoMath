from itertools import product


def valid_assignment(n: int, assignment: tuple[int, ...]) -> bool:
    maxd = n // 2
    edges_by_distance = {d: [] for d in range(1, maxd + 1)}
    for i in range(n):
        for j in range(i + 1, n):
            d = (j - i) % n
            d = min(d, n - d)
            edges_by_distance[d].append((i, j))

    masks = [[0] * n for _ in range(3)]
    for d, color in enumerate(assignment, start=1):
        for u, v in edges_by_distance[d]:
            masks[color][u] |= 1 << v
            masks[color][v] |= 1 << u

    for color in range(3):
        for u in range(n):
            mu = masks[color][u]
            vv = mu
            while vv:
                lsb = vv & -vv
                v = lsb.bit_length() - 1
                if v > u:
                    common = (mu & masks[color][v]).bit_count()
                    if color == 0:
                        if common >= 1:
                            return False
                    else:
                        if common >= 2:
                            return False
                vv ^= lsb
    return True


def first_example(n: int):
    maxd = n // 2
    for assignment in product(range(3), repeat=maxd):
        if valid_assignment(n, assignment):
            return assignment
    return None


if __name__ == "__main__":
    for n in range(17, 22):
        print(n, first_example(n))

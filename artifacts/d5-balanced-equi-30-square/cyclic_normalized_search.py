from itertools import combinations, permutations


N = 30
R = (0, 1, 2, 3, 4, 5)
PERMS = list(permutations(range(6)))


def main() -> None:
    support_candidates = 0
    for C in combinations(range(N), 6):
        counts = [0] * N
        table = [[0] * 6 for _ in range(6)]
        for i, r in enumerate(R):
            for j, c in enumerate(C):
                d = (c - r) % N
                table[i][j] = d
                counts[d] += 1

        if any(x == 0 for x in counts):
            continue
        if sum(max(0, x - 1) for x in counts) != 6:
            continue
        if max(counts) > 2:
            continue

        support_candidates += 1
        duplicated = {d for d, x in enumerate(counts) if x == 2}
        for perm in PERMS:
            deleted = [table[i][perm[i]] for i in range(6)]
            if set(deleted) != duplicated or len(set(deleted)) != 6:
                continue

            kept = []
            for i in range(6):
                for j in range(6):
                    if j != perm[i]:
                        kept.append(table[i][j])
            if len(set(kept)) == 30:
                print("FOUND", C, perm)
                print("deleted differences", deleted)
                print("kept differences", sorted(kept))
                return

    print("no normalized cyclic starter found")
    print("support candidates checked", support_candidates)


if __name__ == "__main__":
    main()

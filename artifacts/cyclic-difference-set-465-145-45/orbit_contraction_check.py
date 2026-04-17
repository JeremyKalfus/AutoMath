"""Exact bounded check for 2-invariant contractions in the (465,145,45) case.

This script is candidate-local proof support for the solve packet.

Assumption used outside the script:
    In a cyclic (465,145,45) difference set, 2 is a numerical multiplier
    because 2 | n = 100 and gcd(2, 465) = 1, so after translation one may
    assume D is fixed by x -> 2x.

What the script checks:
    Under that invariance, the contracted coefficient vectors modulo 93 and
    modulo 155 must be constant on 2-orbits. The standard contraction
    identities then impose exact sum, square-sum, and nonzero-correlation
    equations. This script exhaustively checks those orbit-compressed systems.
"""

from collections import defaultdict
from itertools import product


def two_orbits(modulus: int) -> list[tuple[int, ...]]:
    seen = {0}
    orbits = [(0,)]
    for x in range(1, modulus):
        if x in seen:
            continue
        orbit = []
        y = x
        while y not in orbit:
            orbit.append(y)
            y = (2 * y) % modulus
        seen.update(orbit)
        orbits.append(tuple(orbit))
    return orbits


def correlation_matrices(modulus: int, orbits: list[tuple[int, ...]]) -> list[list[list[int]]]:
    mats = []
    for orbit in orbits[1:]:
        rep = orbit[0]
        size = len(orbits)
        mat = [[0] * size for _ in range(size)]
        for i, oi in enumerate(orbits):
            for j, oj in enumerate(orbits):
                count = 0
                for u in oi:
                    for v in oj:
                        if (u - v) % modulus == rep:
                            count += 1
                mat[i][j] = count
        mats.append(mat)
    return mats


def tuple_data(max_entry: int) -> tuple[dict[tuple[int, int], list[tuple[int, ...]]], dict[tuple[int, int], int]]:
    buckets: dict[tuple[int, int], list[tuple[int, ...]]] = defaultdict(list)
    counts: dict[tuple[int, int], int] = defaultdict(int)
    for tup in product(range(max_entry + 1), repeat=6):
        key = (sum(tup), sum(x * x for x in tup))
        buckets[key].append(tup)
        counts[key] += 1
    return buckets, counts


def correlation_value(vec: tuple[int, ...], mat: list[list[int]]) -> int:
    total = 0
    for i, row in enumerate(mat):
        if vec[i] == 0:
            continue
        for j, coeff in enumerate(row):
            if coeff:
                total += coeff * vec[i] * vec[j]
    return total


def find_solutions(
    modulus: int,
    orbit_sizes: list[int],
    max_entry: int,
    total_sum: int,
    total_square_sum: int,
    target_correlation: int,
) -> list[tuple[int, ...]]:
    orbits = two_orbits(modulus)
    mats = correlation_matrices(modulus, orbits)
    buckets, _ = tuple_data(max_entry)
    sols = []

    if modulus == 93:
        # One size-1 orbit, one size-2 orbit, then six size-5 and six size-10 orbits.
        for a in range(max_entry + 1):
            for b in range(max_entry + 1):
                rem_sum = total_sum - a - 2 * b
                rem_sq = total_square_sum - a * a - 2 * b * b
                if rem_sum < 0 or rem_sq < 0:
                    continue
                for (sx, qx), xs in buckets.items():
                    rs = rem_sum - 5 * sx
                    rq = rem_sq - 5 * qx
                    if rs < 0 or rq < 0 or rs % 10 or rq % 10:
                        continue
                    ys = buckets.get((rs // 10, rq // 10), [])
                    for x in xs:
                        for y in ys:
                            vec = (a, b, *x, *y)
                            if all(correlation_value(vec, mat) == target_correlation for mat in mats):
                                sols.append(vec)
    elif modulus == 155:
        # One size-1 orbit, one size-4 orbit, then six size-5 and six size-20 orbits.
        for a in range(max_entry + 1):
            for b in range(max_entry + 1):
                rem_sum = total_sum - a - 4 * b
                rem_sq = total_square_sum - a * a - 4 * b * b
                if rem_sum < 0 or rem_sq < 0:
                    continue
                for (sx, qx), xs in buckets.items():
                    rs = rem_sum - 5 * sx
                    rq = rem_sq - 5 * qx
                    if rs < 0 or rq < 0 or rs % 20 or rq % 20:
                        continue
                    ys = buckets.get((rs // 20, rq // 20), [])
                    for x in xs:
                        for y in ys:
                            vec = (a, b, *x, *y)
                            if all(correlation_value(vec, mat) == target_correlation for mat in mats):
                                sols.append(vec)
    else:
        raise ValueError(f"unsupported modulus {modulus}")

    return sols


def main() -> None:
    configs = [
        {
            "modulus": 93,
            "max_entry": 5,
            "total_sum": 145,
            "total_square_sum": 100 + 45 * 5,
            "target_correlation": 45 * 5,
        },
        {
            "modulus": 155,
            "max_entry": 3,
            "total_sum": 145,
            "total_square_sum": 100 + 45 * 3,
            "target_correlation": 45 * 3,
        },
    ]

    for cfg in configs:
        orbits = two_orbits(cfg["modulus"])
        sizes = [len(orbit) for orbit in orbits]
        sols = find_solutions(
            modulus=cfg["modulus"],
            orbit_sizes=sizes,
            max_entry=cfg["max_entry"],
            total_sum=cfg["total_sum"],
            total_square_sum=cfg["total_square_sum"],
            target_correlation=cfg["target_correlation"],
        )
        print(f"mod {cfg['modulus']} orbit sizes: {sizes}")
        print(f"mod {cfg['modulus']} solutions: {len(sols)}")


if __name__ == "__main__":
    main()

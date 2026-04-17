"""Exact bounded check for 5-orbit-constant contractions in the (781,300,115) case.

Assumption used outside the script:
    The packeted contracted-multiplier criterion allows t = 5 as a valid
    multiplier on the quotients modulo 11 and 71. After translation, the
    contracted coefficient vectors may therefore be taken constant on
    multiplication-by-5 orbits.

What the script checks:
    Modulo 71, the contraction has one fixed residue class and fourteen
    nonzero 5-orbits. The standard contracted identities impose exact sum,
    square-sum, and nonzero-correlation equations on the resulting fifteen
    orbit values. This script searches that reduced integer system.
"""

from collections import Counter


def five_orbits(modulus: int) -> list[tuple[int, ...]]:
    seen = {0}
    orbits = [(0,)]
    for x in range(1, modulus):
        if x in seen:
            continue
        orbit = []
        y = x
        while y not in orbit:
            orbit.append(y)
            y = (5 * y) % modulus
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


def multiset_counts(length: int, total_sum: int, total_sq: int, max_entry: int) -> list[Counter[int]]:
    out: list[Counter[int]] = []

    def rec(value: int, left_n: int, left_s: int, left_q: int, cur: Counter[int]) -> None:
        if value < 0:
            if left_n == left_s == left_q == 0:
                out.append(+cur)
            return
        if left_n < 0 or left_s < 0 or left_q < 0:
            return
        max_count = min(left_n, left_s // value if value else left_n)
        for count in range(max_count, -1, -1):
            sq = count * value * value
            if sq > left_q:
                continue
            if count:
                cur[value] = count
            rec(value - 1, left_n - count, left_s - count * value, left_q - sq, cur)
            if count:
                del cur[value]

    rec(max_entry, length, total_sum, total_sq, Counter())
    return out


def search_for_solution(a: int, mats: list[list[list[int]]], target: int) -> tuple[int, ...] | None:
    total_sum = (300 - a) // 5
    total_sq = (1450 - a * a) // 5
    multisets = multiset_counts(length=14, total_sum=total_sum, total_sq=total_sq, max_entry=11)

    linear = []
    pair = []
    for mat in mats:
        lin = [mat[0][i] + mat[i][0] for i in range(1, 15)]
        quad = [[0] * 14 for _ in range(14)]
        for i in range(14):
            for j in range(14):
                ii = i + 1
                jj = j + 1
                if i == j:
                    quad[i][j] = mat[ii][jj]
                else:
                    quad[i][j] = mat[ii][jj] + mat[jj][ii]
        linear.append(lin)
        pair.append(quad)

    for counts in multisets:
        max_value = max(v for v, c in counts.items() if c)
        counts[max_value] -= 1
        if counts[max_value] == 0:
            del counts[max_value]

        vec = [0] * 14
        vec[0] = max_value
        partials = [a * linear[s][0] * max_value + pair[s][0][0] * max_value * max_value for s in range(14)]
        rem_sum = total_sum - max_value
        rem_sq = total_sq - max_value * max_value

        def dfs(pos: int, counts: Counter[int], rem_sum: int, rem_sq: int, partials: list[int]) -> tuple[int, ...] | None:
            if pos == 14:
                if rem_sum == rem_sq == 0 and all(x == target for x in partials):
                    return tuple([a] + vec)
                return None
            if rem_sum < 0 or rem_sq < 0:
                return None
            left = 14 - pos
            if rem_sum > 11 * left or rem_sq > 121 * left:
                return None
            # Lower square bound from Cauchy.
            if left and rem_sq * left < rem_sum * rem_sum:
                return None

            for value in sorted(counts, reverse=True):
                if counts[value] == 0:
                    continue
                vec[pos] = value
                new_partials = partials[:]
                for s in range(14):
                    inc = a * linear[s][pos] * value + pair[s][pos][pos] * value * value
                    for j in range(pos):
                        inc += pair[s][pos][j] * value * vec[j]
                    new_partials[s] += inc
                if any(x > target for x in new_partials):
                    continue
                counts[value] -= 1
                if counts[value] == 0:
                    del counts[value]
                sol = dfs(pos + 1, counts, rem_sum - value, rem_sq - value * value, new_partials)
                counts[value] = counts.get(value, 0) + 1
                if sol is not None:
                    return sol
            vec[pos] = 0
            return None

        sol = dfs(1, counts, rem_sum, rem_sq, partials)
        if sol is not None:
            return sol
    return None


def main() -> None:
    modulus = 71
    orbits = five_orbits(modulus)
    mats = correlation_matrices(modulus, orbits)
    target = 115 * 11
    print(f"mod {modulus} orbit sizes: {[len(o) for o in orbits]}")
    for a in (0, 5, 10):
        sol = search_for_solution(a, mats, target)
        print(f"a={a}: {'found solution ' + str(sol) if sol else 'no solution found'}")


if __name__ == "__main__":
    main()

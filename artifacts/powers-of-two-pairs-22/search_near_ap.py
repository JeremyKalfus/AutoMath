from itertools import combinations


WITNESS = tuple(range(-17, 27, 2))
WINDOW = tuple(range(-40, 71))
POWERS = {1 << k for k in range(10)}


def edge_count(values):
    values = tuple(sorted(values))
    total = 0
    for x, y in combinations(values, 2):
        if x + y in POWERS:
            total += 1
    return total


def best_odd_progression():
    best = None
    for a in range(-41, 64, 2):
        vals = tuple(range(a, a + 44, 2))
        score = edge_count(vals)
        item = (score, a, vals)
        if best is None or item > best:
            best = item
    return best


def best_local_k_swap(base, k):
    base = tuple(sorted(base))
    base_set = set(base)
    outside = tuple(v for v in WINDOW if v not in base_set)
    best = (edge_count(base), base)
    for removed in combinations(base, k):
        kept = tuple(v for v in base if v not in removed)
        for added in combinations(outside, k):
            cand = tuple(sorted(kept + added))
            score = edge_count(cand)
            if score > best[0]:
                best = (score, cand)
    return best


if __name__ == "__main__":
    witness_score = edge_count(WITNESS)
    ap_score, ap_start, ap_vals = best_odd_progression()
    one_swap = best_local_k_swap(WITNESS, 1)
    two_swap = best_local_k_swap(WITNESS, 2)

    print(f"witness_score={witness_score}")
    print(f"witness={WITNESS}")
    print(f"best_odd_progression_score={ap_score}")
    print(f"best_odd_progression_start={ap_start}")
    print(f"best_odd_progression={ap_vals}")
    print(f"best_one_swap_score={one_swap[0]}")
    print(f"best_one_swap={one_swap[1]}")
    print(f"best_two_swap_score={two_swap[0]}")
    print(f"best_two_swap={two_swap[1]}")

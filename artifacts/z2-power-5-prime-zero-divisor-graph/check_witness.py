from itertools import combinations
from json import dump
from math import gcd

OWNERS = {2: 0, 3: 1, 5: 2, 7: 3, 11: 4, 13: 4}
SUBSETS = list(range(1, 32))
LABELS = list(range(1, 32))


def required_mask(n: int) -> int:
    mask = 0
    for p, bit in OWNERS.items():
        if n % p == 0:
            mask |= 1 << bit
    return mask


def subset_key(mask: int) -> str:
    return "{" + ",".join(str(i + 1) for i in range(5) if mask & (1 << i)) + "}"


ALLOWED = {
    n: [s for s in SUBSETS if (s & required_mask(n)) == required_mask(n)]
    for n in LABELS
}

ORDER = sorted(LABELS, key=lambda n: (len(ALLOWED[n]), bin(required_mask(n)).count("1"), n))
MATCH = {}


def augment(label: int, seen: set[int]) -> bool:
    for subset in sorted(ALLOWED[label], key=lambda s: (bin(s).count("1"), s)):
        if subset in seen:
            continue
        seen.add(subset)
        if subset not in MATCH or augment(MATCH[subset], seen):
            MATCH[subset] = label
            return True
    return False


for label in ORDER:
    if not augment(label, set()):
        raise RuntimeError(f"no containing subset available for label {label}")

violations = []
for a, b in combinations(SUBSETS, 2):
    if a & b == 0:
        ga = MATCH[a]
        gb = MATCH[b]
        if gcd(ga, gb) != 1:
            violations.append((subset_key(a), subset_key(b), ga, gb))

if violations:
    raise RuntimeError(f"found gcd violations: {violations[:3]}")

witness = {subset_key(s): MATCH[s] for s in sorted(SUBSETS, key=lambda s: (bin(s).count("1"), s))}

with open("artifacts/z2-power-5-prime-zero-divisor-graph/witness.json", "w") as f:
    dump(witness, f, indent=2, sort_keys=False)
    f.write("\n")

hist = {}
for label in LABELS:
    k = bin(required_mask(label)).count("1")
    hist[k] = hist.get(k, 0) + 1

print(f"matching = {len(MATCH)}")
print(f"coprime_ok = {int(not violations)}")
print(f"required_set_hist = {hist}")

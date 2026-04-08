#!/usr/bin/env python3

import json
import math
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def primes_upto(n: int) -> list[int]:
    out = []
    for k in range(2, n + 1):
        for p in range(2, int(k**0.5) + 1):
            if k % p == 0:
                break
        else:
            out.append(k)
    return out


def factor_mask(m: int, owner: dict[int, int], primes: list[int]) -> int:
    x = m
    mask = 0
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            mask |= 1 << owner[p]
            while x % p == 0:
                x //= p
    if x > 1:
        mask |= 1 << owner[x]
    return mask


def mask_to_subset(mask: int) -> list[int]:
    return [i + 1 for i in range(8) if (mask >> i) & 1]


def build_owner_map() -> dict[int, int]:
    primes = primes_upto(254)
    owner = {2: 0}
    odd_primes = [p for p in primes if p != 2]
    for idx, p in enumerate(odd_primes):
        owner[p] = 1 + (idx % 7)
    return owner


def hopcroft_karp(adj: dict[int, list[int]], left: list[int], right: list[int]) -> tuple[int, dict[int, int | None], dict[int, int | None]]:
    inf = 10**9
    pair_u = {u: None for u in left}
    pair_v = {v: None for v in right}
    dist: dict[int, int] = {}

    def bfs() -> bool:
        q = deque()
        d_nil = inf
        for u in left:
            if pair_u[u] is None:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf
        while q:
            u = q.popleft()
            if dist[u] >= d_nil:
                continue
            for v in adj[u]:
                mate = pair_v[v]
                if mate is None:
                    d_nil = dist[u] + 1
                elif dist[mate] == inf:
                    dist[mate] = dist[u] + 1
                    q.append(mate)
        return d_nil != inf

    def dfs(u: int) -> bool:
        for v in adj[u]:
            mate = pair_v[v]
            if mate is None or (dist[mate] == dist[u] + 1 and dfs(mate)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = inf
        return False

    matching = 0
    while bfs():
        for u in left:
            if pair_u[u] is None and dfs(u):
                matching += 1
    return matching, pair_u, pair_v


def main() -> None:
    primes = primes_upto(254)
    owner = build_owner_map()
    vertices = [mask for mask in range(1, 256) if mask != 255]
    labels = list(range(1, 255))

    req_mask = {m: factor_mask(m, owner, primes) for m in labels}
    adj = {
        m: [v for v in vertices if (v & req_mask[m]) == req_mask[m]]
        for m in labels
    }

    matching, pair_u, pair_v = hopcroft_karp(adj, labels, vertices)
    if matching != 254:
        raise SystemExit(f"perfect matching failed: {matching}")

    violations = []
    for i, v in enumerate(vertices):
        for w in vertices[i + 1:]:
            if (v & w) == 0 and math.gcd(pair_v[v], pair_v[w]) != 1:
                violations.append((v, w, pair_v[v], pair_v[w]))
                break
        if violations:
            break
    if violations:
        raise SystemExit(f"coprimality violation: {violations[0]}")

    owner_groups: dict[str, list[int]] = {str(i + 1): [] for i in range(8)}
    for p in primes:
        owner_groups[str(owner[p] + 1)].append(p)

    witness = {
        "slug": "z2-power-8-prime-zero-divisor-graph",
        "title": "Is the zero-divisor graph Γ(Z_2^8) prime?",
        "owner_groups": owner_groups,
        "required_sets": {
            str(m): mask_to_subset(req_mask[m])
            for m in labels
        },
        "label_of_subset": {
            ",".join(map(str, mask_to_subset(v))): pair_v[v]
            for v in vertices
        },
    }
    (ROOT / "witness.json").write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")

    req_size_hist = {}
    for m in labels:
        size = len(mask_to_subset(req_mask[m]))
        req_size_hist[size] = req_size_hist.get(size, 0) + 1

    print("owner_groups =", owner_groups)
    print("matching =", matching)
    print("coprime_ok = 1")
    print("allowed_size_min =", min(len(adj[m]) for m in labels))
    print("allowed_size_max =", max(len(adj[m]) for m in labels))
    print("required_set_size_hist =", dict(sorted(req_size_hist.items())))
    print("witness_path =", ROOT / "witness.json")


if __name__ == "__main__":
    main()

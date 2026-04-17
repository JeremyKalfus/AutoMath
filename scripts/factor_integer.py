#!/usr/bin/env python3
from __future__ import annotations

import math
import random
import sys


def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for 64-bit integers, which covers AutoMath's current arithmetic range.
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (pow(x, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def factor_into(n: int, out: list[int]) -> None:
    if n == 1:
        return
    if is_probable_prime(n):
        out.append(n)
        return
    d = pollard_rho(n)
    factor_into(d, out)
    factor_into(n // d, out)


def format_factorization(n: int, factors: list[int]) -> str:
    parts = []
    for p in sorted(set(factors)):
        exp = factors.count(p)
        parts.append(f"{p}^{exp}" if exp > 1 else str(p))
    rhs = " * ".join(parts) if parts else "1"
    return f"{n} = {rhs}"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: python3 scripts/factor_integer.py <n> [<n> ...]", file=sys.stderr)
        return 1
    for raw in argv[1:]:
        try:
            n = int(raw)
        except ValueError:
            print(f"{raw}: not an integer", file=sys.stderr)
            return 1
        sign = -1 if n < 0 else 1
        n_abs = abs(n)
        if n_abs in (0, 1):
            print(f"{n} = {n}")
            continue
        factors: list[int] = []
        factor_into(n_abs, factors)
        if sign < 0:
            factors.append(-1)
        print(format_factorization(n, factors))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

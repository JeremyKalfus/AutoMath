from itertools import product


def paf(seq, shift):
    n = len(seq)
    return sum(seq[i] * seq[(i + shift) % n] for i in range(n))


def main():
    vals = list(range(-23, 24, 2))
    signatures = {}
    representatives = {}
    tuple_count = 0

    for seq in product(vals, repeat=5):
        if sum(seq) != 1:
            continue
        key = (sum(x * x for x in seq), paf(seq, 1), paf(seq, 2))
        signatures[key] = signatures.get(key, 0) + 1
        representatives.setdefault(key, seq)
        tuple_count += 1

    matches = []
    ordered_pair_count = 0
    for key, count in signatures.items():
        target = (186 - key[0], -46 - key[1], -46 - key[2])
        partner_count = signatures.get(target, 0)
        if not partner_count:
            continue
        ordered_pair_count += count * partner_count
        matches.append(
            {
                "x_signature": key,
                "y_signature": target,
                "x_count": count,
                "y_count": partner_count,
                "x_example": representatives[key],
                # If z has sum 1, then -z has sum -1 and the same PAF values.
                "y_example": tuple(-t for t in representatives[target]),
            }
        )

    q_values = sorted({row["x_signature"][0] for row in matches})

    print(f"sum1_tuples={tuple_count}")
    print(f"signature_count={len(signatures)}")
    print(f"matching_signature_pairs={len(matches)}")
    print(f"actual_ordered_pairs={ordered_pair_count}")
    print(f"qA_values={q_values}")
    print("sample_matches=")
    for row in matches[:20]:
        print(row)


if __name__ == "__main__":
    main()

import numpy as np


def main() -> None:
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    allowed_by_edge_count: dict[int, int] = {}

    for mask in range(1 << len(pairs)):
        f = np.zeros((5, 5), dtype=float)
        edge_count = 0
        for bit, (i, j) in enumerate(pairs):
            if (mask >> bit) & 1:
                f[i, j] = 1.0
                f[j, i] = 1.0
                edge_count += 1

        h = np.zeros((7, 7), dtype=float)
        h[:5, :5] = f
        for u in (5, 6):
            for v in range(5):
                h[u, v] = 1.0
                h[v, u] = 1.0

        if np.linalg.eigvalsh(h)[0] >= -3 - 1e-9:
            allowed_by_edge_count[edge_count] = allowed_by_edge_count.get(edge_count, 0) + 1

    print(allowed_by_edge_count)


if __name__ == "__main__":
    main()

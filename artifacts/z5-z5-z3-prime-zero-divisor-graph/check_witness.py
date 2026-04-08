import math


classes = {
    "V1": {6, 12, 18, 24},
    "V2": {1, 5, 13, 25},
    "V3": {7, 11},
    "V12": {2, 8, 9, 10, 15, 16, 20, 26, 27, 30, 32, 34, 36, 38, 39, 40},
    "V13": {3, 4, 14, 21, 22, 28, 33, 42},
    "V23": {17, 19, 23, 29, 31, 35, 37, 41},
}

edges = [
    ("V1", "V2"),
    ("V1", "V3"),
    ("V1", "V23"),
    ("V2", "V3"),
    ("V2", "V13"),
    ("V3", "V12"),
]

all_labels = set().union(*classes.values())
assert all_labels == set(range(1, 43))
assert sum(len(s) for s in classes.values()) == 42

violations = []
edge_count = 0
for left, right in edges:
    for a in classes[left]:
        for b in classes[right]:
            edge_count += 1
            if math.gcd(a, b) != 1:
                violations.append((left, a, right, b))

if violations:
    raise SystemExit(f"violations: {violations}")

print("partition_ok=1")
print("edge_coprime_ok=1")
print(f"edge_count={edge_count}")

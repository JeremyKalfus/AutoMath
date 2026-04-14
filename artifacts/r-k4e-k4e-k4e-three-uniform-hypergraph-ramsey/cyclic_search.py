from itertools import combinations


N = 13
COLORS = (0, 1, 2)


def orbit_rep(triple):
    pts = sorted(triple)
    reps = []
    for shift in range(N):
        shifted = sorted(((x - shift) % N) for x in pts)
        if shifted[0] == 0:
            reps.append(tuple(shifted))
    return min(reps)


triples = [tuple(t) for t in combinations(range(N), 3)]
orbit_index = {}
orbit_reps = []
for triple in triples:
    rep = orbit_rep(triple)
    if rep not in orbit_index:
        orbit_index[rep] = len(orbit_reps)
        orbit_reps.append(rep)


constraints = []
for quad in combinations(range(N), 4):
    ids = tuple(sorted(orbit_index[orbit_rep(triple)] for triple in combinations(quad, 3)))
    if ids not in constraints:
        constraints.append(ids)


var_to_constraints = {i: [] for i in range(len(orbit_reps))}
for idx, cons in enumerate(constraints):
    for var in set(cons):
        var_to_constraints[var].append(idx)


def violates(cons, assignment):
    counts = [0, 0, 0]
    for var in cons:
        color = assignment.get(var)
        if color is None:
            continue
        counts[color] += 1
    if max(counts) >= 3:
        return True
    unassigned = 4 - sum(counts)
    for color in COLORS:
        if counts[color] + unassigned >= 3:
            return False
    return True


def constraint_domain(cons, assignment):
    vars_in_cons = []
    for var in cons:
        if var not in assignment and var not in vars_in_cons:
            vars_in_cons.append(var)
    if not vars_in_cons:
        return None
    possible = {var: set() for var in vars_in_cons}
    for colors in product_colors(len(vars_in_cons)):
        trial = dict(assignment)
        for var, color in zip(vars_in_cons, colors):
            trial[var] = color
        if not violates(cons, trial):
            for var, color in zip(vars_in_cons, colors):
                possible[var].add(color)
    return possible


def product_colors(k):
    if k == 0:
        yield ()
        return
    if k == 1:
        for c in COLORS:
            yield (c,)
        return
    for prefix in product_colors(k - 1):
        for c in COLORS:
            yield prefix + (c,)


def propagate(assignment):
    changed = True
    while changed:
        changed = False
        for cons in constraints:
            if violates(cons, assignment):
                return None
            local = constraint_domain(cons, assignment)
            if local is None:
                continue
            for var, domain in local.items():
                if not domain:
                    return None
                if len(domain) == 1:
                    color = next(iter(domain))
                    if var in assignment:
                        if assignment[var] != color:
                            return None
                    else:
                        assignment[var] = color
                        changed = True
    return assignment


def choose_var(assignment):
    best_var = None
    best_score = None
    for var in range(len(orbit_reps)):
        if var in assignment:
            continue
        score = len(var_to_constraints[var])
        if best_score is None or score > best_score:
            best_var = var
            best_score = score
    return best_var


def search(assignment):
    assignment = propagate(dict(assignment))
    if assignment is None:
        return None
    if len(assignment) == len(orbit_reps):
        return assignment
    var = choose_var(assignment)
    for color in COLORS:
        assignment[var] = color
        result = search(assignment)
        if result is not None:
            return result
    assignment.pop(var, None)
    return None


solution = search({})
print(f"orbits={len(orbit_reps)} constraints={len(constraints)}")
if solution is None:
    print("NO_CYCLIC_SOLUTION")
else:
    print("CYCLIC_SOLUTION")
    for idx, rep in enumerate(orbit_reps):
        print(idx, rep, solution[idx])

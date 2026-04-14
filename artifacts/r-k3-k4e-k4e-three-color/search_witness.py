import argparse
import itertools
import math
import random
import time


RED = 0
BLUE = 1
GREEN = 2
COLOR_CHARS = "RBG"


class RamseyInstance:
    def __init__(self, n: int):
        self.n = n
        self.edges = []
        self.edge_index = {}
        for i in range(n):
            for j in range(i + 1, n):
                idx = len(self.edges)
                self.edges.append((i, j))
                self.edge_index[(i, j)] = idx
        self.triangles = []
        self.edge_to_tris = [[] for _ in self.edges]
        for tri in itertools.combinations(range(n), 3):
            a, b, c = tri
            eids = [
                self.edge_index[(a, b)],
                self.edge_index[(a, c)],
                self.edge_index[(b, c)],
            ]
            tid = len(self.triangles)
            self.triangles.append(tuple(eids))
            for eid in eids:
                self.edge_to_tris[eid].append(tid)
        self.quads = []
        self.edge_to_quads = [[] for _ in self.edges]
        for quad in itertools.combinations(range(n), 4):
            verts = list(quad)
            eids = []
            for i in range(4):
                for j in range(i + 1, 4):
                    eids.append(self.edge_index[(verts[i], verts[j])])
            qid = len(self.quads)
            self.quads.append(tuple(eids))
            for eid in eids:
                self.edge_to_quads[eid].append(qid)

    def random_coloring(self, red_bias: float = 0.24):
        blue_bias = (1.0 - red_bias) / 2.0
        cuts = (red_bias, red_bias + blue_bias)
        colors = []
        for _ in self.edges:
            x = random.random()
            if x < cuts[0]:
                colors.append(RED)
            elif x < cuts[1]:
                colors.append(BLUE)
            else:
                colors.append(GREEN)
        return colors

    def initial_state(self, colors):
        tri_red_counts = [0] * len(self.triangles)
        quad_blue_counts = [0] * len(self.quads)
        quad_green_counts = [0] * len(self.quads)
        bad_red = 0
        bad_blue = 0
        bad_green = 0
        for tid, eids in enumerate(self.triangles):
            cnt = sum(colors[eid] == RED for eid in eids)
            tri_red_counts[tid] = cnt
            if cnt == 3:
                bad_red += 1
        for qid, eids in enumerate(self.quads):
            bcnt = sum(colors[eid] == BLUE for eid in eids)
            gcnt = sum(colors[eid] == GREEN for eid in eids)
            quad_blue_counts[qid] = bcnt
            quad_green_counts[qid] = gcnt
            if bcnt >= 5:
                bad_blue += 1
            if gcnt >= 5:
                bad_green += 1
        return {
            "colors": colors,
            "tri_red_counts": tri_red_counts,
            "quad_blue_counts": quad_blue_counts,
            "quad_green_counts": quad_green_counts,
            "bad_red": bad_red,
            "bad_blue": bad_blue,
            "bad_green": bad_green,
        }

    def score(self, state):
        return state["bad_red"] + state["bad_blue"] + state["bad_green"]

    def apply_recolor(self, state, eid: int, new_color: int):
        colors = state["colors"]
        old_color = colors[eid]
        if old_color == new_color:
            return
        for tid in self.edge_to_tris[eid]:
            old_cnt = state["tri_red_counts"][tid]
            if old_cnt == 3:
                state["bad_red"] -= 1
            if old_color == RED:
                old_cnt -= 1
            if new_color == RED:
                old_cnt += 1
            state["tri_red_counts"][tid] = old_cnt
            if old_cnt == 3:
                state["bad_red"] += 1
        for qid in self.edge_to_quads[eid]:
            old_b = state["quad_blue_counts"][qid]
            old_g = state["quad_green_counts"][qid]
            if old_b >= 5:
                state["bad_blue"] -= 1
            if old_g >= 5:
                state["bad_green"] -= 1
            if old_color == BLUE:
                old_b -= 1
            elif old_color == GREEN:
                old_g -= 1
            if new_color == BLUE:
                old_b += 1
            elif new_color == GREEN:
                old_g += 1
            state["quad_blue_counts"][qid] = old_b
            state["quad_green_counts"][qid] = old_g
            if old_b >= 5:
                state["bad_blue"] += 1
            if old_g >= 5:
                state["bad_green"] += 1
        colors[eid] = new_color

    def recolor_delta(self, state, eid: int, new_color: int):
        old = self.score(state)
        old_color = state["colors"][eid]
        if old_color == new_color:
            return 0
        self.apply_recolor(state, eid, new_color)
        new = self.score(state)
        self.apply_recolor(state, eid, old_color)
        return new - old

    def hill_climb(self, restarts: int, steps: int, red_bias: float):
        best_state = None
        best_score = math.inf
        for restart in range(restarts):
            state = self.initial_state(self.random_coloring(red_bias=red_bias))
            current_score = self.score(state)
            if current_score < best_score:
                best_score = current_score
                best_state = self.copy_state(state)
            if current_score == 0:
                return state, restart, 0
            temperature = 1.5
            for step in range(steps):
                eid = random.randrange(len(self.edges))
                old_color = state["colors"][eid]
                move_colors = [c for c in (RED, BLUE, GREEN) if c != old_color]
                random.shuffle(move_colors)
                chosen = None
                chosen_delta = None
                for new_color in move_colors:
                    delta = self.recolor_delta(state, eid, new_color)
                    if delta <= 0:
                        chosen = new_color
                        chosen_delta = delta
                        break
                    if chosen is None or delta < chosen_delta:
                        chosen = new_color
                        chosen_delta = delta
                if chosen_delta <= 0 or random.random() < math.exp(-chosen_delta / max(temperature, 1e-6)):
                    self.apply_recolor(state, eid, chosen)
                    current_score += chosen_delta
                    if current_score < best_score:
                        best_score = current_score
                        best_state = self.copy_state(state)
                    if current_score == 0:
                        return state, restart, step + 1
                temperature *= 0.9997
        return best_state, None, None

    def copy_state(self, state):
        return {
            "colors": state["colors"][:],
            "tri_red_counts": state["tri_red_counts"][:],
            "quad_blue_counts": state["quad_blue_counts"][:],
            "quad_green_counts": state["quad_green_counts"][:],
            "bad_red": state["bad_red"],
            "bad_blue": state["bad_blue"],
            "bad_green": state["bad_green"],
        }

    def validate(self, colors):
        state = self.initial_state(colors[:])
        return self.score(state) == 0, state

    def encode(self, colors):
        return "".join(COLOR_CHARS[c] for c in colors)


def adjacency_by_color(instance: RamseyInstance, colors):
    n = instance.n
    adj = [[[False] * n for _ in range(n)] for _ in range(3)]
    for eid, (u, v) in enumerate(instance.edges):
        c = colors[eid]
        adj[c][u][v] = True
        adj[c][v][u] = True
    return adj


def exact_extension(instance: RamseyInstance, colors):
    assert instance.n == 20
    adj = adjacency_by_color(instance, colors)
    assigned = [-1] * 20
    red_set = set()
    blue_set = set()
    green_set = set()
    blue_deg = [0] * 20
    green_deg = [0] * 20

    def feasible(v, color):
        if color == RED:
            for u in red_set:
                if adj[RED][u][v]:
                    return False
            return True
        if color == BLUE:
            hits = [u for u in blue_set if adj[BLUE][u][v]]
            if len(hits) > 1:
                return False
            if len(hits) == 1 and blue_deg[hits[0]] >= 1:
                return False
            return True
        hits = [u for u in green_set if adj[GREEN][u][v]]
        if len(hits) > 1:
            return False
        if len(hits) == 1 and green_deg[hits[0]] >= 1:
            return False
        return True

    def apply(v, color):
        assigned[v] = color
        changed = []
        if color == RED:
            red_set.add(v)
            return changed
        if color == BLUE:
            blue_set.add(v)
            for u in blue_set:
                if u != v and adj[BLUE][u][v]:
                    blue_deg[u] += 1
                    blue_deg[v] += 1
                    changed.append(u)
            return changed
        green_set.add(v)
        for u in green_set:
            if u != v and adj[GREEN][u][v]:
                green_deg[u] += 1
                green_deg[v] += 1
                changed.append(u)
        return changed

    def undo(v, color, changed):
        if color == RED:
            red_set.remove(v)
        elif color == BLUE:
            for u in changed:
                blue_deg[u] -= 1
                blue_deg[v] -= 1
            blue_set.remove(v)
        else:
            for u in changed:
                green_deg[u] -= 1
                green_deg[v] -= 1
            green_set.remove(v)
        assigned[v] = -1

    def choose_vertex():
        best_v = None
        best_options = None
        for v in range(20):
            if assigned[v] != -1:
                continue
            options = [c for c in (RED, BLUE, GREEN) if feasible(v, c)]
            if not options:
                return v, []
            if best_options is None or len(options) < len(best_options):
                best_v = v
                best_options = options
                if len(best_options) == 1:
                    break
        return best_v, best_options

    def backtrack():
        v, options = choose_vertex()
        if v is None:
            return assigned[:]
        if not options:
            return None
        for color in options:
            changed = apply(v, color)
            out = backtrack()
            if out is not None:
                return out
            undo(v, color, changed)
        return None

    return backtrack()


def summarize_score(state):
    return {
        "total": state["bad_red"] + state["bad_blue"] + state["bad_green"],
        "red_triangles": state["bad_red"],
        "blue_j4": state["bad_blue"],
        "green_j4": state["bad_green"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260414)
    parser.add_argument("--restarts20", type=int, default=100)
    parser.add_argument("--steps20", type=int, default=40000)
    parser.add_argument("--restarts21", type=int, default=60)
    parser.add_argument("--steps21", type=int, default=50000)
    parser.add_argument("--red-bias", type=float, default=0.24)
    parser.add_argument("--skip21", action="store_true")
    args = parser.parse_args()

    random.seed(args.seed)
    t0 = time.time()

    inst20 = RamseyInstance(20)
    state20, restart20, step20 = inst20.hill_climb(
        restarts=args.restarts20, steps=args.steps20, red_bias=args.red_bias
    )
    ok20, validated20 = inst20.validate(state20["colors"])
    print(f"n=20 best score: {summarize_score(validated20)}")
    if ok20:
        print(f"n=20 witness found at restart={restart20} step={step20}")
        print(f"n=20 encoding: {inst20.encode(state20['colors'])}")
        ext = exact_extension(inst20, state20["colors"])
        print(f"n=20 exact one-vertex extension exists: {ext is not None}")
        if ext is not None:
            counts = {c: ext.count(c) for c in (RED, BLUE, GREEN)}
            print(
                "extension partition sizes: "
                f"R={counts[RED]} B={counts[BLUE]} G={counts[GREEN]}"
            )
            print("extension assignment:", "".join(COLOR_CHARS[c] for c in ext))
    else:
        print("n=20 witness not found; extension test skipped")

    if args.skip21:
        print(f"elapsed_seconds: {time.time() - t0:.2f}")
        return

    inst21 = RamseyInstance(21)
    state21, restart21, step21 = inst21.hill_climb(
        restarts=args.restarts21, steps=args.steps21, red_bias=args.red_bias
    )
    ok21, validated21 = inst21.validate(state21["colors"])
    print(f"n=21 best score: {summarize_score(validated21)}")
    if ok21:
        print(f"n=21 witness found at restart={restart21} step={step21}")
        print(f"n=21 encoding: {inst21.encode(state21['colors'])}")
    else:
        print("n=21 witness not found in bounded local search")

    print(f"elapsed_seconds: {time.time() - t0:.2f}")


if __name__ == "__main__":
    main()

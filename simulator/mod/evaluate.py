import random
from copy import deepcopy

def manhattan_like(a, b):
    """Hex distance metric in axial coordinates.

    Computes the Chebyshev-equivalent distance between two hex cells
    using axial (q, r) coordinates, derived from cube coordinates.
    """
    dq = abs(a[0] - b[0])
    dr = abs(a[1] - b[1])
    ds = abs((-a[0] - a[1]) - (-b[0] - b[1]))
    return max(dq, dr, ds)


def pivot_mobility(player, pieces, grid, get_legal_moves_fn, get_axis_control_fn, directions, in_grid_fn):
    pivot = next((p for p in pieces if p["type"] == "Pivot" and p["player"] == player), None)
    if not pivot:
        return 0
    legal = get_legal_moves_fn(pivot, pieces, grid, directions, in_grid_fn)
    axis_control = get_axis_control_fn(pieces, grid, directions, in_grid_fn)
    occupied = {(p["q"], p["r"]) for p in pieces}
    return sum(1 for h in legal if h not in occupied and h not in axis_control)


def evaluate_position(for_player, pieces, grid,
                      get_legal_moves_fn, get_axis_control_fn, manhattan_like_fn,
                      directions, in_grid_fn):
    me, opp = for_player, ("B" if for_player == "A" else "A")

    my_mob = pivot_mobility(me, pieces, grid,
                            get_legal_moves_fn, get_axis_control_fn,
                            directions, in_grid_fn)
    opp_mob = pivot_mobility(opp, pieces, grid,
                             get_legal_moves_fn, get_axis_control_fn,
                             directions, in_grid_fn)

    opp_pivot = next((p for p in pieces if p["type"] == "Pivot" and p["player"] == opp), None)
    avg_dist = 0
    if opp_pivot:
        mine = [p for p in pieces if p["player"] == me]
        dists = [manhattan_like_fn((p["q"], p["r"]),
                                   (opp_pivot["q"], opp_pivot["r"])) for p in mine]
        avg_dist = sum(dists) / len(dists) if dists else 0

    score = 3 * (my_mob - opp_mob) - 0.2 * avg_dist
    score += random.uniform(-0.05, 0.05)
    return score


def choose_best_move(for_player, pieces, grid,
                     get_legal_moves_fn, get_axis_control_fn, manhattan_like_fn,
                     directions, in_grid_fn,
                     randomize=False):
    candidates = []
    my_pieces = [p for p in pieces if p["player"] == for_player]

    for piece in my_pieces:
        legal = get_legal_moves_fn(piece, pieces, grid, directions, in_grid_fn)
        for move in legal:
            next_pieces = deepcopy(pieces)
            for np in next_pieces:
                if np["id"] == piece["id"]:
                    np["q"], np["r"] = move
                    break
            score = evaluate_position(for_player,
                                     next_pieces, grid,
                                     get_legal_moves_fn, get_axis_control_fn, manhattan_like_fn,
                                     directions, in_grid_fn)
            candidates.append((piece["id"], piece["type"], move[0], move[1], score))

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[4], reverse=True)
    if randomize and len(candidates) > 1:
        k = min(3, len(candidates))
        return random.choice(candidates[1:k])
    return candidates[0]

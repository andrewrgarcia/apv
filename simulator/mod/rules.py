
def get_legal_moves(
    piece,
    pieces,
    grid,
    directions,
    in_grid_fn,
):
    occupied = {(p["q"], p["r"]) for p in pieces}
    q, r = piece["q"], piece["r"]
    moves = []

    if piece["type"] == "Pivot":
        for dq, dr in directions:
            h = (q + dq, r + dr)
            if in_grid_fn(h, grid) and h not in occupied:
                moves.append(h)

    elif piece["type"] == "Axis":
        for dq, dr in directions:
            step = (q + dq, r + dr)
            while in_grid_fn(step, grid) and step not in occupied:
                moves.append(step)
                step = (step[0] + dq, step[1] + dr)

    elif piece["type"] == "Veil":
        for dq, dr in directions:
            landing = (q + 2 * dq, r + 2 * dr)
            if in_grid_fn(landing, grid) and landing not in occupied:
                moves.append(landing)

    elif piece["type"] == "Veil90":
        D = len(directions)
        for i in range(D):
            d1 = directions[i]
            d2 = directions[(i + 1) % D]
            landing = (q + d1[0] + d2[0], r + d1[1] + d2[1])
            if in_grid_fn(landing, grid) and landing not in occupied:
                moves.append(landing)

    return moves


def get_axis_control(
    pieces,
    grid,
    directions,
    in_grid_fn,
):
    control = set()

    for a in (p for p in pieces if p["type"] == "Axis"):
        for dq, dr in directions:
            step = (a["q"] + dq, a["r"] + dr)
            while (
                in_grid_fn(step, grid)
                and not any(p["q"] == step[0] and p["r"] == step[1] for p in pieces)
            ):
                control.add(step)
                step = (step[0] + dq, step[1] + dr)

    return control


def check_victory(
    pieces,
    grid,
    directions,
    add_hex_fn,
    in_grid_fn,
    get_legal_moves_fn,
    get_axis_control_fn,
):
    axis_control = get_axis_control_fn(pieces, grid, directions, in_grid_fn)
    occupied = {(p["q"], p["r"]) for p in pieces}

    for pivot in (p for p in pieces if p["type"] == "Pivot"):
        enemy = "A" if pivot["player"] == "B" else "B"

        # Adjacent hexes
        adj = [
            add_hex_fn((pivot["q"], pivot["r"]), d)
            for d in directions
        ]

        free_adj = [
            h for h in adj
            if in_grid_fn(h, grid) and h not in occupied and h not in axis_control
        ]

        legal_moves = get_legal_moves_fn(
            pivot, pieces, grid,
            directions,
            in_grid_fn,
        )

        if not free_adj and not legal_moves:
            return enemy

    return None

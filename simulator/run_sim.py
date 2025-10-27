import random
from statistics import mean, median
import time

from mod import (
    generate_hex_grid, initial_pieces, in_grid, add_hex,
    DIRECTIONS, PLAYERS,
    get_legal_moves, get_axis_control, check_victory,
    manhattan_like, choose_best_move,
)

def run_one_match(first_player, mirror=False, verbose=False, delay=0.0):
    grid = generate_hex_grid(4)
    pieces = initial_pieces()

    if mirror:
        for p in pieces:
            p["q"], p["r"] = -p["q"], -p["r"]
            p["player"] = "A" if p["player"] == "B" else "B"
        if verbose:
            print("MIRRORED")

    current = first_player
    winner = None
    turns = 0
    max_turns = 500
    last_states = []

    while not winner and turns < max_turns:
        turns += 1
        board_state = tuple(sorted((p["player"], p["type"], p["q"], p["r"]) for p in pieces))
        last_states.append(board_state)
        if len(last_states) > 8:
            last_states.pop(0)
        loop_detected = last_states.count(board_state) > 1

        move = choose_best_move(
            current, pieces, grid,
            get_legal_moves, get_axis_control, manhattan_like,
            DIRECTIONS, in_grid,
            randomize=loop_detected
        )

        if not move:
            winner = "A" if current == "B" else "B"
            break

        pid, ptype, q, r, score = move
        old = next((p for p in pieces if p["id"] == pid), None)
        old_q, old_r = old["q"], old["r"]
        old["q"], old["r"] = q, r

        maybe = check_victory(
            pieces, grid,
            DIRECTIONS, add_hex, in_grid,
            get_legal_moves, get_axis_control
        )

        if verbose:
            print(f"T{turns:03d}: {current} {ptype} ({old_q},{old_r})->({q},{r})")

        if maybe:
            winner = maybe
            break

        current = "A" if current == "B" else "B"
        if delay:
            time.sleep(delay)

    return winner, turns


def run_simulation_batch(n=20):
    stats = {"A": 0, "B": 0, "draw": 0}
    by_start = {"A": {"A": 0, "B": 0}, "B": {"A": 0, "B": 0}}
    turns_list = []

    for i in range(n):
        first = random.choice(PLAYERS)
        mirror = random.random() < 0.5
        print(f"Game {i+1}/{n} | First: {first} | Mirror: {mirror}")

        winner, turns = run_one_match(first, mirror=mirror, verbose=False)
        turns_list.append(turns)

        if winner:
            stats[winner] += 1
            by_start[first][winner] += 1
        else:
            stats["draw"] += 1

        print(f"Winner: {winner or 'None'} in {turns} turns")

    print("\nAPV Simulation Bias Report")
    print(f"Games: {n}")
    print(f"A wins: {stats['A']} | B wins: {stats['B']} | Draws: {stats['draw']}")
    print(f"Avg turns: {mean(turns_list):.2f} | Median: {median(turns_list):.2f} | Max: {max(turns_list)}")

    print("By starting player:")
    for starter in ["A", "B"]:
        print(f"  {starter} start: A {by_start[starter]['A']}, B {by_start[starter]['B']}")


if __name__ == "__main__":
    run_simulation_batch(200)

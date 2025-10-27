# APV Solver Benchmark Framework

This repository provides a self-play baseline for **APV (Axis · Pivot · Veil)** — a deterministic, perfect-information hex strategy game. It serves as a **benchmark opponent** for developing stronger APV engines.

The current agent uses a **greedy single-ply evaluation** with mobility and positional heuristics.
It is intentionally beatable.
Your task is to improve on it.

---

## Objective

Create an APV solver that:

1. Plays by the official APV rules
2. Demonstrates **consistent advantage** against the baseline greedy agent
3. Runs deterministically using perfect information
4. Can be integrated into automated evaluation using this simulator

You are free to build any solver architecture, including:

* Deep search (minimax, alpha-beta, transposition tables)
* Monte-Carlo Tree Search (MCTS)
* Reinforcement learning or AlphaZero-style policy/value networks
* Hybrid heuristic and simulation systems

---

## How Engines Are Evaluated

Your agent must provide a move-selection function compatible with:

```python
choose_best_move(for_player, pieces, grid, ...)
```

It will then be evaluated using `run_one_match()` and `run_simulation_batch()` in this repo:

```bash
python run_sim.py
```

The baseline runs:

* 200 games per batch (configurable)
* Randomized first-player
* 50% mirrored boards (spatial bias cancellation)
* Reporting win rates, draw rates, and turn-length distributions

A successful solver must **outperform the baseline** under these uniform test conditions.

---

## Contributing Your Engine

Develop your solver in **your own repository**.
When you have results:

1. Open a GitHub **Issue** titled:
   `Engine Submission: <your engine name>`
2. Include:

   * Brief description of implementation
   * Link to your public repo
   * Win-rate logs from benchmark evaluation
3. If accepted, your engine will be:

   * Linked from this project’s README as a recognized solver
   * Considered for a dedicated evaluation harness and future competition formats

This call to action is also documented in a GitHub Issue labeled **Enhancement**.

---

## Status

| Component                      | Purpose                       |   Status  |
| ------------------------------ | ----------------------------- | :-------: |
| Baseline greedy agent          | Minimum required benchmark    |  Complete |
| Engine submission process      | Competitor integration        |   Active  |
| Tournament framework           | Engine vs. engine scored runs | In design |
| ML/AlphaZero-style experiments | Advanced solver strength      |  Proposed |

---

## Research Focus

This project exists to support:

* Engine development methodology for deterministic strategy games
* Analysis of spatial initiative and containment dynamics
* Modern solver architectures applied to new perfect-information systems

If you are interested in contributing to the competitive engine ecosystem for APV, this simulator is the entry point.

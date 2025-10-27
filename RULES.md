# 🪖 APV — Rules of Engagement  
*A deterministic strategy game of foresight and containment.*

Playable online: [https://apvgame.vercel.app](https://apvgame.vercel.app)

---

## 1. Objective

Immobilize the opposing **Pivot (●)** — the command node —  
so it has **no legal moves** and all six adjacent hexes are blocked or controlled.  
No captures occur; victory arises purely from positional dominance.  
If both Pivots are immobilized simultaneously, the game is a **draw**.

---

## 2. Components

| Unit | Symbol | Count | Description |
|------|---------|--------|-------------|
| **Pivot** | ● | 1 | Command node; its immobilization ends the game. |
| **Axis** | ▲ | 2 | Line-control unit; defines geometric containment lines. |
| **Veil** | ◆ | 2 | Jump unit; establishes tempo and reach (two-step straight). |
| **Turned Veil** | ■ | 2 | Angular jump unit; shifts through adjacent directions to disrupt linear control. |

**Board:** Hexagonal grid of radius 4 (61 cells).  
Coordinates use axial notation `(q,r)` with six directions:  
`(+1,0) (+1,−1) (0,−1) (−1,0) (−1,+1) (0,+1)`.

---

## 3. Starting Layout

```

Player A (North)
Pivot ● at (0,+4)
Axis ▲ at (−1,+3), (1,+3)
Veil ◆ at (−1,+2), (1,+2)
Turned Veil ■ at (0,+3), (0,+2)

Player B (South)
Pivot ● at (0,−4)
Axis ▲ at (−1,−3), (1,−3)
Veil ◆ at (−1,−2), (1,−2)
Turned Veil ■ at (0,−3), (0,−2)

```

---

## 4. Turn Structure

Each turn has two phases:

1. **Primary Move** — perform one legal movement.  
2. **Future Order (optional)** — assign a deferred action to another unit.

A Future Order executes automatically at the start of that player’s next turn if the destination remains unoccupied.  
Only one order may exist per player at any time.

---

## 5. Movement Rules

### Pivot (●)
- Moves exactly one hex in any direction.  
- Cannot enter occupied hexes.

### Axis (▲)
- Slides any number of hexes in a straight line until blocked.  
- Cannot jump or end on an occupied hex.

### Veil (◆)
- Jumps exactly two hexes in any direction, ignoring the intervening one.  
- Must land on an empty hex within the board.

### Turned Veil (■)
- Jumps along **two adjacent directions**, forming a 60° turn.  
- Always lands on one of six mid-ring cells between the main axes.  
- Must land on an empty hex within the board.

---

## 6. Victory

| Outcome | Condition |
|----------|------------|
| **Win** | Opponent’s Pivot (●) immobilized. |
| **Draw** | Both Pivots immobilized simultaneously. |
| **Ongoing** | Neither condition met. |

---

## 7. Optional Variants

### Limited Orders
Future Orders may be issued only every two turns,  
emphasizing deliberate tempo management.

### Blind Deployment
Players alternate piece placement before the first move,  
creating asymmetric openings under perfect information.

---

## 8. Strategic Essence

| Element | Represents | Function |
|----------|-------------|-----------|
| **Axis (▲)** | Initiative | Defines containment geometry |
| **Pivot (●)** | Command | Balances centrality and defense |
| **Veil (◆)** | Tempo | Executes linear jumps for phase advantage |
| **Turned Veil (■)** | Adaptability | Breaks line stagnation through angular flanking |

The discipline lies in **temporal foresight** — knowing when to act, when to delay, and when to commit.

---

## 9. Credits

**Designer:** Andrew R. Garcia, Ph.D
Systems Engineer & Cognitive-AI Researcher  
Developed 2025  

© 2025 Andrew R. Garcia  
Licensed under **CC BY-NC-ND 4.0**  
[https://creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0/)

PLAYERS = ["A", "B"]
DIRECTIONS = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
]

def generate_hex_grid(radius=4):
    grid = []
    for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            if abs(q + r) <= radius:
                grid.append((q, r))
    return grid

def initial_pieces():
    return [
        # Player A
        {"id": "A_P", "type": "Pivot", "player": "A", "q": -2, "r": 4},
        {"id": "A_A1", "type": "Axis", "player": "A", "q": -4, "r": 3},
        {"id": "A_A2", "type": "Axis", "player": "A", "q": 1, "r": 3},
        {"id": "A_V1", "type": "Veil", "player": "A", "q": -1, "r": 4},
        {"id": "A_V2", "type": "Veil", "player": "A", "q": -3, "r": 4},
        {"id": "A_V90_1", "type": "Veil90", "player": "A", "q": 0, "r": 4},
        {"id": "A_V90_2", "type": "Veil90", "player": "A", "q": -4, "r": 4},

        # Player B
        {"id": "B_P", "type": "Pivot", "player": "B", "q": 2, "r": -4},
        {"id": "B_A1", "type": "Axis", "player": "B", "q": 4, "r": -3},
        {"id": "B_A2", "type": "Axis", "player": "B", "q": -1, "r": -3},
        {"id": "B_V1", "type": "Veil", "player": "B", "q": 1, "r": -4},
        {"id": "B_V2", "type": "Veil", "player": "B", "q": 3, "r": -4},
        {"id": "B_V90_1", "type": "Veil90", "player": "B", "q": 0, "r": -4},
        {"id": "B_V90_2", "type": "Veil90", "player": "B", "q": 4, "r": -4},
    ]

def add_hex(a, b): return (a[0] + b[0], a[1] + b[1])
def hex_eq(a, b): return a[0] == b[0] and a[1] == b[1]
def in_grid(h, grid): return any(hex_eq(h, g) for g in grid)

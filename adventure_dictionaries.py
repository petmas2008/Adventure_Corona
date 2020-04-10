from random import randint
movements = {
    "left": (-1, 0),
    "right": (+1, 0),
    "forward": (0, +1),
    "backwards": (0, -1)
    }

objects = {
    "car": (randint(0, 2), randint(0, 2)),
    "hat": (randint(0, 2), randint(0, 2)),
    "shotgun": (randint(0, 2), randint(0, 2)),
    "knife": (randint(0, 2), randint(0, 2)),
    "chair": (randint(0, 2), randint(0, 2)),
    "phone": (randint(0, 2), randint(0, 2)),
    "plant": (randint(0, 2), randint(0, 2)),
    "boots": (randint(0, 2), randint(0, 2))
    }

allowed_verbs = {
    "get": (objects, "You got the"),
    "go": (movements, "You went"),
    "drive": (objects, "You are driving the"),
    "drop": (objects, "You dropped")
    }

place = {
    (0, 0): "living room",
    (0, 1): "dining room",
    (-1, 0): "toilet",
    (1, 0): "bedroom",
    (0, -1): "hallway",
    (0, -2): "door",
    (1, 1): "kitchen",
    (0, 2): "garden"
    }
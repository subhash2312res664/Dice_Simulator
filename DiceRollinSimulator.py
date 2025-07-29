import random

# Dice faces using ASCII
dice_faces = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"

    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    ),
}

def roll_dice():
    roll = random.randint(1, 6)
    print(f"\n🎲 You rolled a {roll}!\n")
    for line in dice_faces[roll]:
        print(line)

# Main loop
while True:
    user_input = input("\nPress ENTER to roll the dice (or type E/Q to quit)...")
    if user_input.lower() == "e" or user_input.lower() == "q":
        print("Exiting... 🎲")
        break
    roll_dice()


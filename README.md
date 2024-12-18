# Battleship Game in Python (Terminal Version)

## Overview

This is a simple **Battleship** game created using Python, which is played directly in the terminal/command-line interface. The game allows two players (or a single player against the computer) to take turns guessing the location of ships on a grid, with the goal of sinking all the opponent's ships first.

## Features

- **2-player mode**: Play against a friend on the same computer.
- **Terminal-based**: Simple interface using the command line.
- **Ships**: The game features multiple ships of different sizes that must be located and sunk.
- **Grid-based**: The game is played on a grid where each player places their ships and attempts to guess the location of the opponent’s ships.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd battleship
   ```

## Run the game:

**To start the game, simply run the Python file in your terminal**:

```bash
python3 battleship.py

```

# How to Play

1. Place your ships:
   Each player places their ships on the grid. The grid is typically 10x10,
   and ships can be placed horizontally or vertically. The ships’ sizes vary,
   and you must position them strategically to avoid being hit.

2. Turn-based gameplay:
   Players take turns guessing where the opponent's ships are located by entering coordinates
   (e.g., A5 for row A, column 5).

3. Hit or Miss:
   After each guess, you will see whether the shot was a "hit" or "miss."
   The goal is to sink all of the opponent's ships.

4. Winning the Game:
   The first player to sink all of the opponent's ships wins the game.

# Game Controls

- Enter coordinates to make a guess (e.g., A1, B2, etc.).
- After each guess, the result (hit or miss) will be displayed,
  and the turn will switch to the other player.

Welcome to Battleship!

Player 1, it's your turn!
Enter coordinates to attack (e.g., A1):

> A1
> Result: Miss!

Player 2, it's your turn!
Enter coordinates to attack (e.g., B3):

> B3
> Result: Hit!

And so on...

### Support and Contact Details

For any questions or support regarding the Battleship game, feel free to reach out to us via our GitHub profiles:

1. Betty Jelagat: https://github.com/bettyje
2. Daniel Mburu: https://github.com/waweru89
3. Bravin Murambi: https://github.com/bravjr

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# Battleship Game in Python (Terminal Version)

## Overview

This is a simple **Battleship** game created using Python, which is played directly in the terminal/command-line interface. The game allows two players (or a single player against the computer) to take turns guessing the location of ships on a grid, with the goal of sinking all the opponent's ships first.

## Features

- **Computer VS Player mode**: Play against a friend on the same computer.
- **User-Friendly**: Input validation ensure the player enters valid input and prevents duplicate shots.
- **Difficulty Levels**: The program adapts the board size and number of ships to match the chosen difficulty.
- **Smart AI Opponent**: The computer uses intelligent targeting logic to provide a challenging experience.
- **Grid-based**: The game is played on a grid where each player places their ships and attempts to guess the location of the opponent’s ships.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd battleship
   pip install tabulate
   ```

## Run the game:

**To start the game, simply run the Python file in your terminal**:

```bash
python3 battleship.py

```

# How to Play Battleship
Battleship is a turn-based strategy game where you aim to sink your opponent's ships by guessing their locations on the board.

**Game Setup**
Choose a Difficulty Level:

-Easy: 5x5 grid with 1 ship.
-Medium: 8x8 grid with 2 ships.
-Hard: 10x10 grid with 4 ships.
-Select Players:

**Play against the Computer in single-player mode**.
Place Ships:

Ships are automatically placed for you and the computer. Ships vary in size:
Battleship: 5 tiles long.
Cruiser: 4 tiles long.
Destroyer: 3 tiles long.
Submarine: 2 tiles long.
Gameplay
Player’s Turn:

Input your target in the format ROW,COLUMN (e.g., A,1) to fire a shot.
The game will tell you if your shot is a hit or miss.
Sinking all parts of a ship removes it from the opponent’s fleet.
Computer’s Turn:

The computer fires back using a mix of random shots and smart targeting when it scores a hit.
**Visual Feedback**:

Your board shows your ships and the computer's hits.
The opponent's board (computer) reveals hits and misses but hides ship locations.
**Winning the Game**
The game ends when one player sinks all the opponent's ships. If your fleet is destroyed, the computer wins. If you sink all the computer’s ships, you win!
**Additional Features**
Smart AI: The computer uses a strategy to target adjacent cells after scoring a hit.
Grid Reference: Rows are labeled A, B, C, etc., and columns are numbered 1, 2, 3, etc.
Enjoy the game and may the best strategist win! 🎯



### Support and Contact Details

For any questions or support regarding the Battleship game, feel free to reach out to us via our GitHub profiles:

1. Betty Jelagat: https://github.com/bettyje
2. Daniel Mburu: https://github.com/waweru89
3. Bravin Murambi: https://github.com/bravjr

## License

This project is licensed under the MIT License - see the LICENSE file for details.

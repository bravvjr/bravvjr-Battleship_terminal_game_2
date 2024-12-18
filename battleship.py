import random
import os
from player import Player
from ship import Ship
from board import Board

#Stand ships available in the game
available_ships = [
    {"name": "Battleship", "length": 5},
    {"name": "Cruiser", "length": 4},
    {"name": "Destroyer", "length": 3},
    {"name": "Sub", "length": 2}
    ]

#This is the settings for difficulty levles in the form for [rows, columns, # of ships]
difficulties = {
    "easy" : [5, 5, 1],
    "medium" : [8, 8, 2],
    "hard" : [10, 10, 4]
}

def clear_screen():
    # Clearing the Screen
    # posix is os name for linux or mac
    if(os.name == 'posix'):
        os.system('clear')
        # else screen will be cleared for windows
    else:
        os.system('cls')
    print("WELCOME TO BATTLESHIP\n")

#This function will get the user inputed target and check it for validity.
def get_shot(player, rows, columns):
    shot = []
    target = input("\nInput your target in the format ROW,COLUMN. For example:\n\nA,1\n\nTarget: ")
    try:
        target = target.split(",")
        for coordinate in target:
            try:
                #Checks for integer
                shot.append(int(coordinate)-1)
            except:
                #Converts letter to integer
                shot.append(ord(coordinate)-65)
        
        #If the input is outside the range of the board
        if shot[0] >= rows or shot[1] >= columns:
            print("You need to enter coordinates that are on the board. Try again.")
            return False
        #If this target has already been tried
        if shot in player.shots_fired:
            print("You have already tried that coordinate. Try again!")
            return False
        #If the shot is valid and not a repeat, it returns
        else:
            player.shots_fired.append(shot)   
            return shot
    except:
        print("Please enter a valid coordinate.")
        return False

def get_players():
    #Get 1 or 2 player game
    players = []
    while True:
        num_players = input("You can play Battleship as a 1 player or 2 player game.\n\n1. 1 Player\n2. 2 Players\n\n")
        if num_players == "1":
            clear_screen()
            name = input("\nWhat is your name?\n\n")
            players.append(Player(name))
            break
        elif num_players == "2":
            clear_screen()
            name = input("\nWhat the name for player 1?\n\n")
            players.append(Player(name))
            clear_screen()
            name = input("\nWhat the name for player 2?\n\n")
            players.append(Player(name))
            break
        else:
            clear_screen()
            print("Please enter a valid option, 1 or 2")
    return players
    
    
def get_difficulty():
    #Choose difficulty
    difficulty = int(input("""Please choose difficulty:\n\n
        1. Easy
        2. Medium
        3. Hard\n\n"""))
    clear_screen()
    return difficulty

def one_player_game():
    clear_screen()
    turn = 0
    computer_shots = []  # Keep track of computer's shots
    last_hit = None      # Store the last successful hit
    direction_queue = [] # Queue to store adjacent cells for targeting

    # Function to get valid adjacent cells
    def get_adjacent_cells(hit):
        """Generate adjacent cells (up, down, left, right) around a hit."""
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        adjacent = []
        for dr, dc in directions:
            new_r, new_c = hit[0] + dr, hit[1] + dc
            if 0 <= new_r < players[1].board.rows and 0 <= new_c < players[1].board.columns:
                adjacent.append([new_r, new_c])
        return adjacent

    # Main game loop
    while players[0].ships_remaining > 0 and players[1].ships_remaining > 0:
        # Player's turn
        print("\nYour Board:")
        print(players[1].board.print_board(True))  # Player's board (show ships)
        
        print("\nComputer's Board:")
        print(players[0].board.print_board(False))  # Hide ships on computer's board
        
        print("\nYour Turn:")
        while True:
            shot = get_shot(players[0], players[0].board.rows, players[0].board.columns)
            if shot:
                break

        # Update computer's board with player's shot
        hit = players[0].board.update_board(shot)
        if hit == "hit":
            for ship in players[0].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk:
                        players[0].ships_remaining -= 1

        # Computer's turn
        input("\nPress Enter for the computer's turn...")
        clear_screen()
        print("\nComputer's Turn:")

        while True:
            # Smart targeting logic
            if last_hit and direction_queue:  # Continue targeting adjacent cells
                computer_shot = direction_queue.pop(0)
            elif last_hit:  # Generate new adjacent cells after a successful hit
                direction_queue = get_adjacent_cells(last_hit)
                direction_queue = [shot for shot in direction_queue if shot not in computer_shots]
                if direction_queue:
                    computer_shot = direction_queue.pop(0)
                else:
                    last_hit = None  # Reset if no valid adjacent cells
                    computer_shot = [random.randint(0, players[1].board.rows - 1),
                                     random.randint(0, players[1].board.columns - 1)]
            else:  # Random shot if no previous hits
                computer_shot = [random.randint(0, players[1].board.rows - 1),
                                 random.randint(0, players[1].board.columns - 1)]

            if computer_shot not in computer_shots:
                computer_shots.append(computer_shot)
                break

        print(f"Computer fired at {chr(computer_shot[0] + 65)},{computer_shot[1] + 1}")

        # Update player's board with computer's shot
        hit = players[1].board.update_board(computer_shot)
        if hit == "hit":
            last_hit = computer_shot  # Update the last successful hit
            for ship in players[1].ships:
                if computer_shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk:
                        players[1].ships_remaining -= 1
                        last_hit = None  # Reset targeting when a ship is sunk
                        direction_queue = []  # Clear the direction queue

        # Check if the computer won
        if players[1].ships_remaining == 0:
            clear_screen()
            print("Game Over! The computer sank all your ships!")
            break

        turn += 1
        clear_screen()


def two_player_game():
    clear_screen()
    turn = 0
    attacker = 0
    defender = 0
    while players[defender].ships_remaining > 0:
        attacker = turn % 2
        if attacker == 0:
            defender = 1
        else:
            defender = 0
        
        print("Player {player}'s turn".format(player = players[attacker].name))
        print("\n{player}'s Board".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\n{player}'s Board".format(player = players[defender].name))
        print(players[defender].board.print_board(False))
    
        while True:
            shot = get_shot(players[attacker],players[defender].board.rows, players[defender].board.columns)
            if shot != False:
                break
        clear_screen()
        print("Player {player}'s turn".format(player = players[attacker].name))
        print("\n{player}'s Board".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\n{player}'s Board\n".format(player = players[defender].name))        
        hit = players[defender].board.update_board(shot)
        if hit == "hit":
            for ship in players[defender].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk == True:
                        players[defender].ships_remaining -= 1
        input("\nHit Enter then pass the computer to your partner")
        clear_screen()
        input("Hit Enter when you're ready")
        clear_screen()
        turn += 1
    finish = input("Game Over! Press Enter to exit game")
    clear_screen()

# Initiate the Game
clear_screen()

players = get_players()  # Get player(s)
if len(players) == 1:
    # Add computer player for one-player mode
    players.insert(0, Player("Computer"))  # Add computer as the first player
    

# Choose difficulty
while True:
    difficulty = get_difficulty()
    if difficulty in [1, 2, 3]:
        break
    print("Invalid input\n")    

# Create boards and place ships for both the player and the computer
for player in players:
    if difficulty == 1:
        player.get_board(difficulties["easy"][:2])
        player.get_ships(difficulties["easy"][2], available_ships)
    elif difficulty == 2:
        player.get_board(difficulties["medium"][:2])
        player.get_ships(difficulties["medium"][2], available_ships)
    elif difficulty == 3:
        player.get_board(difficulties["hard"][:2])
        player.get_ships(difficulties["hard"][2], available_ships)    

# Place ships on the boards
for player in players:
    player.place_ships()

one_player_game()    
#count players
if len(players) == 1:
    one_player_game()
else:
    two_player_game()
     
      
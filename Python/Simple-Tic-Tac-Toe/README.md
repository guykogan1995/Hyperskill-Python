# Tic-Tac-Toe Game Readme

## Description

This Python script allows you to play a game of Tic-Tac-Toe. The script creates a 3x3 game board and prompts two players to take turns making moves. The game will continue until one of the players wins, or the game ends in a draw. The script checks for valid moves, handles occupied cells, and determines the game's outcome.

Key features of the game:

- Interactive board: The script provides a visual representation of the game board, so you can see the current state of the game.

- Valid moves: The script ensures that players can only make valid moves within the 3x3 grid.

- Occupied cells: Players are prevented from making moves in cells that are already occupied.

- Game outcome: The script checks for a win by either player, a draw, or an ongoing game.

- Turn-based gameplay: The game alternates between two players, allowing them to take turns.

## Usage

To play the Tic-Tac-Toe game, follow these steps:

1. Copy and paste the script into your Python environment.

2. Execute the script.

3. The script will display an empty game board:

```
---------
|       |
|       |
|       |
---------
```

4. Follow the script's prompts to enter your moves. You will be asked to input coordinates in the format `x y`, where `x` is the row and `y` is the column (both ranging from 1 to 3).

5. The game will continue until one player wins, or it ends in a draw. The script will announce the outcome and ask if you want to play again.

6. Enjoy playing Tic-Tac-Toe with a friend!

## Example

Here's an example of playing the Tic-Tac-Toe game:

```
---------
|       |
|       |
|       |
---------

Player X's turn. Enter the coordinates (row and column): 2 2
---------
|       |
|   X   |
|       |
---------

Player O's turn. Enter the coordinates (row and column): 1 1
---------
| O     |
|   X   |
|       |
---------

Player X's turn. Enter the coordinates (row and column): 2 1
---------
| O     |
|   X   |
| X     |
---------

Player O's turn. Enter the coordinates (row and column): 1 2
---------
| O O   |
|   X   |
| X     |
---------

Player X's turn. Enter the coordinates (row and column): 3 1
---------
| O O   |
|   X   |
| X X   |
---------

Player O's turn. Enter the coordinates (row and column): 3 3
---------
| O O   |
|   X   |
| X X O |
---------

Player X's turn. Enter the coordinates (row and column): 1 3
---------
| O O X |
|   X   |
| X X O |
---------

Player X wins!

Do you want to play again? (yes/no): no
```

In this example, two players took turns making moves, and Player X won the game. The players were given the option to play again.

## License

This script is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it as needed.

Enjoy playing Tic-Tac-Toe with your friends and have fun!
# Text-Based Survival Game

## Introduction
Welcome to the Text-Based Survival Game, a simple yet engaging command-line game where you, as a commander, must explore various locations, manage robots, upgrade your capabilities, and survive in a challenging environment. This game is designed to test your strategic thinking and decision-making skills.

## Getting Started
To start playing the game, follow these steps:

1. **Requirements:**
   - This game is written in Python, so you need to have Python installed on your computer.
   - Clone or download the game files to your computer.

2. **Running the Game:**
   - Open your terminal or command prompt.
   - Navigate to the game directory where the Python script is located.
   - Run the game using the following command:
     ```
     python game.py
     ```

3. **Gameplay:**
   - Follow the on-screen instructions to navigate the game menu and make choices.
   - Explore different locations, manage robots, upgrade your capabilities, and make strategic decisions to survive and collect resources.

## Gameplay
The gameplay consists of the following main features:

- **Exploration:** Explore different locations, collect resources, and face encounters.
- **Robot Management:** Manage your robots, which are your key assets in the game.
- **Upgrades:** Purchase upgrades to enhance your capabilities.
- **Saving Progress:** Save your game progress to continue later.

## Commands
The game uses simple commands to interact with the menu and gameplay. Here are the basic commands:

- `new`: Start a new game.
- `exit`: Exit the game.
- `high`: View the high scores.
- `load`: Load a saved game.
- `up`: Upgrade your capabilities.
- `save`: Save your game progress.

## High Scores
Compete with other players to achieve the highest score and make it to the high scores list.

## Upgrades
You can spend your resources to purchase upgrades that will help you survive longer and collect more resources.

## Saving and Loading
You can save your game progress and load it later to continue from where you left off.

## Example Output
Here's an example of what the game's output might look like as a player interacts with it:
+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+

[New]  Game
[Load] Game
[High] Scores
[Help]
[Exit]

Your command: new

Enter Your name:
Player1

Greetings, commander Player1!
Are you ready to begin?
  [Yes] [No] Return to Main Menu

Your command: yes

+==============================================================================+
  $   $$$$$$$   $  |
  $$$$$     $$$$$  |
      $$$$$$$      |
     $$$   $$$     |
     $       $     |
+==============================================================================+
| Titanium: 0                                                                  |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+

Your command: explore

Searching
[1] High Street: 50
[2] Green Park: 75
[3] Destroyed Arch: 60
[4] Lower Depths: 30
[5] Out World: 70
[6] Destroyed Planes: 40
[7] Murky Waters: 20
[8] Hell Land: 10
[9] Space Water: 90

[S] to continue searching

Your command: 3

Deploying robots
Enemy encounter
Destroyed Arch was explored successfully, 1 robot lost...
Acquired 60 lumps of titanium
+==============================================================================+
  $   $$$$$$$   $  |
  $$$$$     $$$$$  |
      $$$$$$$      |
     $$$   $$$     |
     $       $     |
+==============================================================================+
| Titanium: 60                                                                 |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+

Your command: explore

Searching
[1] High Street: 80
[2] Green Park: 40
[3] Destroyed Arch: 20
[4] Lower Depths: 70
[5] Out World: 10
[6] Destroyed Planes: 90
[7] Murky Waters: 50
[8] Hell Land: 45
[9] Space Water: 65

[S] to continue searching

Your command: s

Nothing more in sight.
  [Back]

Your command: back

+==============================================================================+
  $   $$$$$$$   $  |
  $$$$$     $$$$$  |
      $$$$$$$      |
     $$$   $$$     |
     $       $     |
+==============================================================================+
| Titanium: 60                                                                 |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+

Your command: upgrade

|================================|
|          UPGRADE STORE         |
|                         Price  |
| [1] Titanium Scan         250  |
| [2] Enemy Encounter Scan  500  |
| [3] New Robot            1000  |
|                                |
| [Back]                         |
|================================|

Your command: 2

Purchase successful. You will now see how likely you will encounter an enemy at each found location.
+==============================================================================+
  $   $$$$$$$   $  |
  $$$$$     $$$$$  |
      $$$$$$$      |
     $$$   $$$     |
     $       $     |
+==============================================================================+
| Titanium: 60                                                                 |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+

Your command: save

   Select save slot:
    [1] Player1 Titanium: 60 Robots: 3 Last save: 2023-10-30 15:45 Titanium Upgrade: True Encounter Upgrade: False
    [2] empty 0
    [3] empty 0

Your command: 1

                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|


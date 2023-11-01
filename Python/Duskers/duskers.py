import os
import random
import re
import sys
from datetime import datetime

regular_menu = """                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|"""
intro_menu = """+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+"""
arg_length = len(sys.argv)
locations_string = "High_street,Green_park,Destroyed_Arch,Lower_Depths,Out_World,Destroyed_Planes," \
                   "Murky_Waters,Hell_Land,Space_Water"
seed_num, animations_count_min, animations_count_max, locations = "0", "0", "0", locations_string.replace("_", " ")
if arg_length == 5:
    seed_num, animations_count_min, animations_count_max, locations = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[
        4].replace("_", ' ')
if arg_length != 1 and arg_length != 5:
    raise Exception("Arguments can either be 0 or must be 4")
random.seed(seed_num)
name, last_val, robot_lives, lines, show_titanium, show_encounter, new_robot, names = ("", 0, 3, ["empty"] * 3,
                                                                                       False, False, False, [])
if not os.path.isfile("save_file"):
    with open("save_file", "w") as f:
        f.write("\n".join(lines))
if not os.path.isfile("high_scores"):
    with open("high_scores", "w") as f:
        start_scores = ["empty 0"] * 10
        f.write("\n".join(start_scores))


def save_for_high_score():
    high_scores_str = ""
    with open("high_scores", "r") as file:
        score_lines = file.readlines()
        score_names = [i.split()[0] for i in score_lines]
        score_lines = [int(i.split()[1]) for i in score_lines]
        high_scores = [(player_name, score) for (player_name, score) in zip(score_names, score_lines)]
    if "empty" in score_names and 0 in score_lines:
        for num, item in enumerate(high_scores):
            if item[1] == 0 and item[0] == "empty":
                high_scores[num] = name, last_val
                high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)
                high_scores_str = [i[0] + " " + str(i[1]) for i in high_scores]
                break
        with open("high_scores", "w") as file:
            file.write("\n".join(high_scores_str))
    else:
        min_score = min([i[1] for i in high_scores])
        if last_val >= min_score:
            for num, item in enumerate(high_scores):
                if item[1] <= last_val:
                    old_list = high_scores
                    if len(high_scores) is 10:
                        high_scores = high_scores[:num] + [(name, last_val)] + high_scores[num:len(high_scores)-1]
                    break
            high_scores_str = [i[0] + " " + str(i[1]) for i in high_scores]
            with open("high_scores", "w") as file2:
                file2.write("\n".join(high_scores_str))


def helper_function(places, titanium, generator_places, ret_string, count, encounters):
    print("Searching")
    place_name = random.choice(places)
    titanium_yield = random.randint(10, 100)
    titanium.append(titanium_yield)
    generator_places.append(place_name)
    encounter_rate = random.random()
    encounters.append(encounter_rate)
    percentage_defeat = int(round(encounter_rate * 100))
    if show_encounter & show_titanium:
        ret_string.append(
            "[" + str(count) + "] " + place_name + ": " + str(titanium_yield) + " Encounter rate: "
            + str(percentage_defeat) + "%")
    elif show_titanium:
        ret_string.append("[" + str(count) + "] " + place_name + ": " + str(titanium_yield))
    elif show_encounter:
        ret_string.append(
            "[" + str(count) + "] " + place_name + ": " + "Encounter rate: " + str(percentage_defeat)
            + "%")
    else:
        ret_string.append("[" + str(count) + "] " + place_name)


def save_to_file(command4):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    with open("save_file", "r") as file:
        temp = file.readlines()
    with open("save_file", "w") as file:
        temp[int(command4) - 1] = name + " Titanium: " + str(last_val) + " Robots: " + str(robot_lives) \
                                  + " Last save: " + str(time) + " Titanium Upgrade: " + str(show_titanium) \
                                  + " Encounter Upgrade: " + str(show_encounter)
        temp = [i.replace("\n", "") for i in temp]
        file.write("\n".join(temp))


def gameLogic():
    global name, last_val, robot_lives, show_encounter, show_titanium
    print(intro_menu)
    print("""\n[New]  Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]\n""")
    print("Your command:")
    menu_commands = ["new", "exit", "help", "high", "back", "load"]
    command = input().lower()
    while command != "new":
        if command not in menu_commands:
            print("Invalid input\n")
            print("Your command:")
            command = input().lower()
        elif command == "exit":
            print("\nThanks for playing, bye!")
            exit(0)
        elif command == "high":
            print("\n\tHIGH SCORES\n")
            with open("high_scores", "r") as file:
                scores = file.readlines()
            new_scores = ["(" + str(count + 1) + ") " + i for count, i in enumerate(scores) if "empty" not in i]
            if len(new_scores) != 0:
                print("".join(new_scores))
            print("\n\t[Back]\n")
            print("Your command:")
            command = input().lower()
        elif command == "load":
            run_loop = True
            while run_loop:
                with open("save_file", "r") as file:
                    temp = file.readlines()
                new_temp = [i.replace("\n", "") for i in temp]
                print(f"""   Select save slot:
        [1] {new_temp[0]}
        [2] {new_temp[1]}
        [3] {new_temp[2]}\n""")
                print("your command:")
                command5 = input()
                while command5 not in ["1", "2", "3", "back"]:
                    print("Invalid input")
                    print("\nYour command:")
                    command5 = input().lower()
                if command5 == "back":
                    print()
                    gameLogic()
                    robo_gameLogic()
                    exit(0)
                if temp[int(command5) - 1].replace("\n", "") == "empty":
                    print("Empty slot!\n")
                    continue
                print(f"""                          |==============================|
                            |    GAME LOADED SUCCESSFULLY  |
                            |==============================|
     Welcome back, commander {temp[int(command5) - 1].split(" ")[0]}!""")

                last_val = int(temp[int(command5) - 1].split(" ")[2])
                name = temp[int(command5) - 1].split(" ")[0]
                robot_lives = int(temp[int(command5) - 1].split(" ")[4])
                if new_temp[int(command5) - 1].split(" ")[11] == "False":
                    show_titanium = False
                else:
                    show_titanium = True
                if new_temp[int(command5) - 1].split(" ")[14] == "False":
                    show_encounter = False
                else:
                    show_encounter = True
                robo_gameLogic()
                exit(0)
        elif command == "back":
            print("\n" + intro_menu)
            print("""\n[New]  Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]\n""")
            print("Your command:")
            command = input().lower()
    print("\nEnter Your name:")
    name = input()
    print(f"\nGreetings, commander {name}!\n"
          f"Are you ready to being?\n"
          f"\t[Yes] [No] Return to Main[Menu]\n")
    print("Your command:")
    command2 = input().lower()
    while command2 != "yes":
        if command2 == "no":
            print("\nHow about now.\nAre you ready to being?\n"
                  "\t[Yes] [No] Return to Main[Menu]\n")
            print("Your command:")
            command2 = input().lower()
        elif command2 == "menu":
            print("""\n+=======================================================================+
  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                      (Survival ASCII Strategy Game)
+=======================================================================+""")
            print("""\n[New]  Game\n[Load] Game\n[High] Scores\n[Help]\n[Exit]\n""")
            print("Your command:")
            command2 = input().lower()
            if command2 == "new":
                break
        else:
            print("Invalid input")
            print("\nYour command:")
            command2 = input().lower()


def save_function():
    with open("save_file", "r") as file:
        temp = file.readlines()
    temp = [i.replace("\n", "") for i in temp]
    print(f"""   Select save slot:
    [1] {temp[0]}
    [2] {temp[1]}
    [3] {temp[2]}\n""")
    print("Your command:")
    command4 = input().lower()
    while command4 not in ["1", "2", "3", "back"]:
        print("Invalid input")
        print("\nYour command:")
        command4 = input().lower()
    if command4 == "back":
        print()
        gameLogic()
        robo_gameLogic()
        exit(0)
    save_to_file(command4)
    print("""                        |==============================|
                        |    GAME SAVED SUCCESSFULLY   |
                        |==============================|""")


def robo_gameLogic():
    global show_titanium, show_encounter, robot_lives, last_val
    robot = ["  $   $$$$$$$   $  |", "  $$$$$     $$$$$  |", "      $$$$$$$      |", "     $$$   $$$     |",
             "     $       $     |"]
    robot = "\n".join([(i * robot_lives)[:len(i * robot_lives) - 1] for i in robot])

    new_menu = f"""+==============================================================================+
{robot}
+==============================================================================+
| Titanium: {last_val}                                                                  |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+
"""
    print(new_menu)
    print("Your command:")
    command = input().lower()
    robo_commands = ["ex", "up", "m", "save"]
    while command not in robo_commands:
        print("Invalid input")
        print("\nYour command:")
        command = input().lower()
    if command == "m":
        print(regular_menu)
        print("\nYour command:")
        command = input().lower()
        if command == "save":
            save_function()
            exit(0)
        elif command == "exit":
            print("\nThanks for exiting!")
            exit(0)
        elif command == "main":
            gameLogic()
            robo_gameLogic()
        elif command == "back":
            robo_gameLogic()
    elif command == "save":
        save_function()
        robo_gameLogic()
    elif command == "ex":
        num_locations = random.randint(1, 9)
        count, titanium, places, generator_places, ret_string, encounters = 1, [], (locations.split(",")), [], [], []
        helper_function(places, titanium, generator_places, ret_string, count, encounters)
        print("\n".join(ret_string))
        print("\n[S] to continue searching\n")
        print("Your command:")
        command3 = input().lower()
        while command3 != "":
            if command3 == "back":
                robo_gameLogic()
            while command3 != "s" and (command3.isdigit() is not True or (0 > int(command3) or int(command3) > count)):
                print("\nInvalid input")
                print("Your command:")
                command3 = input().lower()
            if command3 != "s":
                encounter_rate_two = random.random()
                if encounters[int(command3) - 1] > encounter_rate_two:
                    print(f"Deploying robots\nEnemy encounter\nHigh street was explored successfully, "
                          f"1 robot lost..\nAcquired {titanium[int(command3) - 1]} lumps of titanium")
                    robot_lives -= 1
                    if robot_lives == 0:
                        save_for_high_score()
                        print("Game Over")
                        robot_lives = 3
                        last_val = 0
                        gameLogic()
                        robo_gameLogic()
                        exit(0)
                    last_val += titanium[int(command3) - 1]
                else:
                    print(f"Deploying robots\nHigh street was explored successfully, "
                          f"with no damage taken.\nAcquired {titanium[int(command3) - 1]} lumps of titanium")
                    last_val += titanium[int(command3) - 1]
                robo_gameLogic()
                exit(0)
            if count < num_locations:
                count += 1
                helper_function(places, titanium, generator_places, ret_string, count, encounters)
                print("\n".join(ret_string))
                print("\n[S] to continue searching\n")
                print("Your command:")
                command3 = input().lower()
                while command3 != "s" and (0 > int(command3) or int(command3) > count):
                    print("\nInvalid input")
                    print("Your command:")
                    command3 = input().lower()
            else:
                print("\nNothing more in sight.\n\t[Back]\n")
                print("Your command:")
                command3 = input().lower()
    elif command == "up":
        print("""                       |================================|
                       |          UPGRADE STORE         |
                       |                         Price  |
                       | [1] Titanium Scan         250  |
                       | [2] Enemy Encounter Scan  500  |
                       | [3] New Robot            1000  |
                       |                                |
                       | [Back]                         |
                       |================================|
\n""")
        print("Your command: ")
        command6 = input().lower()
        while command6 not in ["1", "2", "3", "back"]:
            print("\nInvalid input")
            print("Your command:")
            command6 = input().lower()
        while command6 != "back":
            if command6 == "1":
                if last_val >= 250:
                    show_titanium = True
                    last_val -= 250
                    print("Purchase successful. You can now see how much titanium\
you can get from each found location.")
                else:
                    print("Purchase unsuccessful. You can try again when you have enough titanium.")
                robo_gameLogic()
                exit(0)
            elif command6 == "2":
                if last_val >= 500:
                    last_val -= 500
                    show_encounter = True
                    print("Purchase successful. You will now see how likely \
you will encounter an enemy at each found location.")
                else:
                    print("Purchase unsuccessful. You can try again when you have enough titanium.")
                    print("Your command:")
                    command6 = input().lower()
                robo_gameLogic()
                exit(0)
            elif command6 == "3":
                if last_val >= 1000:
                    print("Purchase successful. You now have an additional robot")
                    last_val -= 1000
                    robot_lives += 1
                else:
                    print("Purchase unsuccessful. You can try again when you have enough titanium.\n")
                    print("Your command:")
                    command6 = input().lower()
                robo_gameLogic()
                exit(0)
        robo_gameLogic()


gameLogic()
robo_gameLogic()

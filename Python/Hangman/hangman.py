import random

correct_answer_list = ['python', 'java', 'swift', 'javascript']
print("H A N G M A N\n")
print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
game_choice = input()
wins = 0
losses = 0
while game_choice != "exit":
    if game_choice == "results":
        print("You won: " + str(wins) + " times")
        print("You lost: " + str(losses) + " times")
        print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
        game_choice = input()
    elif game_choice == "exit":
        print("")
        break
    elif game_choice == "play":
        num = 8
        word = random.choice(correct_answer_list)
        final_word = ("-" * len(word))
        print(final_word)
        choices = set()
        while num > 0:
            print(final_word)
            print("Input a letter: ")
            guess = input()
            indexes = []
            old_length = len(choices)
            choices.add(guess)
            new_length = len(choices)
            if len(guess) > 1 or len(guess) == 0:
                print("Please, input a single letter.")
            elif "A" <= guess <= "Z" or guess < "A":
                print("Please, enter a lowercase letter from the English alphabet.")
            elif old_length == new_length:
                print("You've already guessed this letter.")
            else:
                for j in range(len(word)):
                    if word[j] == guess:
                        indexes.append(j)
                if guess in word:
                    for index in indexes:
                        final_word = final_word[0:index] + str(guess) + final_word[index+1:len(final_word)]
                        word = word[0:index] + "*" + word[index + 1:len(word)]
                else:
                    print("That letter doesn't appear in the word.")
                    num -= 1
                if "-" not in final_word:
                    break
            print("")
        if "-" in final_word:
            print("You Lost!")
            losses += 1
            print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
            game_choice = input()
        else:
            print("You guessed the word " + final_word + "!\n" + "You survived!")
            wins += 1
            print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
            game_choice = input()
        print("")
    else:
        print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")

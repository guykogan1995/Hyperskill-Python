# Mini Calculator Game

This is a simple text-based Mini Calculator Game in Python. The game offers two levels: one for performing simple operations with numbers between 2 and 9, and the other for finding the integral squares of numbers between 11 and 29. You will be given 5 questions, and you need to provide the correct answers. At the end of the game, you can choose to save your results in a file named "results.txt".

## How to Play

1. Run the script in your Python environment.
2. You will be prompted to choose a game level by entering a number:
    - Level 1: Simple operations with numbers 2-9
    - Level 2: Integral squares of 11-29
3. You will be presented with 5 questions, one at a time.
4. Enter your answer for each question.
5. After each question, you will be informed if your answer is correct or not.
6. At the end of the game, you will be shown your score out of 5.
7. You can choose to save your results in "results.txt" by entering "yes" or "no".

## Example Output

Here's an example of what the game's output might look like:

```
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
1
5 + 3
8
Right!
7 * 8
56
Right!
4 + 9
13
Right!
2 - integral squares of 11-29
17
Wrong!
9 + 5
14
Right!
Your mark is 4/5. Would you like to save the result? Enter yes or no.
yes
What is your name?
John
The results are saved in "results.txt"
```

## Results File

If you choose to save the results, they will be stored in a file named "results.txt" with the following format:

```
John: 4/5 in level 1 - simple operations with numbers 2-9
```

This line indicates that the player named "John" scored 4 out of 5 in level 1.

Have fun playing the Mini Calculator Game!
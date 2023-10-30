# Flash Cards Program

This is a Python program that allows you to create and manage flashcards. You can add cards, remove cards, export them to a file, import cards from a file, test your knowledge by asking for definitions, view the hardest cards, reset card statistics, and save a log of your interactions.

Here's how to use the program:

1. Run the script in your Python environment.
2. You will be prompted to enter various commands to manage your flashcards.
3. You can perform actions like adding cards, removing cards, exporting and importing cards, testing your knowledge, and more.

## Example Output

Here's an example of what the program's output might look like:

```
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
add
The card:
Python
The definition of the Card:
A high-level programming language.
The pair "Python":"A high-level programming language." has been added.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
ask
How many times to ask?
3
Print the definition of "Python":
A programming language.
Wrong. The right answer is "A high-level programming language."
Print the definition of "Python":
A high-level programming language.
Correct!
Print the definition of "Python":
A programming language.
Wrong. The right answer is "A high-level programming language."

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
hardest card
The hardest card is "Python". You have 2 errors answering it.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
export
File name:
flashcards.json
3 cards have been saved

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
log
File name:
log.txt
The log has been saved.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
exit
Bye bye!
```

In this example, cards were added, tested, the hardest card was found, cards were exported to a JSON file, and a log was saved. Finally, the program was exited.

Enjoy managing your flashcards with this program!
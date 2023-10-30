import json
import os
from io import StringIO
import argparse

command = ""


class FlashCards:
    def __init__(self):
        self.cards = {}
        self.memory_file = StringIO()

    def add_card(self, term_to_add, definition_to_add):
        self.cards[term_to_add] = [definition_to_add, 0]

    def remove_card(self, term_to_remove):
        if term_to_remove in self.cards:
            self.cards.pop(term_to_remove)
            print("The card has been removed.\n")
            self.memory_file.write("The card has been removed.\n\n")
        else:
            print(f"Can't remove \"{term_to_remove}\": there is no such card.")
            self.memory_file.write(f"Can't remove \"{term_to_remove}\": there is no such card.\n")

    def export_to_file(self, file_name=""):
        if file_name == "":
            name_of_file = input("File name:\n")
            self.memory_file.write("File name:\n" + name_of_file)
        else:
            name_of_file = file_name
        with open(name_of_file, "w") as file2:
            json.dump(self.cards, file2, indent=4)
        print(f"{len(self.cards)} cards have been saved")
        self.memory_file.write(f"{len(self.cards)} cards have been saved\n")

    def import_from_file(self, file_name=""):
        if file_name == "":
            name_of_file = input("File name:\n")
            self.memory_file.write("File name:\n" + name_of_file + "\n")
        else:
            name_of_file = file_name
        if os.path.exists(name_of_file):
            with open(name_of_file, "r") as file:
                new_cards = json.load(file)
            self.cards.update(new_cards)
            print(f"{len(new_cards)} cards have been loaded.\n")
            self.memory_file.write(f"{len(new_cards)} cards have been loaded.\n\n")
        else:
            print("File not found.\n")
            self.memory_file.write("File not found.\n\n")

    def ask(self, definitions):
        num_times = int(input("How many times to ask?\n"))
        self.memory_file.write("How many times to ask?\n" + str(num_times) + "\n")
        terms = list(self.cards.keys())
        count, index = 0, 0
        while count < num_times:
            if index == len(terms):
                index = 0
            print(f"Print the definition of \"{terms[index]}\":")
            self.memory_file.write(f"Print the definition of \"{terms[index]}\":" + "\n")
            answer = input()
            if answer == definitions[index]:
                print("Correct!")
                self.memory_file.write("Correct!\n")
            elif answer in definitions:
                for j in range(len(definitions)):
                    if definitions[j] == answer:
                        value_list = self.cards[terms[index]]
                        value_list[1] += 1
                        print(
                            f"Wrong. The right answer is \"{definitions[index]}\", but your definition "
                            f"is correct for \"{terms[j]}\"")
                        self.memory_file.write(f"Wrong. The right answer is \"{definitions[index]}\""
                                               f", but your definition is correct for \"{terms[j]}\"\n")
                        break
            else:
                value_list = self.cards[terms[index]]
                value_list[1] += 1
                print(f"Wrong. The right answer is \"{definitions[index]}\"")
                self.memory_file.write(f"Wrong. The right answer is \"{definitions[index]}\"\n")
            count += 1
            index += 1
        print()
        self.memory_file.write("\n")

    def run_cards(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--import_from", dest="import_file_name", action="store")
        parser.add_argument("--export_to", dest="export_file_name", action="store")
        args = parser.parse_args()
        if args.__dict__["import_file_name"] is not None:
            self.import_from_file(args.__dict__["import_file_name"])
        global command
        while command != "exit":
            print("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            self.memory_file.write("Input the action (add, remove, import, export, ask, exit, log, hardest card, "
                                   "reset stats):\n")
            command = input().lower()
            self.memory_file.write(command + "\n")
            definitions = [i[0] for i in self.cards.values()]
            if command == "add":
                term = input("The card:\n")
                self.memory_file.write("The card:\n" + term + "\n")
                while term in self.cards:
                    old_term = term
                    term = input(f"The card \"{term}\" already exists. Try again:\n")
                    self.memory_file.write(f"The card \"{old_term}\" already exists. Try again:\n")
                definition = input("The definition of the Card:\n")
                self.memory_file.write("The definition of the Card:\n" + definition + "\n")
                while definition in definitions:
                    old_definition = definition
                    definition = input(f"The definition \"{definition}\" already exists. Try again:\n")
                    self.memory_file.write("\n" + f"The definition \"{old_definition}\" already exists. Try again:\n"
                                           + definition)
                self.add_card(term, definition)
                print(f"The pair \"{term}\":\"{definition}\" has been added.\n")
                self.memory_file.write(f"The pair \"{term}\":\"{definition}\" has been added.\n\n")
            elif command == "remove":
                key_to_remove = input("Which card?\n")
                self.memory_file.write("Which card?\n" + key_to_remove + "\n")
                self.remove_card(key_to_remove)
            elif command == "export":
                self.export_to_file()
            elif command == "import":
                self.import_from_file()
            elif command == "ask":
                self.ask(definitions)
            elif command == "hardest card":
                hardest_cards = []
                if len(self.cards) != 0:
                    max_diff = max([i[1] for i in self.cards.values()])
                    for term, value in self.cards.items():
                        if value[1] == max_diff and max_diff != 0:
                            hardest_cards.append(term)
                    if len(hardest_cards) == 1:
                        print(f"The hardest card is \"{hardest_cards[0]}\". you have {max_diff} errors answering it.\n")
                        self.memory_file.write(f"The hardest card is \"{hardest_cards[0]}\". you have {max_diff}"
                                               f" errors answering it.\n\n")
                    elif len(hardest_cards) > 1:
                        hardest_cards_str = "\", \"".join(hardest_cards)
                        print(f"The hardest cards are \"{hardest_cards_str}\". you have {max_diff}"
                              f" errors answering them.\n")
                        self.memory_file.write(f"The hardest cards are \"{hardest_cards_str}\". you have {max_diff}"
                                               f" errors answering them.\n\n")
                    else:
                        print("There are no cards with errors.\n")
                        self.memory_file.write("There are no cards with errors.\n\n")
                else:
                    print("There are no cards with errors.\n")
                    self.memory_file.write("There are no cards with errors.\n\n")
            elif command == "reset stats":
                for card in self.cards:
                    value = self.cards[card]
                    value[1] = 0
                    self.cards[card] = value
                print("Card statistics have been reset.\n")
                self.memory_file.write("Card statistics have been reset.\n\n")
            elif command == "log":
                file_name = input("File name:\n")
                self.memory_file.write(f"File name:\n" + file_name + "\n")
                with open(file_name, "w") as f:
                    f.write(self.memory_file.getvalue())
                print("The log has been saved.\n")
            elif command == "exit":
                print("Bye bye!")
                if args.__dict__["export_file_name"] is not None:
                    self.export_to_file(args.__dict__["export_file_name"])


if __name__ == "__main__":
    new_game = FlashCards()
    new_game.run_cards()

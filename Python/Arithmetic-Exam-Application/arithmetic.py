import os.path
import random


class MiniCalculator:

    def __str__(self):
        return str(self.nums[0]) + " " + self.operator + " " + str(self.nums[1])

    def __init__(self):
        self.operator = random.choice(["+", "-", "*"])
        self.nums = [random.randint(2, 9), random.randint(2, 9)]
        self.answer = self.calculate()

    def calculate(self):
        if self.operator == "-":
            return self.nums[0] - self.nums[1]
        elif self.operator == "+":
            return self.nums[0] + self.nums[1]
        elif self.operator == "*":
            return self.nums[0] * self.nums[1]
        elif self.operator == "/":
            return self.nums[0] / self.nums[1]


class MiniCalculatorSquares(MiniCalculator):

    def __str__(self):
        return str(self.num)

    def __init__(self):
        self.num = random.randint(11, 29)
        self.answer = self.calculate()
        super().__init__()

    def calculate(self):
        return self.num ** 2


def Main():
    str_list = ["1 - simple operations with numbers 2-9", "2 - integral squares of 11-29"]
    print(f"""Which level do you want? Enter a number:
    {str_list[0]}
    {str_list[1]}""")
    level = None
    while level is None or level not in [1, 2]:
        try:
            level = int(input())
        except ValueError or level not in [1, 2]:
            print("Incorrect format.")
            print("""Which level do you want? Enter a number:
            1 - simple operations with numbers 2-9
            2 - integral squares of 11-29""")
    answers = 0
    for i in range(5):
        if level == 1:
            calc = MiniCalculator()
            print(calc)
        else:
            calc = MiniCalculatorSquares()
            print(calc)
        answer = None
        while answer is None:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
        if answer == calc.answer:
            answers += 1
            print("Right!")
        else:
            print("Wrong!")
    saved = input(f"Your mark is {answers}/5. Would you like to save the result? Enter yes or no.\n")
    if saved.lower() in ["yes", "y"]:
        name = input("What is your name?\n")
        if level == 1:
            ret_str = str_list[0]
        else:
            ret_str = str_list[1]
        if os.path.exists("results.txt"):
            with open("results.txt", "a") as f:
                f.write(f"{name}: {answers}/5 in level {level} + {ret_str}\n")
        else:
            with open("results.txt", "w") as f:
                f.write(f"{name}: {answers}/5 in level {level} + {ret_str}\n")
        print("The results are saved in \"results.txt\"")
    else:
        exit(0)


if __name__ == "__main__":
    Main()

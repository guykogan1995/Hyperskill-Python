import string

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
operations = ["+", "-", "*", "/"]
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def check_float(string_1):
    try:
        float(string_1)
        return True
    except ValueError:
        return False


def is_one_digit(v):
    if v.isnumeric() and -10 < int(v) < 10:
        return True
    else:
        return False


def check_func(a, b, oper):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg += msg_6
    a, b = float(a), float(b)
    if (a == 1.0 or b == 1.0) and oper == "*":
        msg += msg_7
    if (a == 0.0 or b == 0.0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


memory = 0.0
input_prmt, result = False, 0
while not input_prmt:
    user_input = input("Enter an equation\n")
    equation = user_input.split()
    x, operation, y = equation[0], equation[1], equation[2]
    if 3 < len(equation) > 3:
        print(msg_0)
    elif ((not x.isdigit() and not check_float(x) and not x == "M") or
          (not y.isdigit() and not check_float(y) and not y == "M")):
        print(msg_1)
    elif operation not in operations:
        print(msg_2)
    else:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x, y = float(x), float(y)
        if x % 1.0 == 0.0 or x == 0.0:
            x = int(x)
        if y % 1.0 == 0.0 or y == 0.0:
            y = int(y)
        x, y = str(x), str(y)
        check_func(x, y, operation)
        x, y = float(x), float(y)
        if operation == "/" and y == 0:
            print(msg_3)
            continue
        if operation == "+":
            result = x + y
        elif operation == "-":
            result = x - y
        elif operation == "*":
            result = x * y
        elif operation == "/":
            result = x / y
        print(result)
        store_result = ""
        while store_result == "":
            store_result = input(msg_4 + "\n").lower()
            if store_result == "y":
                if result % 1.0 == 0.0:
                    result = str(int(result))
                else:
                    result = str(result)
                if is_one_digit(result):
                    make_decision = False
                    msg_index = 10
                    choice_user = input(msg_10 + "\n").lower()
                    if choice_user == "y":
                        msg_answer = choice_user
                        while msg_index < 12:
                            if msg_answer == "y" and msg_index < 12:
                                msg_index += 1
                            elif msg_answer == "n":
                                make_decision = True
                                break
                            if msg_index == 11:
                                msg_answer = msg_11
                            elif msg_index == 12:
                                msg_answer = msg_12
                            msg_answer = input(msg_answer + "\n").lower()
                        if not make_decision:
                            memory = float(result)

                else:
                    memory = float(result)
            elif store_result == "n":
                break
            else:
                continue
        continue_calculations = input(msg_5 + "\n").lower()
        if continue_calculations == "y":
            input_prmt = False
        else:
            input_prmt = True

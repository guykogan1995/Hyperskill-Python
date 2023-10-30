pencil_count = input("How many pencils would you like to use:\n")
passed = False
while not passed:
    try:
        pencil_count = int(pencil_count)
        if pencil_count == 0:
            print("The number of pencils should be positive;")
            pencil_count = input()
        else:
            passed = True
    except ValueError:
        print("The number of pencils should be numeric;")
        pencil_count = input()
name = input("Who will be the first (John, Jack):\n")
names = ["John", "Jack"]
while name not in names:
    print(f"Choose between 'John' and 'Jack';")
    name = input()
while pencil_count > 0:
    ret_str = "|" * pencil_count
    print(ret_str)
    pencils_to_take = 0
    if name == "Jack":
        print("Jack's turn:")
        if pencil_count % 4 == 0:
            pencils_to_take = 3
        elif (pencil_count + 1) % 4 == 0:
            pencils_to_take = 2
        elif (pencil_count + 2) % 4 == 0:
            pencils_to_take = 1
        else:
            pencils_to_take = 1
        print(pencils_to_take)
    else:
        pencils_to_take = input(f"{name}'s turn:\n")
        while pencils_to_take not in ["1", "2", "3"]:
            pencils_to_take = input("Possible values: '1', '2' or '3'\n")
        pencils_to_take = int(pencils_to_take)
        while pencils_to_take > pencil_count:
            print("Too many pencils were taken")
            pencils_to_take = input()
            while pencils_to_take not in ["1", "2", "3"]:
                pencils_to_take = input("Possible values: '1', '2' or '3'\n")
            pencils_to_take = int(pencils_to_take)
    pencil_count -= pencils_to_take
    if name == "John":
        name = "Jack"
    else:
        name = "John"
print(name + " won!")

import random

names = []
friend_count = int(input("Enter the number of friends joining (including you):\n"))
if friend_count <= 0:
    print("No one is joining for the party")
    exit(0)
names.append(input("\nEnter the name of every friend (including you), each on a new line:\n"))
for i in range(friend_count - 1):
    names.append(input())

bill_value = int(input("\nEnter the total bill value:\n"))
user_response = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n").lower()
bill_dict = {i: k for (i, k) in zip(names, [round(bill_value / friend_count, 2)] * friend_count)}
if user_response == "yes":
    name = random.choice(names)
    print(f"{name} is the lucky one!")
    bill_dict = {i: round(bill_value / (friend_count - 1), 2) for i in bill_dict}
    bill_dict[name] = 0
    print(bill_dict)
else:
    print("No one is going to be lucky.")
    print(bill_dict)



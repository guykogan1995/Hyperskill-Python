# Write your code here
print("""Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: $5405.0""")
income = 5405
expenses = int(input("Staff expenses:\n"))
other_expenses = int(input("Other expenses:\n"))
print(f"Net income: ${income - (expenses + other_expenses)}")


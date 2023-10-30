# Bill Splitting Program

This is a simple Python program that helps you split a bill among a group of friends. It also has a "Who is lucky?" feature where one random friend gets their share of the bill waived. Here's how to use the program:

1. Run the script in your Python environment.
2. Enter the number of friends joining the party, including yourself.
3. Enter the names of each friend (including yourself) one by one.
4. Enter the total bill value.
5. Decide whether you want to use the "Who is lucky?" feature by entering "Yes" or "No."

## Example Output

Here's an example of what the program's output might look like:

```
Enter the number of friends joining (including you):
4

Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
David

Enter the total bill value:
120

Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes

David is the lucky one!
{'Alice': 30.0, 'Bob': 30.0, 'Charlie': 30.0, 'David': 0}
```

In this example, the total bill is $120, and the "Who is lucky?" feature was enabled, so David was chosen as the lucky one, and his share of the bill was waived.

If you choose "No" for the "Who is lucky?" feature, the output would look like this:

```
Enter the number of friends joining (including you):
4

Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
David

Enter the total bill value:
120

Do you want to use the "Who is lucky?" feature? Write Yes/No:
No

No one is going to be lucky.
{'Alice': 30.0, 'Bob': 30.0, 'Charlie': 30.0, 'David': 30.0}
```

In this case, no one is chosen as the lucky one, and everyone pays an equal share of the bill.

Enjoy splitting your bills with friends using this program!
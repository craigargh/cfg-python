# Homework: Session 3

Topics in this session:
1. Comparison Operators
1. Logical Operators
1. If Statements


Additional resources:
- Comparisons https://realpython.com/python-operators-expressions/
- if statements https://realpython.com/python-conditional-statements/


# Task 1

Create a program that tells you whether or not you need an umbrella when you leave the house.

The program should:
1. Ask you if it is raining using `input()`
1. If the input is 'y', it should output 'Take an umbrella'
1. If the input is 'n', it should output 'You don't need an umbrella'

# Task 2

I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. 

Have a look at my program and work out what I've done wrong

```python
my_money = input('How much money do you have? ')
boat cost = 20 + 5

if my_money < boat_cost:
	print('You can afford the boat hire')
else:
	print('You cannot afford the board hire')
```

# Task 3

I work for an antique book shop and want to quickly categorise books by the century and decade that they were written.

Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Eighteenth Century, Seventies")

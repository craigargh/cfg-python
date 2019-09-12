# Homework: Session 2

This session:

1. User Input
1. Importing modules
1. Problem solving with Turtle
1. For Loops
1. Functions

Additional resources:
- Input https://realpython.com/python-input-output/
- turtle module documentation https://docs.python.org/3/library/turtle.html
- for loops https://realpython.com/python-for-loop/
- functions https://www.datacamp.com/community/tutorials/functions-python-tutorial


## Question 1

Explain what this program does

```python
for number in range(100):
    output = 'o' * number
	print(output)
```

## Question 2

Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to calculate VAT and need your help to fix it.

```python
def calculate_vat(amount):
    amount * 1.2


total = calculate_vat(100)
print(total)
```  

When your boss runs the program they get the following output:

```
None
```

Your boss expects the program to output the value `120`. What is wrong? How do you fix it?


## Question 3

Using the turtle module, write a program to draw a house. The house should at least have a roof, a door and some windows. Feel free to play around with the design of your house. 

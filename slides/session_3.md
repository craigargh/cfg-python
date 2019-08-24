**Starter:** Rewrite this code to use a for loop and the `range()` function:

```python
print('~' * 0)
print('~' * 1)
print('~' * 2)
print('~' * 3)
print('~' * 4)
print('~' * 5)
print('~' * 6)
print('~' * 7)
print('~' * 8)
```

----

Starter solution

```python
for number in range(9):
    print('~' * number)
```

---

![Code First: Girls](images/logo_large.png)

#### Python Session 3

----

Topics in this session:
1. Comparison Operators
1. Logical Operators
1. If Statements

----

By the end of this session you will be able to:

- Identify Boolean data values
- Explain and combine comparison and logical operators to compare data values
- Apply if, else and elif Statements to control the flow of programs
- Build short games using randomisation

---

### Comparisons and Logical Operators

----

**Bolean:** A data-type that is either `True` or `False`

**Comparison operator:** compare values to determine wheter something is `True` or `False`

----

This code checks if the user has input `'Monday'` using the `==` operator

```python
today = input('What day is it? ')

is_monday = today == 'Monday'

print('Today is Monday: {}'.format(is_monday))
```

----

Summary of comparison operators in Python

Name | Python
---|---
Equal to | `==`
Not equal | `!=`
Greater than | `>`
Less than | `<`
Greater than or equal | `>=`
Less than or equal | `<=`

----

`float()` can convert strings to floats

This code checks if the current temperature is freezing:

```python
temperature = input('What is the temperature? ')

is_freezing = float(temperature) <= 0.0

print('The temperature is freezing: {}'.format(is_freezing))
```

----

**Exercise 3.1:** You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

1. Input the `price` of a burger using `input()`
1. Check whether the `price` is less than or equal (`<=`) `10.00`
1. Print the result in the format below

```bash
Burger is within budget: True
```

**Hint:** remember to convert the input from a string to a decimal with `float()`

----

Solution

```python
price = input('How much is a burger? ')

within_budget = float(price) <= 10.00

print('Burger is within budget: {}'.format(within_budget))
```

----

There are logical operators to combine multiple checks

Python | What it does
---|---
and | both expressions are `True`
or | at least one expression is `True`
not | reverse the expression (`True` becomes `False` and vice-versa)

----

This program will work out if you should visit Mars based on whether you want to visit and if you can afford it:

```python
mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print('You should visit Mars: {}'.format(should_visit_mars))
```
----

**Exercise 3.2:** Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget **AND** has a vegetarian option

```bash
Restaurant meets criteria: True
```

----

Solution:

```python
price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')

within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'

is_good_choice = within_budget and has_vegetarian

print('Restaurant meets criteria: {}'.format(is_good_choice))
```

---

### If Statements

----

**if statement:** used to run a block of code depending on whether a condition is `True` or `False`

----

```python
password = input('password: ')

if password == 'jumanji':
    print('Success!')
```

----

An `if` statement has the following:
1. The `if` keyword
1. A condition (comparison)
1. A colon
1. Body (indented four spaces)

----

This program checks whether you are an admin and you have entered the right password:

```python
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

if not is_admin or not is_password_correct:
    print('Go away')
```

----

**Exercise 3.3:** Rewrite the output of your burger program to use if statements

If it is a good choice it should be:

```bash
This restaurant is a great choice!
```

If it is **not** a good choice it should be:

```bash
Probably not a good idea
```

----

Solution

```python
price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')

within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'

is_good_choice = within_budget and has_vegetarian

if is_good_choice:
    print('This restaurant is a great choice!')

if not is_good_choice:
    print('Probably not a good idea')
```

---

### Else Statements

----

**else statement:** Used with an `if` statement and will run when the `if` condition is `False`


----

```python
password = input('password: ')

if password == 'jumanji':
    print('Success!')
else:
    print('Failure!')

```

----

Here's the admin program rewritten to use `else`:

```python
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

else:
    print('Go away')
```

----

**Exercise 3.4:** Now that you've finished your burger, you want to pay for your food. Let's write a program to calculate your meal and apply a discount if applicable. 

If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.

```python
meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount applicable = discount_choice == 'y'
```

----

Solution

```python
meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')
discount applicable = discount_choice == 'y'

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Total cost: {}'.format(meal_price))
```

---


### Elif Statements


----

**elif statement:** used after `if` statements to check whether another condition is `True` or `False`

----

```python
dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')

elif dog_size < 25:
    print('That is a small dog')

else:
    print('That is an average dog')
```

----

You can use multiple `elif` statements together

```python
dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')

elif dog_size < 10:
    print('That dog could fit in my pocket')

elif dog_size < 25:
    print('That is a small dog')

else:
    print('That is an average dog')
```


----

**Exercise 3.5:** You're cooking a pizza and need to check that the oven is at the right temperature. 

Write a program to:
- Ask the user to input the temperature
- Prints "The oven is too hot" if the temperature is over 200
- Prints "The oven is too cold" if the temperature is under 150
- Prints "The oven is at the perfect temperature" if the temperature is 180
- Prints "The temperature is close enough" for any other temperature

----

Solution

```python
temperature = float(input('What is the temperature of the oven? '))

if temperature > 200:
    print('The oven is too hot')
elif temperature < 150:
    print('The oven is too cold')
elif temperature == 180:
    print('The oven is at the perfect temperature')
else:
    print('The temperature is close enough')
```

---

### Random

----

Python has a built-in library for random data

```python
import random

random_integer = random.rand_int(1, 100)

print(random_integer)
```

----

The `rand_int()` function generates a random number between two values

This program uses `rand_int()` to simulate dice with any number of sides

```python
import random

sides = int(input('How many sides does the die have? '))
random_integer = random.rand_int(1, sides)

print('You rolled a {}'.format(random_integer))
```

----

To practice if statements choose one of the following exercises in your student guide:
- Exercise 3.6: Flip a coin
- Exercise 3.7: Rock, Scissors, Paper
- Exercise 3.8: Roulette

----

**Exercise 3.6:** This program uses random to simulate a coin flip.

To finish the program you will need to add the following:
- If the random coin flip matches the choice input by the user then they win
- Ohterwise if the random coin flip does not match the choice input by the user then they lose

```python 
import random

def flip_coin():
    random_number = random.rand_int(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = int(input('heads or tails: '))
result = flip_coin()

print('The coin landed on {}'.format(result))
```

----

**Exercise 3.7:** This program simulates rock, paper, scissors. The first winning condition has been added. To finish the program you'll need to add all of the other winning and losing conditions.

```python
import random

def random_choice():
    choice_number = random.rand_int(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'

    return choice

my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice = 'rock' and opponent_choice == 'scissors':
    print('You win!')
```

----

**Exercise 3.8:** Not Quite Roulette

Ask the user to enter the following three things using `input()`:
- The amount they want to bet
- A colour (red or black)
- A number between 1 and 100

After generating a random number and colour:
- If the colour matches, the users keeps the amount that was bet
- If the number matches, the users wins double the amount that was bet
- If the colour and number matches, the users wins 100 times the amount that was bet
- When neither the colour or number matches the user wins 0
- Output the amount the user won

The following code will generate a random number and colour:

```python
import random


def colour():
    random_number = random.rand_int(1, 2)

    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'

    return colour


random_number = random.rand_int(1, 100)
random_colour = colour()
```

---

### Recap

----

This session:
1. Comparison operators 
1. Logical Operators
1. If Statements

----

Question 1: Equals to (==) is a comparison operator. Name two more comparison operators

----

Question 2: What is the output of this code?

```python
print(True and True)
print(True and False)
print(True or True)
print(True or False)
```

----

Question 3: I expect this code to output "This is too many apples", but instead it outputs "That is a sensible number of apples". Why does this happen?

```python
apples = 100

if apples >= 10:
    print('That is a sensible number of apples')
elif apples > 50:
    print('This is too many apples')
elif apples < 10:
    print('That is not enough apples')
```

----



**Homework:** Session 3 homework questions in your student guide

**Starter:** ???

---

# Code First: Girls

#### Python Session 3

----


This session:
1. Logical Operators
1. If Statements
1. Functions
1. Dictionaries

---

### Logical Operators

----

**Bolean:** A data-type that is either `True` or `False`

**Logical Operators:** used to check if an expression is `True` or `False`

----

This code checks if the user has input `'Monday'` using the `==` operator

```python
today = input('What day is it? ')

is_monday = today == 'Monday'

print('Today is Monday: {}'.format(is_monday))
```

----

Operators in Python

Name | Python
---|---
Equal to | `==`
Not equal | `!=`
Greater than | `>`
Less than | `<`
Greater than or equal | `>=`
Less than or equal | `<=`

----

This code checks if today is not Monday
```python
today = input('What day is it? ')

is_not_monday = today != 'Monday'

print('Today is not Monday: {}'.format(is_not_monday))
```

----

**Exercise:** You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

1. Input the `price` of a burger using `input()`
1. Check whether the `price` is less than or equal (`<=`) `10.00`
1. Print the result in the format below

```bash
Burger is within budget: True
```

**Hint:** remember to convert the input from a string to a decimal with `float()`

----


Answer

```python
price = input('How much is a burger? ')

within_budget = float(price) <= 10.00

print('Burger is within budget: {}'.format(within_budget))
```

----

There are operators to combine multiple checks

Python | What it does
---|---
and | both expressions are `True`
or | at least one expression is `True`
not | reverse the expression (`True` becomes `False` and vice-versa)

----

This program will work out if you should buy a hat:

```python
enough_money = True
hat_looks_good = True

should_buy_hat = enough_money and hat_looks_good

print('You should buy the hat: {}'.format(should_buy_hat))
```
----

**Exercise:** Add code to your burger program to input whether the restaurant has a vegetarian option

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
1. A condition (logical operator expression)
1. A colon
1. Body (indented four spaces)

----

This program checks whether you are an admin and you have entered the right password:

```python
name = input("What is your name? ")
password = input("What is your password? ")

is_admin = name == 'admin'
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

if not is_admin or not is_password_correct:
    print('Go away')
```

----

**Exercise:** Rewrite the output of your burger program to use if statements

Depending on the input the output should be:

```bash
This restaurant is a great choice!
```

Otherwise it should be:

```bash
Probably not a good idea
```

----

**else statement:** Used with an `if` statement and will run when the `if` condition is `False`


----

```python
password = input('password: ')

if password == 'jumanji':
    print('Success!')
else:
    print('Fail!')

```

----

Here's the program that helps you decide whether to buy a hat using `if` and `else`:

```python
enough_money = True
hat_looks_good = True

if enough_money and hat_looks_good:
    print('Go for it!')
else:
    print('Probably not a good idea')
```

---


### Dictionaries

----

**Dictionary:** Stores a colleciton of labelled items. Each item has a key and a value

----

```python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}
```

----

Values in a dictionary are accessed using their keys
```python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])
```

----

**Exercise:** Print the values of `name`, `post_code` and `street_number` from the dictionary

```python
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
```

**Extension:** Print the values of `longitude` and `latitude` from the inner dictionary

----

Solution:

```python
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name'])
print(place['post_code'])
print(place['street_number'])
```

----

Extension:

```python
print(place['location']['longitude'])
print(place['location']['latitude'])


location = place['location']

print(location['longitude'])
print(location['latitude'])
```

----

Putting dictionaries inside a list is very common

```python
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]

for person in people:
    print(person['name'])
    print(person['age'])
```

----

**Exercise:** Using a for loop, output the values `name`, `colour` and `price` of each dictionary in the list

```python
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
```

----

Solution

```python
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])
```


---

### Recap

----

This session:
1. Logical Operators
1. If Statements
1. Functions
1. Dictionaries

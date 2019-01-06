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

**Logical Operators:** used to check if an expression is `True` or `False`

----

This code checks if the user has input `'Monday'` using the `==` operator

``` python
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
``` python
today = input('What day is it? ')

is_not_monday = today != 'Monday'

print('Today is not Monday: {}'.format(is_not_monday))
```

----

**Task:** You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

1. Input the `price` of a burger using `input()`
1. Check whether the `price` is less than or equal (`<=`) `10.00`
1. Print the result in the format below

``` command-line
Burger is within budget: True
```

**Hint:** remember to convert the input from a string to a decimal with `float()`

----


Answer

``` python
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

``` python
today = input('What day is it? ')
sunny = input('Is it sunny? (y/n)')

is_weekend = today == 'Saturday' or today == 'Sunday'
is_sunny = sunny == 'y'

is_beach_good_idea = is_weekend and is_sunny

print('You should go to the beach: {}'.format(is_beach_good_idea))
```
----

**Task:** Add code to your burger program to input whether the restaurant has a vegetarian option

The output should say whether the cost is within budget **AND** has a vegetarian option

``` command-line
Restaurant meets criteria: True
```

----

``` python
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

``` python
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

``` python
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

**Task:** Rewrite the output of your burger program to use if statements

For example:

``` command-line
This restaurant is a great choice!
```

OR

``` command-line
Probably not a good idea
```

----

**else statement:** Used with an `if` statement and will run when the `if` condition is `False`


----

``` python
password = input('password: ')

if password == 'jumanji':
    print('Success!')
else:
    print('Fail!')

```

----

``` python

today = input('What day is it? ')
raining = input('Is it sunny? (y/n)')

is_weekend = today == 'Saturday' or today == 'Sunday'
is_raining = raining == 'y'

is_beach_good_idea = is_weekend and not is_raining

if is_beach_good_idea:
    print('You should go to the beach today!')
else:
    print('Don't go to the beach today')


```

---


### Functions

---- 

**Function:** A reusable block of code

----

``` python
def poem():
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love cats.')


```

----

All functions have
1. a `def` operator
1. a name
1. brackets
1. a colon
1. body (indented 4 spaces)

----

We call a function to use it

``` python
def poem():
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love cats.')


poem()
```
----

Functions can be called many times

``` python
def poem():
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love cats.')


poem()
poem()
poem()
poem()

```
----

**Task:** Using a function, write a poem (or copy one from the internet)

Call the function three times to output the poem three times.

----

**Argument:** A parameter used to change the behaviour of a function

----

Arguments go inside the brackets and are treated like variables

``` python
def poem(thing_that_i_love):
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love {}.'.format(thing_that_i_love))


poem('pancakes')
```

----

**Task:** Modify your poem function to use an argument to set a single word in your poem.

**Extension:** Use the `input()` with a variable. Use that variable for your function's argument.

----

```python
def poem(thing_that_i_love):
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love {}.'.format(thing_that_i_love))

poem("Python")
```

----

``` python
def poem(thing_that_i_love):
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love {}.'.format(thing_that_i_love))


thing = input('Enter something that you love: ')
poem(thing)
```

----

Functions can have multiple arguments seperated by commas

``` python
def poem(thing_that_i_love, author, title):
    print(title)
    print('')
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love {}.'.format(thing_that_i_love))
    print('')
    print('by {}'.format(author))


poem('hamburgers', 'Hamburgler', 'A Poem About Hamburgers')
```

----

Values can be returned from functions using the `return` operator

``` python
def add(num_1, num_2):
    return num_1 + num_2

my_height = 182
friend_height = 160

total_height = add(my_height, friend_height)

print(total_height)
```

----

**Task:** Complete the function to return the area of a circle



Use the comments to help you

``` python
def circle_area():  # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    # return area here


area =  circle_area(10)

print(area)

```

----

Answer

``` python
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

area = circle_area(9)

print(area)
```
---

### Dictionaries

----

**Dictionary:** Stores a colleciton of labelled items. Each item has a key and a value

----

``` python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}
```

----

Values in a dictionary are accessed using their keys
``` python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])
```

----

**Task:** Print the values of `name`, `post_code` and `street_number` from the dictionary

``` python
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

Solution

``` python
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

``` python
print(place['location']['longitude'])
print(place['location']['latitude'])


location = place['location']

print(location['longitude'])
print(location['latitude'])
```

----

Putting dictionaries inside a list is very common

``` python
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]

for person in people:
    print(person['name'])
    print(person['age'])
```

----

**Task:** Using a for loop, output the values `name`, `colour` and `price` of each dictionary in the list

``` python
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
```

----

``` python
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
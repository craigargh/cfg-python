Fill in the blanks:

\_\_\_\_\_\_: a Python **data type** for **whole numbers**.

\_\_\_\_\_\_: a Python **data type** for **decimal numbers**.

\_\_\_\_\_\_: a Python data type for **text** and **characters**.

\_\_\_\_\_\_: a reusable **label** for a piece of data in Python.


*(5 mins)*

----

Answers:

**Integer:** a Python **data type** for **whole numbers**.

**Float:** a Python **data type** for **decimal numbers**.

**String:** a Python data type for **text** and **characters**.

**Variable:** a reusable **label** for a piece of data in Python.

---

# Code First: Girls

#### Python Session 2

---

Homework

---

This session
1. Functions
1. Lists
1. For loops
1. Boolean operators
1. If statements

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
    print('But never doubt I love {}}.'.format(thing_that_i_love))


poem('pancakes')
```

----

**Task:** Change your poem function to use an argument to change its output

**Extension:** store the result of `raw_input()` in a variable and use that when you call your function

----

``` python
def poem(thing_that_i_love):
    print('Doubt thou the stars are fire;')
    print('Doubt that the sun doth move;')
    print('Doubt truth to be a liar;')
    print('But never doubt I love {}}.'.format(thing_that_i_love))


thing = raw_input('Enter something that you love: ')
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
    print('But never doubt I love {}}.'.format(thing_that_i_love))
    print('')
    print('by {}'.format(author))


poem('hamburgers', 'Hamburgler', 'I love hamburgers')
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


area =  # call the function with a number here

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

### Lists

----

**List:** an ordered collection of values

----

List are written inside square brackets and separated by commas


``` python
lottery_numbers = [4, 8, 15, 16, 23, 42]
```

``` python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
```

----

Lists can be made up of values of one or more data types

``` python
orchid_row = ['Magnoliopsida', 12, 3, 8, 9, 'white']
```

----
List values can be accessed using their **index** in square brackets

``` python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

print(student_names[2])
```

Outputs:

``` command-line
Helena
```

----

List indexes start counting from 0

``` python
student_names = [
    'Diedre',    # index 0
    'Hank',      # index 1
    'Helena',    # index 2
    'Salome'   # index 3
]

print(student_names[0])
```

Outputs:

``` command-line
Diedre
```

---

### For Loops

----

Lists ♥ `for` loops

----

**`for` loop:** allows you to repeat a block of code for every item in a list

----

``` python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

for student_name in student_names:
    print(student_name)
```

Output


``` command-line
Diedre
Hank
Helena
Salome
```
----

A `for` loop has
- A `for` operator
- A variable name that stores each list value one at a time
- An `in` operator
- A list of values
- A body (indented four spaces)

----

**Task:** I have a load of cats and need you to feed them when I'm on holiday

Here is a list of all my cats

``` python
cats = ['Fluffy', 'Ginger', 'Whiskers', 'Rod']
```

To feed all my cats write a for loop that contains this code
``` python
print('I am feeding {}'.format(cat))
print('{} says meow'.format(cat))
```

----

``` python
cats = ['Fluffy', 'Ginger', 'Whiskers', 'Rod']

for cat in cats:
    print('I am feeding {}'.format(cat))
    print('{} says meow'.format(cat))

```

----

The pre-written `range()` function returns a list of numbers

``` python
for number in range(5):
    print(number)
```

Outputs

``` command-line
0
1
2
3
4
```

----

**Task:** Using a `for` loop, the `range()` function and the multiply operator, print this output:

``` command-line
o
oo
ooo
oooo
ooooo
oooooo
ooooooo
oooooooo
ooooooooo
```

**Extension 1:** Use `raw_input()` to set the number of lines output

**Extension 2:** The `reversed()` function reverses a list. Can you use it to flip the pattern above?

----

Solution

``` python
for number in range(10):
    print('o' * number)
```

Extension

``` python
for number in reversed(range(10)):
    print('o' * number)
```
---

### Logical Operators

----

**Logical Operators:** used to check if an expression is `True` or `False`

----

This code checks if the user has input `'Monday'` using the `==` operator

``` python
today = raw_input('What day is it? ')

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
today = raw_input('What day is it? ')

is_not_monday = today != 'Monday'

print('Today is not Monday: {}'.format(is_monday))
```

----

**Task:** You have a budget of £10 and want to write a program to decide which burger restaurant to go to.

1. Input the `price` of a burger using `raw_input()`
1. Check whether the `price` is less than or equal (`<=`) `10.00`
1. Print the result in the format below

``` command-line
Burger is within budget: True
```

**Hint:** remember to convert the input from a string to a decimal with `float()`

----


Answer

``` python
price = raw_input('How much is a burger? ')

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
today = raw_input('What day is it? ')
raining = raw_input('Is it sunny? (y/n)')

is_weekend = today == 'Saturday' or today == 'Sunday'
is_raining = raining == 'y'

is_beach_good_idea = is_weekend and not is_raining

print('You should go to the beach: {}'.format(is_beach_good_idea))
```
----

**Task:** Add code to your burger program to check whether the restaurant has a vegetarian option

----

``` python
price = raw_input('How much is a burger? ')
vegetarian = raw_input('Is there a vegetarian option? (y/n) ')

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
password = raw_input('password: ')

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

today = raw_input('What day is it? ')
raining = raw_input('Is it sunny? (y/n)')

is_weekend = today == 'Saturday' or today == 'Sunday'
is_raining = raining == 'y'

is_beach_good_idea = is_weekend and not is_raining

if is_beach_good_idea:
    print('You should go to the beach today!')

if not is_beach_good_idea:
    print('Don't go to the beach today')


```

----

**Task:** Rewrite the output of your burger program to use if statements

You should have one output when the restaurant is a good choice and one output for when the restaurant is not a good choice

----

**else statement:** Used with an `if` statement and will run when the `if` condition is `False`


----

``` python
password = raw_input('password: ')

if password == 'jumanji':
    print('Success!')
else:
    print('Fail!')

```

----

``` python

today = raw_input('What day is it? ')
raining = raw_input('Is it sunny? (y/n)')

is_weekend = today == 'Saturday' or today == 'Sunday'
is_raining = raining == 'y'

is_beach_good_idea = is_weekend and not is_raining

if is_beach_good_idea:
    print('You should go to the beach today!')
else:
    print('Don't go to the beach today')


```

---

### Recap

----

1. User input
1. Functions
1. Lists
1. For loops
1. Boolean operators
1. If statements

---

Homework

**Task:** Discuss your solution to the homework task with someone that you didn't work with last week

---

# Code First: Girls

#### Python Session 2

----

Homework

----

This session
1. Functions
1. Lists
1. For loops

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

**Extension 1:** Use `input()` to set the number of lines output

**Extension 2:** The `reversed()` function reverses a list. Can you use it to flip the pattern above?

----

Solution

``` python
for number in range(10):
    print('o' * number)
```

Extension 1

```python
repeat = int(input('How many repeats? '))

for number in range(repeats):
    print('o' * number)
```

Extension 2

``` python
for number in reversed(range(10)):
    print('o' * number)
```
---

### Recap

----

1. Functions
1. Lists
1. For loops

---

**Homework:**

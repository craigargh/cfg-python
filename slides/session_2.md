**Starter:** Discuss your homework with the person sitting next to you

---

![Code First: Girls](images/logo_large.png)

#### Python Session 2

----

This session:
1. Importing libraries
1. Problem solving with Turtle
1. For Loops
1. Lists

---

### Python  Libraries

----

**Library:** Structured code that someone else has written that you can reuse in your programs

----

Libraries are imported into your Python programs:

```python
import turtle
```

Turtle is library for creating basic drawings.

----

After importing a library you can use the library's functions:

```python
import turtle

turtle.forward(100)
turtle.right(130)
turtle.forward(100)

turtle.done()
```

----

`turtle.forward(100)` moves the turtle forward by a number of pixels

`turtle.right(130)` rotates the turtle by a number of degrees

`turtle.done()` tells the turtle that you've finished giving it commands. Without this it will wait for new commands (if run from the shell) or disappear (if run from file).

----

The turtle's speed can be set with `turtle.speed(1)` for slow

---

### Problem Solving (with Turtles)

----

Let's make square together (file name `square.py`)

A square has **four** sides and an angle of **ninety** degrees:

```python
import turtle

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.done()
```

----

Variables can be used to set the angles and size of your shapes:

```python
import turtle

side_length = 200
angle = 90

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.done()
```

Change `square.py` to use variables

----

You can play around with filling the shape and colors:

```python
import turtle

side_length = 200
angle = 90

turtle.fillcolor('red')
turtle.begin_fill()

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.end_fill()

turtle.done()
```

----

**Task:** Using `turtle` draw a triangle

A triangle has **three** sides and an angle of **120** degrees

**Extension:** Make the triangle blue

----

Answer:

```python
import turtle

side_length = 100
angle = 120

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.done()
```

----

Extension Answer:

```python
import turtle

side_length = 100
angle = 120

turtle.fillcolor('blue')
turtle.begin_fill()

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)


turtle.end_fill()

turtle.done()
```

----

**Task:** On the next three slides there are different shapes and drawings.

Choose **some** of the drawings and try to recreate them with `turtle`.

The drawings are grouped by difficulty. Try the level one if you need more support or the level three if you're ready for a challenge.

----

**Level One**

Pentagon: **five** sides, angle of **one-hundred and eight**

Octagon: **eight** sides, angle of **one-hundred and thirty five**

Rectangle: **two** with length **two-hundred**, **two** sides with length **one-hundred**, angle of **ninety**

----

**Level Two**

Right-angled triangle

A parallelagram

Three different sized Squares with different colours

----

**Level Three**

A circle

A star

A cat

----

Solutions for each drawing can be found at [URL FOR SOLUTIONS]()

---

### For Loops

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

----

Level 1 Challenge: Pentagon

Level 2 Challenge: Circle

Level 3 Challenge: Sprial

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

### For Loops ♥ Lists

----

Using lists and for loops together

---


### Recap

----

This session:
1. Importing libraries
1. Problem solving with Turtle
1. For Loops
1. Lists

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
1. Functions

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

turtle.color('red', 'pink')
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

**Exercise 1.1:** Create a new file called `triangle.py`. Using `turtle` draw a triangle.

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

turtle.color('blue', 'blue')
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

---


### For Loops

----

**`for` loop:** allows you to repeat a block of code for every item in a list


----

A `for` loop has
- A `for` operator
- A variable name that stores each list value one at a time
- An `in` operator
- A list of values
- A body (indented four spaces)


----

The pre-written `range()` function returns a list of numbers

```python
for number in range(5):
    print(number)
```

----

For loops are really useful for repeating code. Notice in the original code for the square that you repeat the same bit of code four times:

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

----

Using a for loop you can simplify the program:

```python
import turtle

side_length = 200
angle = 90

for side in range(4):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
```


----

**Exercise 1.2: Choose your sides**

In this exercise you'll create a program that can draw shapes with any number of sides.

When you run the program it will ask you to input the number of sides that the shape should have. The program will then calculate the correct angle for the shape and draw it for you.

I've started the program for you:

```python
import turtle

sides = int(input('Number of sides: ')) 

angle = 360 / sides
side_length = 60

# Add the for loop here
turtle.forward(side_length)
turtle.right(angle)

turtle.done()
```

**Extension:** Create a new file called `spiral.py` and write a program to create a 100 sided spiral with an angle of 90 degrees

----

Solution:


```python
import turtle

sides = int(input('Number of sides: ')) 

angle = 360 / sides
side_length = 60

for side in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
```

----

Extension Solution:

```python
import turtle

sides = 100 

angle = 360 / sides

for side in range(sides):
    turtle.forward(side)
    turtle.right(angle)

turtle.done()
```

---

### Lists

----

**List:** an ordered collection of values

----

List are written inside square brackets and separated by commas


```python
lottery_numbers = [4, 8, 15, 16, 23, 42]
```

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
```

----

Lists can be made up of values of one or more data types

```python
orchid_row = ['Magnoliopsida', 12, 3, 8, 9, 'white']
```

----
List values can be accessed using their **index** in square brackets

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

print(student_names[2])
```

----

List indexes start counting from 0

```python
student_names = [
    'Diedre',    # index 0
    'Hank',      # index 1
    'Helena',    # index 2
    'Salome'   # index 3
]

print(student_names[0])
```

---

### For Loops ♥ Lists

----

Using lists and for loops together

----



```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

for student_name in student_names:
    print(student_name)
```

----

**Exercise 1.3:** I have a load of cats and I want you to create a piece of art with all of their names on it.

You need to use the turtle library to write the cats' names on each corner of a square.

The `turtle.write()` function will write a string using turtle. I've started the code for you, you need to add the for loop:


```python
import turtle

cat_names = ['Fluffy', 'Ginger', 'Whiskers', 'Rod']

# Add for loop here

turtle.write(cat_name)
turtle.forward(100)
turtle.right(90)

turtle.done()

```

----

Solution:

```python
import turtle

cat_names = ['Fluffy', 'Ginger', 'Whiskers', 'Rod']

for cat_name in cat_names:
    turtle.write(cat_name)
    turtle.forward(100)
    turtle.right(90)

turtle.done()

```

---

### Functions

----

**Function:** A reusable block of code

----

```python
import turtle


def square():
    side_length = 100
    angle = 90

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
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

```python
import turtle


def square():
    side_length = 100
    angle = 90

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)


square()
```
----

Functions can be called many times

```python
import turtle


def square():
    side_length = 100
    angle = 90

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)


square()
turtle.forward(150)
square()
```

----

**Exercise 1.4:** Create a function that draws a triangle using turtle.

----

Solution:

```python
import turtle


def triangle():
    side_length = 100
    angle = 120

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)


triangle()
```



----

**Argument:** A parameter used to change the behaviour of a function

----

Arguments go inside the brackets and behave like variables

```python
import turtle


def square(side_length):
    angle = 90

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

square(60)
square(100)
```

----

**Exercise 1.5:** Modify your triangle function so that you can set the **side length** using an argument

**Extension:** Use a second argument to set the **colour** of the triangle

----

Solution:

```python
import turtle


def triangle(side_length):
    angle = 120

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)


triangle(400)
triangle(300)
triangle(200)
triangle(100)
```
----

Extension:

```python
import turtle


def triangle(side_length, colour):
    angle = 120
    
    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()


triangle(400, 'red')
triangle(300, 'pink')
triangle(200, 'blue')
triangle(100, 'yellow')
```

----

Functions can have multiple arguments seperated by commas

```python
import turtle


def square(side_length, colour):
    angle = 90

    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()

square(400, 'red')
square(300, 'pink')
square(200, 'blue')
square(100, 'yellow')
```

----

Values can be returned from functions using the `return` operator

```python
def add(num_1, num_2):
    return num_1 + num_2

my_height = 182
friend_height = 160

total_height = add(my_height, friend_height)

print(total_height)
```

----

**Exercise 1.6:** Complete the function to return the area of a circle



Use the comments to help you

```python
def circle_area():  # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    # return area here


area =  circle_area(10)

print(area)

```

----

Answer

```python
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

area = circle_area(9)

print(area)
```
---


### Recap

----

This session:

1. Importing libraries
1. Problem solving with Turtle
1. For Loops
1. Lists
1. Functions

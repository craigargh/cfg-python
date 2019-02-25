# Session 2.


This session:

1. Importing libraries
1. Problem solving with Turtle
1. For Loops
1. Lists
1. Functions


## Python  Libraries

Libraries allow you to reuse code that other people have written for a specific purpose. This can save you time and effort. In this session you'll use a library called `turtle` that can create simple drawings.



> **Library:** Structured code that someone else has written that you can reuse in your programs

With Python there are two types of libraries. The first is called a standard library and is pre-installed when you install Python. The other type of library are not part of the standard library and need to be installed separately. We'll cover this other type of library in a later session. The `turtle` library is part of the standard library so you don't need to do any more steps to install it.

The first thing that you do when using libraries with your Python program is to *import* it. This tells Python to load the library so that you can use it in your program.

This is what a basic import looks like in Python:

```python
import turtle
```

The import has two parts:

1. The `import` statement
1. The name of the library that is being imported 

Now that the turtle library is imported you can start using it's functions in your program. When run, this program draws one line, turns one-hundred and thirty degrees and draws a second line. When you run the program you should see an arrow that draws the shapes. This arrow is the turtle.


```python
import turtle

turtle.forward(100)
turtle.right(130)
turtle.forward(100)

turtle.done()
```



The `turtle.forward()`, `turtle.right(130)`, and `turtle.done()` commands all start with `turtle.`. This tells Python that we want to use the command from the `turtle` library.


The `turtle.forward()` funciton makes the turtle move forward a number of pixels, leaving a line behind it. In the program above the turtle moves forward `100` pixels twice. To turn the turtle you use `turtle.right()` and specify a number of degrees. There's a also a `turtle.left()` function that turns it in the opposite direction. 

The `turtle.done()` command tells the turtle that you've finished giving it commands. Without this it will wait for new commands (if run from the shell) or disappear (if run from file).

When playing with the turtle it can be useful to slow it down so that you can see what it going on. The turtle's speed can be set with `turtle.speed(1)` to make it move slowly. Here's the same program with a slower turtle:

```python
import turtle

turtle.speed(1)

turtle.forward(100)
turtle.right(130)
turtle.forward(100)

turtle.done()
```



## Problem Solving (with Turtles)

In this part of the session I'll show you how to use the turtle to draw a square with Python. This may not seem impressive, but it's a good stepping stone for learning so really powerful stuff in Python.


Copy this code into a new Python file in PyCharm (you might want to save it in a file named `square.py`):

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

It should draw a square when you run it.

Let's look at what's going on. A square has **four** sides and an angle of **ninety** degrees. The main part of the program is this:

```python
turtle.forward(100)
turtle.right(90)
```

It draws a line and then turns the turtle `90` degress to the right. These two lines of code are repeated four times to create the square.

Since the same two lines of code are repeated four times, it's a good time to use variables. Here's the program rewritten to use a variable for `side_length` and `angle`:

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

Now if I want to change the size or angle of the shape I only need to change it in one place, instead of four places.


The turtle library comes with lots of neat little things for your drawings. With the `turtle.color()`, `turtle.begin_fill()`, and `turtle.end_fill()` functions you can play around the shape's line and fill colours:

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

In the next exercise you'll take what you've learned about turtle and adapt the above program to create a triangle.

----

**Exercise 1.1:** Create a new file called `triangle.py`. Using `turtle` draw a triangle.

A triangle has **three** sides and an angle of **120** degrees

**Extension:** Make the triangle blue

**Much harder extension** Make a circle (hint: circles aren't one sided shapes, they are three-hundred and sixty sided shapes)

----

## For Loops

Repetition is a very common thing in programming. In this section you'll learn about a very powerful feature in Python called a *for loop*. A for loop is used to repeat a block of code a certain number of times. 

For loops are usually used with something called a list. You'll learn about lists later on in this session. 

**`for` loop:** allows you to repeat a block of code for every item in a list

To write a for loop you need five things:

1. A `for` operator
1. A variable name that stores each list value one at a time
1. An `in` operator
1. A list of values
1. A body (indented four spaces)

Here's an example of a four loop that will print the number `0`, `1`, `2`, `3`, and `4`:

```python
for number in range(5):
    print(number)
```

Let's break down what's going on here. Look at the `range(5)` function. This function is used to tell the for loop how many times to repeat. Here I've used the value `5` so the for loop will repeat 5 times.

The `number` part of the for loop works like a variable. The value of the variable is set by the `range()` function and changes each time the loop repeats. 

The first time the loop runs the value of `number` is set to `0`. The body of the loop is then run. In this case the body is `print(number)`, which will print the value of the `number` variable (`0`). After the body has completed running the loop starts again. 

The second time the loop runs the value of `number` is set to `1`. The body then runs, once again printing the value of `number`. The loops repeats three more times in total, setting the value value of `number` to `2`, `3`, and `4` in the third, fourth, fifth repeats respectively.

After the fifth loop has finished the `range()` function doesn't return any more numbers so the loop stops. 

For loops are really useful for repeating code. Notice that in the original code for the square I repeated the same bit of code four times:

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

Using a for loop I can simplify the program by using a for loop to do the repetition:

```python
import turtle

side_length = 200
angle = 90

for side in range(4):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
```

This code will draw an identical square. The benefit here is the code is more concide. If the shape became more complex, for example if it had 360 sides instead of 4, the code would look almost the same:

```python
import turtle

side_length = 1
angle = 1

for side in range(360):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
```

All that's change here are the values of `side_length`, `angle`, and the number inside the `range()` function. Now imagine instead that I wanted to write this same program without the for loop. It would be over 700 lines long, making it hard to change and hard to spot errors. 

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


## Lists

So far you've seen three data-types: strings, integers, and floats. You're now going to learn about a new, very special, data-type called a list.

Like a list in the real world, a Python list is a collection of multiple pieces of data kept together. Lists are a special data-type in that they can contain multiple values of other data-types. 

**List:** an ordered collection of values

List are written inside square brackets and separated by commas. Here's a list of integer values that I've named `lottery_values` using a variable:


```python
lottery_numbers = [4, 8, 15, 16, 23, 42]
```

The next list has a collection of string values to create a list of students' names:

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
```

Lists can be made up of values of one or more data types. In this list I'm recording my friend's name as a string and their age as an integer:

```python
friend = ['Hilda', 27]
```

You'll often want to get values out of a list. List values can be accessed using their **index** in square brackets:

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

print(student_names[2])
```

When this program runs it will output `'Helena'`. The `students[2]` part of the code gets the value in the second index of the list. In this case the value is `'Helena'`. 

Why is the value in index 2 `'Helena'` and not `'Hank'`?

List indexes start counting from 0. In the above list the value of `'Diedre'` is at index `0`, `'Hank'` is at index `1`, `'Helena'` at `2`, and `'Salome'` at `3`. 

I've formatted the program and added comments to illustrate this clearer:

```python
student_names = [
    'Diedre',    # index 0
    'Hank',      # index 1
    'Helena',    # index 2
    'Salome'   # index 3
]

print(student_names[0])
```

There is a reason that list indexes start at `0` instead of `1`. Old computers had a very small memory. To save memory list indexes started at `0` instead of `1`. With modern computers memory isn't as much of an issue, but the tradition of starting list indexes at `0` was still kept around. 


## For Loops ♥ Lists



Using lists and for loops together

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


## Functions

**Function:** A reusable block of code

```python
import turtle


def square():
    side_length = 100
    angle = 90

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
```

All functions have
1. a `def` operator
1. a name
1. brackets
1. a colon
1. body (indented 4 spaces)

If you ran the above code it wouldn't do anything. All you've done is define a function, you actually need to *call* the function to use it.

To call a function you write the function's name followed by brackets like the call to `square()` on the last line of this program:

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

**Argument:** A parameter used to change the behaviour of a function


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


## Recap


This session:

1. Importing libraries
1. Problem solving with Turtle
1. For Loops
1. Lists
1. Functions



If tkinter isn't installed on Linux:

```bash
sudo apt-get install python3-tk 
```
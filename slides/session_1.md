Make sure that you have installed:
1. Python 3.7 (www.python.org/downloads/)
1. PyCharm Community Edition (www.jetbrains.com/pycharm/download/)

---

![Code First: Girls](images/logo_large.png)

#### Python Session 1

----

Course overview:

1. Data types, variables and operations
1. Input, functions, loops and conditionals
1. Flask
1. APIs
1. Git and the command-line
1. Group project and Deploying code
1. Group project
1. Group presentations

----

Instructor Introductions

----

This session:
1. Run Python with files and shell
1. Data types
1. Maths operations
1. Understanding Error Messages
1. Variables
1. User input

----

Put a coloured Post-It note on the back of your laptop monitor during exercises:
- Red/pink: I need instructor support
- Green: I do not need instructor support

----

PyCharm

[EXPLAIN WHY WE'RE USING PYCHARM]

----

Slides are available at [https://github.com/craigargh/cfg-python](https://github.com/craigargh/cfg-python)

---

### Why Python?

----

[WRITE DEFINITIONS]

**Program:** 

**Programming Language:**

----

[EXPAND EACH OF THESE INTO A SLIDE EACH]

Python:
1. Designed to be clean and readable
1. 3rd party libraries
 - Web
 - Data science
 - Machine learning
1. Popular
1. Open Source

----

PyCon - Annual conferences held in different countries

Scholarships for under-represented groups

---

### Your first Python program

----

Create a new project called `cfg_python`

![create new PyCharm project](gifs/pycharm_new.gif)

----

Create a new Python file called `hello` (`.py` is added automatically)

![create new PyCharm file](gifs/pycharm_new_file.gif)

----

Add this code to `hello.py`

```python
print('Hello, World!')
```

----

Run the program

![run the Python program](gifs/pycharm_run.gif)

----

🎉 Congratulations! 🎉 

You've just run your first Python program

---


### Numbers and Operators in Python

----

**Integer:** a Python **data type** for **whole numbers**. For example `5`, `-99` and `1048` are all integers.

**Float:** a Python **data type** for **decimal numbers**. For example `5.6`, `9.0` and `-67.1001` are all floats.

----

There are two main ways to write and run Python programs:
1. With files 
1. On the Python shell (also called console)

----

Python files:
- `.py` file extension
- Runs all lines from top-to-bottom
- Only shows output when using `print()`
- Can be re-run

----

The Python shell:

- Each line starts with `>>>`
- Runs one line at a time
- Interactive
- Immediate output
- Exploration
- Can't re-run (use files instead)

----

![open Python shell](gifs/pycharm_python_shell.gif)

----

**Exercise 1.1:** Type these lines into your **Python shell**:

```python
5 - 6
8 * 9
6 / 2
5 / 2
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4
```

What does each one do and what is its output?

Are there any outputs you didn't expect?

----
Subtraction:
```python
5 - 6
```

Multiplication:
```python
8 * 9
```

Division:
```python
6 / 2
```

Division (different behaviour in Python 2):
```python
5 / 2
```

Float division:
```python
5.0 / 2
```

Modulo (remainder):
```python
5 % 2
```

Brackets:
```python
2 * (10 + 3)
```

Exponent (x to the power of y)
```python
2 ** 4
```

----

Operator types
* `+`: add
* `-`: subtract
* `*`: multiply
* `/`: division
* `**`: exponent
* `%`: modulo (remainder)

---

### The String Data Type

----

**String:** a Python data type for **text** and **characters**.

`'Hello'`, `"abcdef1234"` and `'cats'` are all strings

----

Strings must be written between a pair of single or double speech marks

 `'...'` or `"..."`


```python
"This is a string"
```

```python
'This is also a string'
```

----
Forgetting the speech marks

```python
hello
```

Will cause this exception

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
```

----
To fix it add speech marks


```python
"hello"
```

----

The `*` and `+` operators work on strings as well as integers.

Let's investigate what they do

----
**Exercise:**

In your **Python shell** type each of these

```python
"Cat"
"Cat" + " videos"

"Cat" * 3
"Cat" + 3

"Cat".upper()
"Cat".lower()

"the lord of the rings".title()
```

What is the output for each one and why?

One of them causes an exception. Read the exception message. What do you think it means?

----

Results:

```python
"Cat"
```

```python
"Cat" + " videos"
```

```python
"Cat" * 3
```

```python
"Cat" + 3
```

```python
"Cat".upper()
```

```python
"Cat".lower()
```

```python
"the lord of the rings".title()
```

----

1. The `+` operator can join two strings together, this is called **concatenation**

1. The `*` operator repeats a string a number of times

1. `.upper()`, `.lower()` and `.title()` are **methods**. They perform a specific action on the string e.g. uppercasing the characters

----

This exception is caused when trying to join a string value with an integer value

```python
>>> print("Cat" + 3)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```

----

Putting a number in `str()` converts it to a string

```python
>>> print("Cat" + str(3))
Cat3
```

---

### Variables

----

**Variable:** a reusable **label** for a piece of data in Python

----

Creating (assigning) a variable has three parts:
1. The variable's name
1. An equals sign `=`
1. The data value it references

```python
username = 'l33t_cat'
age = 23
```

----

Values and variables are interchangeable

A variable can be put anywhere that a data value can be used

```python
print('spaghetti')
```


```python
food = 'spaghetti'
print(food)

```

----

Variables can be reused. This program calculates the cost of 12 oranges. 

```python
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

print(str(oranges) + " oranges")
print("costs " + str(total_cost))
```

The `oranges` variable is used twice in the program

----

**Exercise**: In a new Python **file** called `cat_food.py`, create a program that calculates how many cans of cat food you need to feed 10 cats

Your will need:
1. A **variable** for the number of **cats**
1. A **variable** for the number of **cans** each cat eats in a day
1. A `print()` function to output the result

**Extension:** change the calculation to work out the amount needed for 7 days
----

An example answer:

```python
cats = 10
cans = 2

total_cans = cats * cans

output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)
```

----

Extension answer:

```python
cats = 10
cans = 2
days = 7

total_cans = cats * cans * days

msg = str(cats) + " cats eat " + str(total_cans) + " cans in " + str(days) + " days"
print(msg)
```

---

### String Formatting

----

Python strings have a method (`.format()`) that substitutes placeholders `{}` for values

```python
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

output = "{} oranges costs £{}".format(oranges, total_cost)

print(output)
```

----

This could have been written as:

```python
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

output = str(oranges) + " oranges costs £" + str(total_cost)

print(output)
```

----

**Exercise:** Rewrite `cat_food.py` to use string formatting instead of joining strings with `+`.

An example of string formatting:
```
user_name = 'l33t_cat'
age = 23

output = '{} is {} years old'.format(user_name, age)
print(output)
```

----

Answer:

```python
cats = 10
cans = 2

total_cans = cats * cans

output = "{} cats eat {} cans".format(cats, total_cans)
print(output)
```

---

### User Input

----

The `input()` function allows you to input data after the program has started running


----

[GIF OF USING input()]

----

In a new file called `my_name.py`

```python
name = input('What is you name? ')
print('Hello, {}'.format(name))
```

----

Oranges with user input

```python
oranges_string = input('How many oranges do you want? ')

oranges = int(oranges_string)
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

output = "{} oranges costs £{}".format(oranges, total_cost)

print(output)
```

----

**Exercise:** Change `cat_food.py` so that the number of cats can be input when the program is run

----

Answer:

```python
cats_string = input('How many cats do you need to feed? ')

cats = int(cats_string)
cans = 2

total_cans = cats * cans

output = "{} cats eat {} cans".format(cats, total_cans)
print(output)
```

---

### Comments

----

**Comment:** a way for a programmer to write human-readable notes in their code. When running a program, comments are ignored by Python.


----

Comments in Python start with a `#`

```python
# A program to calculate the cost of some oranges

oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

output = "{} oranges costs £{}".format(oranges, total_cost)

print(output)
```

---

### Recap

----

1. Run Python with files and shell
1. Data types (Integers, Floats and Strings)
1. Maths operations
1. Variables
1. User input


---

**Homework:**

[https://github.com/craigargh/cfg-python/tree/master/homework/session_1.md](https://github.com/craigargh/cfg-python/tree/master/homework/session_1.md)
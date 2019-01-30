# Session 1



In this session:

1. Running Python files
1. Data types
1. Maths operations
1. Understanding Error Messages
1. Variables
1. User input

Before you start Session 1, make sure that you've followed the setup instructions in the Introduction.

## Your First Python Program

Time to write your first Python program! 

To write and run your first Python program follow each of the four steps below. Refer back to these steps whenever you want as you'll need to use them throughout the course. 


**Step One:** First let's create a new Python file in Pycharm. 

Right click on the `cfg_python` folder on the Project Tool Window and select `New › Python File`.

![Creating a new file](new_file_image.png)

**Step Two:** In the window enter `hello` as the name and click `OK`. PyCharm will automatically add the `.py` for you.

![Call the file `hello`](name_your_file.png)

**Step Three:** Now that you've create your file, let's add some Python code.

In the file type the following:

```python
print('Hello, World!')
```

> Make sure that `print` has no capital letters. There should also be two speech marks (one either side of the `Hello, World` text) and an opening and closing bracket.

**Step Four:** Now that you've written your Python code, it's time to run it!

To run you program, right click anywhere in the file and click on `Run hello`. You should see PyCharm's Run window appear with the text `Hello, World!`. 

Congratulations! You've just run your first Python program. 

That's cool and everything, but what's going on?

In your program there are two main bits: 
1. The `print()` bit
1. The `'Hello, World!'` bit that's inside of the `print()` bit.

The `print()` bit is an example of a *function*. A function does a specific task. The task of the `print()` function is to display some data value to you, the programmer. If you removed the `print()` your program would still run OK, it just wouldn't display the output to you.

> **Function:** a pre-written set of instructions to complete a certain task

In this case the data value that is being displayed is `'Hello, World!'`. This is an example of a *string*. You'll learn about strings in more depth very soon. For the time you just need to know that strings are used to represent text in Python. 

By changing the text in the string, you change the value that is output. For example I've changed the value of the string to output a description of my favourite socks:

```python
print('My favourite socks have blue diamonds')
```

Try changing the value to whatever you want!


## Numbers and Operators

When writing programs you'll often want to work with numbers and do calculations on those numbers. That's what this section is all about. I'll introduce you to two (yes, two!) types of numbers and a bunch of different operators.

The first type of numbers you'll get to know are *Integers*. Integers are whole numbers without decimal points. For example `1`, `4329884` and `-63` are all integers.

The second type of numbers are called *Floats*. A float is any number that has a decimal point. For example `1.65`, `82.0` and `-9.3` are all floats. 

Before you move on I want to tell you about *data types*. A data type refers to what kind of thing a piece of data is. For example `7` has an integer data type and `'Hello, World!'` has a string data type. 

So far you've seen three data types: strings, integers, and floats. You'll cover a few more data types throughout the course. It's important to know what data types you're working with as different data types can have different operations performed on them.

> **Data Type**: The kind of data that determines what values it can be and what operations can be performed with it

> **Integer:** a Python **data type** for **whole numbers**

> **Float:** a Python **data type** for **decimal numbers**

Now that you've seen the two types of number data, let's take a look at *maths operators*. 

A maths operator combines two number values to calculate a result. For example if I wanted to see the result of adding the integer values `5` and `17` together I could use the *addition operator* (`+`) like so:

```python
print(5 + 17)
```

When I run this like of code the value `22` would be displayed.

> **Maths Operator:** An operation that calculates the result of combining two number values

I can also use float values with the addition operator. Here my code will display the result of adding the float values `8.3` and `10.12`:

```python
print(8.3 + 10.12)
```

The value `18.42` should be displayed when this program is ran.

There are a handful of maths operators in Python. Let's do a task to find out how they behave.

----

### **Task 1.1** Operators in the Python Console

In this task you will use different maths operators to discover their purpose. You'll also learn about a different way to run Python code using the Python console.

Python has two main ways to run code: files and the console. You've already used files, let's take a look at the console.

When a Python file is run it will start at the top of the file and run each line one at a time. When it reaches the end of the file the program finishes running. The only way for you the programmer to see the output of the program is to use the `print()` function.

The Python Console is different to files. It immediately shows the result of a line of code without needing to use the `print()` function.

To view the Python Console, go to the top menu and click `View › Tool Window › Python Console`. Each line in the Python Console begins with `>>>`. You can type Python code in and press enter to run it. The Python Console will immediately show the result. 

For example if I enter `9 + 3` on the Python Console it would look like this:

```python
>>> 9 + 3
12

>>>
```

As the Python Console console immediatly shows results it is useful for quickly exploring how new bits of code work. Files on the other hand are useful when you want to run the same code multiple times.

Let's use the Python Console to explore how different Maths Operators work.

In your Python Console type the following lines of code one at a time:

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

Look at the output for each line. What do you think each operator does? Are there any outputs that you didn't expect?

----

[EXPLAIN EACH OF THE OPERATORS USED IN THE EXERCISE]

## Strings



## Variables

Labels

Variables work with all data-types

## String Formatting

There a few different ways to do string formatting in Python

[F-STRINGS]

## User Input


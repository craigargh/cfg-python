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

The `print()` bit is an example of a *function*. A function does a specific task. The task of the `print()` function is to display some data value to you, the programmer.

> **Function:** a pre-written set of instructions to complete a certain task

In this case the data value that is being displayed is `'Hello, World!'`. This is an example of a *string*. You'll learn about strings in more depth very soon. For the time you just need to know that strings are used to represent text in Python. 

By changing the text in the string, you change the value that is output. For example I've changed the value of the string to output a description of my favourite socks:

```python
print('My favourite socks have yellow spots')
```

Try changing the value to whatever you want!


## Numbers and Operators

When writing programs you'll often want to work with numbers and do calculations on those numbers. That's what this section is all about. I'll introduce you to two (yes, two!) types of numbers and a bunch of different operators.



**Operator:** 

----

### **Task 1.1** Getting to know your operators

In a new Python file called `operators.py` add the following lines of code:

```python
python(5 - 6)
python(8 * 9)
python(6 / 2)
python(5 / 2)
python(5.0 / 2)
python(5 % 2)
python(2 * (10 + 3))
python(2 ** 4)
```

Each line contains two numbers and an operator. Python will run the program from top-to-bottom, one line at a time.

Your task is to find explain what each operator does. Are there any outputs that you didn't expect?

----

## Strings

## Variables

Labels

Variables work with all data-types

## String Formatting

## User Input


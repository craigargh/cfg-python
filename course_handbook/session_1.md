# Session 1.

## Getting Started with Python

In this session:

1. Running Python files
1. Data types
1. Maths operations
1. Understanding Error Messages
1. Variables
1. User input

Before you start Session 1, make sure that you've followed the setup instructions in the Introduction.

## Why Python?

There are lots of really great programming languages out there. You may have hear of ones like Java, Ruby, JavaScript (weirdly unrelated to Java), and C. They're all languages (just like human languages such as English and French), but instead of being used to communicate from one person to another, they're used to communicate instructions to a computer.

All languages have a set of rules that specify how you write them. Each language has different rules, but there are some core concepts that are shared between them. 

> **Programming Language:** A language with a set of rules that communicates instructions to a computer

So what's so special about Python? 

Python has a lot going for it. Firstly, Python is designed to be readable. The people who design the Python language have put a lot of care and effort this (so say thanks if you ever see them). One of the benefits of this is that there is a gentler learning curve for beginners compared to some other languages.

Secondly, Python has a large number of third-party libraries. "What's a library?" I hear you ask. In basic terms, a library is a collection of code that other people have written that you can reuse. This saves you a lot of time as you don't have to write that bit of the code yourself. 

In Python there are libraries that are designed to build websites, analyse large amounts of data, draw pictures, hack into computers, make a velociraptor appear, and many more.

> **Library:** Reusable collection of code that someone else has written which you can use

Finally, Python is a very popular language. It's used in a diverse areas like science, machine learning, finance, motion pictures and many more. The skills that you learn as a beginner are a fundamental part of any career that uses Python. 

## Your First Python Program

Time to write your first Python program! 

To write and run your first Python program follow each of the four steps below. Refer back to these steps whenever you want as you'll need to use them throughout the course. 


**Step One:** First let's create a new Python file in Pycharm. 

Right click on the `cfg_python` folder on the Project Tool Window and select `New > Python File`.

**Step Two:** In the window enter `hello` as the name and click `OK`. PyCharm will automatically add the `.py` for you.

**Step Three:** Now that you've create your file, let's add some Python code. In the file type the following:

```python
print('Hello, World!')
```

Make sure that `print` has no capital letters. There should also be two speech marks (one either side of the `Hello, World` text) and an opening and closing bracket.

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

> **Integer:** a Python data type for whole numbers

> **Float:** a Python data type for decimal numbers

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

There are a handful of maths operators in Python. Let's do an exercise to find out how they behave.

----

### Exercise 1.1: Operators in the Python Console

In this task you will use different maths operators to discover their purpose. You'll also learn about a different way to run Python code using the Python console.

Python has two main ways to run code: files and the console. You've already used files, let's take a look at the console.

When a Python file is run it will start at the top of the file and run each line one at a time. When it reaches the end of the file the program finishes running. The only way for you the programmer to see the output of the program is to use the `print()` function.

The Python Console is different to files. It immediately shows the result of a line of code without needing to use the `print()` function.

To view the Python Console, go to the top menu and click `View > Tool Window > Python Console`. Each line in the Python Console begins with `>>>`. You can type Python code in and press enter to run it. The Python Console will immediately show the result. 

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
5 / 0
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4
```

Look at the output for each line. What do you think each operator does? Are there any outputs that you didn't expect?

----

Now that you've tried out the operators, here's a bit more detail about them.

The subtraction operator (`-`) minuses one number from another. For example, the result of `8 - 3` would be `5`.

The multiplication operator (`*`) times two numbers together. The result of `7 * 5` is `35`

To divide one number by another, the division operator (`/`) is used. For example `8 / 4` is `2` and `5 / 2` is `2.5`. Note that you will get an error if you divide by zero that looks like this `ZeroDivisionError: division by zero
`.

The modulo (`%`) operator is similar to division. Instead of saying how many times one number divides by another it works out how many times the first number can be divided prefectly by the second and returns the difference. For example `4` divides perfectly by `2` twice with no remainder so the result is `0`, while `5` divides by `2` twice with a remainder or `1`, so the result is `1`.

The exponent (`**`) operator calculates the power of one number by another. For example `2 ** 3` is `8`, which is equivalent of `2 * 2 * 2`.

By default Python will evaluate operators in the following order:
1. Brackets
1. Exponent
1. Multiplication
1. Division
1. Modulo
1. Addition
1. Subtraction

Brackets can be used to change the order that calculations are done. For example the result of this calculation will be `23`:

```python
2 * 10 + 3
```

By adding brackets around `(10 + 3)` the addition is now calculated first, changing the result to `26`:

```python
2 * (10 + 3)
```

## Strings

Remember back to a short while ago when you wrote you first Python program. The program looked like this:

```python
print('Hello, World!')
``` 

The `'Hello, World!'` part of the program is a data-type is called a *string*. The string data-type in Python is used to represent letters, numbers, symbols and other characters. 

**String:** a Python data type for **text** and **characters**.

All strings begin and end with either single (`''`) or double (`""`) speech marks. 

For example, this is a string...

```python
'Clap clap clap'
```

...and so it this...

```python
"20 cheese cakes"
```

When writing strings you may sometimes forget to include the speech marks entirely. Depending on what's in your string, you will see different errors. Here I haven't included any speech marks for a single word:

```python
Clap
```

I get this error:

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Clap' is not defined
```

The type of error is stated on the last line and is a `NameError`. Python thinks that my string is actually a variable (which you'll learn about in a short while). If you see this error message when using a string, you might have forgotten the speech marks. To fix it, just add the speech marks:

```python
'Clap'
```

Here's another example with multiple words where I've forgotten the speech marks:

```python
Clap clap clap
```

When I run the code in the Python console I get this error:

```bash
  File "<stdin>", line 1
    Clap clap clap
            ^
SyntaxError: invalid syntax
```

This time I get a `SyntaxError`. A `SyntaxError` means that I am not following Python's rules for how to arrange commands. Notice how on the fourth line the error message points to the part of the code that confused Python. Remember to look for this when you see this error message as it can help identify what you need to fix. In this case again the fix is just to put speech around the words:

```python
'Clap clap clap'
```

In the previous exercise you learned about different Python operators and how they behave with number data-types. Some of these operators can be used with strings. In the next exercise you will explore how different operators work with string as well as try some special string commands called methods.


----

### Exercise 1.2: String Operators and Methods

In your **Python console** type each of these commands:

```python
"Cat"
"Cat" + " videos"

"Cat" * 3
"Cat" + 3

"Cat".upper()
"Cat".lower()

"the lord of the rings".title()
```

What is the output for each line and why?

One of the lines causes an exception. Read the exception message. What do you think it means?


----



> **Concatentation:**

> **Method:** 

> **Dot Notation:**

`str()`


## Variables

You're about to be introduced to a very important concept called a *variable*. Are you ready?

**Variable:** A reusable label for a piece of data

A variable is a reusable label for a piece of data. A variable helps Python programs remember pieces of data so that you can reuse them multiple times in your programs.

Look at this line of Python code:

```python
oranges = 12
```

When creating a variable you need three things:
1. A name for the variable
1. An equals sign
1. A value

The name of the variable is `oranges`. The value of the variable is `12`. In between the name and the value there is an equals sign (`=`), which tells Python that you are assigning a value to the variable name. 

In the above example I created a variable with an integer value. You can use any data type with variables. Here's a variable called `name` that has a string value of `"Jonesy"`:

```python
name = 'Jonesy'
```

Once you create a variable it can be used like any other value. Variables and values are interchangable. Wherever you can use a data value you can use a variable.

Let's say that I have 12 oranges and I want to output that. Here I've written a program to do that:

```python
oranges = 12
print(oranges)
```

See how I've put the variable name `oranges` inside the `print()` function's bracket? This is the same as writing `print(12)`. Either way the output will be `12`. The benefit of using a variable is that it can be reused and updated.

I now want to calculate the cost of purchasing oranges. Each orange costs `0.5`. I want to output the total cost and say how many oranges the cost is for. Here's the code:

```python
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

print(str(oranges) + ' oranges') 
print('costs ' + str(total_cost))
```

The output will look something like this:

```
12 oranges
costs 6.0
```

Notice how I've created the `oranges` variable on line 1 and reused it on lines 4 and 6. This means that if I change the value of the `oranges` variable, the value will update everywhere else that it is used. 

Here I've changed the value of `oranges` to 20:

```python
oranges = 20
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

print(str(oranges) + ' oranges') 
print('costs ' + str(total_cost))
```

The rest of the code stays the same, but the output is different:

```
20 oranges
costs 10.0
```
To understand why reusing variables is important here's the code rewritten without the `oranges` variable:

```python
cost_per_orange = 0.5

total_cost = 12 * cost_per_orange

print(str(12) + ' oranges') 
print('costs ' + str(total_cost))
```

I've used the value `12` on lines 3 and 5 instead of the `oranges` variable. If I want to update the number of oranges I now have to update the code in two places instead of one. 

This may seem trivial for such a short program, but when you're working with larger and more complex programs you may forget to update a value and cause the program to behave incorrectly.

Another this you may have noticed is that variables are useful for explaining the purpose of values. In the example without the `oranges` variable, you don't know what the value `12` means without additional explanation. By using a variable the name gives the value context. With a name like `oranges` you can probably tell that the `12` value means the number of oranges.

To recap, variables are labels for pieces of data. Varialbes have a name and a value and can be used wherever you can use a data value. Variables allow you to reuse pieces of data and are useful for indicating the purpose of a value to other people.

----

### Exercise 1.3: Cat Food

In a new Python **file** called `cat_food.py`, create a program that calculates how many cans of cat food you need to feed 10 cats

Your will need:
1. A **variable** for the number of **cats**
1. A **variable** for the number of **cans** each cat eats in a day
1. A `print()` function to output the result

**Extension:** change the calculation to work out the amount needed for 7 days

----

## String Formatting



There a few different ways to do string formatting in Python

[F-STRINGS]

## User Input


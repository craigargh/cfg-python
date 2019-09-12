# Homework: Session 1

Topics this session:

1. Run Python with files and console
1. Recognise data types (Integers, Floats and Strings)
1. Identify different maths operations
1. Understand Error Messages
1. Use variables in your programs


Additional resources:

- Basic Python data-types https://realpython.com/python-data-types/
- Strings https://realpython.com/python-strings/
- String formatting (includes two common alternatives to the string formatting method covered in the session) https://realpython.com/python-string-formatting/
- Understanding error messages https://realpython.com/python-traceback/
- Variables https://realpython.com/python-variables/

## Question 1

I am building some very high quality chairs and need exactly four nails for each chair. I've written a program to calculate how many nails I need to buy to build these chairs.

```python
chairs = '15'
nails = 4

total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)

print('You need to buy {} nails'.format(message))
```

When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails.

Is my program calculating the total number of nails correctly? What is the problem? How do I fix it?


## Question 2

I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix the program?

```python
my_name = Penelope
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)
``` 

## Question 3

I have a lot of boxes of eggs in my fridge and I want to calculate how many omlettes I can make. Write a program to calculate this.

Assume that a box of eggs contains six eggs and I need four eggs for each omlette, but I should be able to easily change these values if I want. The output should say something like "You can make 9 omlettes with 6 boxes of eggs". 

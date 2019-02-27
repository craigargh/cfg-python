# Homework: Session 1

## Question 1

I have written the following Python program to work out how many pizza slices I need to buy for my friends.

```python
people = '15'
pizza_slices = 4

total_pizza_slices = people * pizza_slices

message = 'I need to buy {} pizza slices'.format(total_pizza_slices)

print(message)
```

When I run the program it tells me that I need to buy 15151515 slices of pizza. This seems like a lot of pizza.

Is my program calculating the total number of slices correctly? What is the problem? How do I fix it?



## Question 2

A friend is new to Python and has written this Python program:

```python
raw_input('What is your favourite Pokemon? ')

message = 'Cool! I also like {}'.format(pokemon)
print(message)
```

However, when they run the program, they get this error message. 


```bash
Traceback (most recent call last):
  File "/home/mary/Documents/pokemonproject/favourite.py", line 3, in <module>
    message = 'Cool! I also like {}'.format(pokemon)
NameError: name 'pokemon' is not defined
```

What is the error message telling you? How should your friend fix the error?


## Question 3

I own 20kg of pineapples. Even though I own a lot of pineapples, I still want to buy more.

I want you to write a program to calculate the total weight of the pineapples I will own when I foolishly buy even more pineapples.

Your program should:
1. Create a variable called `current_pineapples` and set the value to `20`
1. Using `raw_input()` ask the user for the weight of the pineapples I plan to buy and assign the value to a variable called `new_pineapples`
1. Add the values of `current_pineapples` and `new_pineapples` together and put the result in a new variable called `total_pineapples`
1. Output the result in the following format `'Seriously. Who needs 32kg of pineapples?'`

*Hint:* The `raw_input()` function returns the user's input as a string. You can convert a string into an integer with the `int()` function e.g.

```python
raw_turtles = raw_input('How many turtles? ')
turtles = int(raw_turtles) 
```

## Question 4

I like to create patterns and I also like to create programs. 

I want you to create a program to output a pattern. The program should ask how many times the pattern should repeat.

For example if I ask the program to repeat once it will output this pattern:

```
.o0o.
```

Whereas if I ask it to repeat 5 times it will output this pattern:

```
.o0o.o0o.o0o.o0o.o0o.
```

# Task 1

Create a program that tells you whether or not you need an umbrella when you leave the house.

The program should:
1. Ask you if it is raining using `raw_input()`
1. If the input is 'y', it should output 'Take an umbrella'
1. If the input is 'n', it should output 'You don't need an umbrella

# Task 2

Here is a list of food

``` python
foods = ['apple', 'cake', 'ham', 'pizza']
```

My favourite food is cake. Here is an if statement that checks whether an item is my favourite food:

``` python
if food == 'cake':
    print('{} is my favourite'.format(food))
else:
    print('{} is not my favourite'.format(food))

```

By combining this if statement with a for loop, check each item in the list to output if it is my favourite food.

The output should look like:
``` command-line
apple is not my favourite
cake is my favourite
ham is not my favourite
pizza is not my favourite

```


# Task 3

This program will pretend to make bicycles. It will output the colour of each bicycle. Every fifth bicycle should be red, all other bicycles should be blue.

The program should:
1. Use a for loop to repeat 30 times
1. Output the bicycle's number and colour
1. If the number of the bicycle divides perfectly by 5, the colour should be red

**Hint:** Try using `bicycle_number % 5 == 0` to work out if the bicycle should be red.

# Session 3 in More Depth



## Logical Operators

Logical operators are all about checking if something is `True` or `False`. This has many applications in programming. Is the password a user has just entered correct? Is there enough money in my account to buy a pair of socks? Can I fit another jelly bean in my mouth?

Notice how all of the above examples are yes or no questions. In Python you can represent a yes as a `True` value and a no as a `False` value.


The `True` and `False` values are both Boolean data types. Named after George Bool, an English Math wizard, Boolean is pronounced like Cool Ian, but with a B.


Like all data types in Python you can use variables to label the values and explain their meaning to other programmers:

```python
am_i_hungry = True
is_it_hot = False
```

On thing to note is that the values `True` and `False` should start with a capital letter. If you miss forget to capitalise the value Python will think the value is a variable and you'll get an error like this:

```bash
>>> i_am_skiing = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

### Checking Stuff is True or False

A lot of the time you won't know if something is `True` or `False` until you check it. This is where logical operators come in. 

In their most basic form logical operators will compare one value with another, then will return `True` or `False` depending on the result.

Say I have five forks and six friends, and I want to know if I have enough forks to throw a dinner party. To do this I can check whether the number of forks I have is greater than my number of friends:

```python
forks = 5
friends = 6

enough_forks = forks >= friends

print('You have enough forks: {}'.format(enough_forks))
```

The output of this program is `You have enough forks: False`

The part of the program that does the comparison is `forks >= friends`. The `>=` bit compares if the value on the left is greater than or equal to the value on the right.

The result of this case is returned and I use the `enough_forks` variable to remember this result. The reason that the result is `False` in this case is because `5` is not greater than or equal to `6`.

I either need more forks or fewer friends.

After a long deliberation I decided to buy one more fork (it was a tought decision):

```python
forks = 6
friends = 6

enough_forks = forks >= friends

print('You have enough forks: {}'.format(enough_forks))
```

Now the output of the program is `You have enough forks: True`

The value of `forks` is now `6`, which is equal to the value of the `friends` variable. So when the `forks >= friends` comparison is made, the value of `enough_forks` is set to `True`.

##### Exercise: Do I have enough eggs to make a really big omlette?

My dinner party is going to be a huge success. My friends will all love how they don't have to share cutlery. I just need to decide what to cook.

To really wow my friends I'm planning to cook a really big omlette. But do I have enough eggs?

I have 17 edible eggs in my fridge. I estimate that I will need three eggs of my friends (remember that I have exactly 6 friends).

Your task is to write a program that calculates whether I have enough eggs for my party omlette. I want the output to look something like this, but with the correct `True` or `False` result:

```
The party omlette has enough eggs: True
```

Be creative with the wording for extra points. Just makes sure it shows the result as `True` or `False`.

### More Ways to Compare Stuff

In the last example I checked whether the number of forks was greater than or equal to the number of friends I have.

Not surprisingly the `>=` comparator in Python is called the `greater than or equal` comparator.

There are other comparators in Python. Let's take a tour of the exciting line-up of comparators that Python has available.

#### Equal To (==)

First up is the `==` or `equal to` comparator. This nifty little comparator checks whether two values are equal. 

Let's say I've built a chair and need to check it has exactly four legs:

```python
required_legs = 4
legs_i_made = 5

right_amount_of_legs = required_legs == legs_i_made

print(right_amount_of_legs)
```

The output of this program is `False`. The values `4` and `5` are not the same so the the result of the comparison is `False`. Oh no I have too many legs on my chair. People are going to give me weird looks.

I've hatily cut off one of the legs with a saw:

```python
required_legs = 4
legs_i_made = 4

right_amount_of_legs = required_legs == legs_i_made

print(right_amount_of_legs)
```

Now the result is `True` as the values `4` and `4` are the same.

Notice how the `equal to` comparator is two equals signs `==`. This looks similar, but is in fact very different, to when you use a single equals sign `=` to create a variable.

Always remember to use a single equals sign `=` when assigning a value to a variable and a double equals sign `==` when comparing two values.

##### Exercise: I'm on chair building spree



#### Checking Things Are Not the Same (!=)



##### Exercise: ???



#### Let's Cover Greater, Less and Their Variants at the Same Time



##### Exercise: How good was the party out of 5 stars



### Joining the Comparisons Together



## If Statements


### Truthy and Falsey


## Problem Solving



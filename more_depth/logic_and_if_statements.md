# Logical Operators and If Statements in More Depth



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

```python
eggs_in_fridge = 17

friends = 6
required_eggs = friends * 3

enough_eggs = 

print('The party omlette has enough eggs: {}'.format(enough_eggs))
```

Your task is to finish my program that calculates whether I have enough eggs for my party omlette. To do this you need to check whether `eggs_is_fridge` is greater than or equal to `required_eggs`. The result should be assigned to the `enough_eggs` variable.

Be creative with the wording of the output for extra points. Just makes sure it shows the result as `True` or `False`.

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

I'm really into building chairs now. If I don't find a way to stop myself I'll have too many chairs for my friends to sit on. They won't know what to do.

Let's write a program to check I have exactly four chairs.

```python
chairs_made = 2
desired_chairs = 6

stop_making_chairs = 

print('Stop making chairs right now: {}'.format(stop_making_chairs))
```

While I hammer and glue bits of wood, it's your job to finish this program. 

You'll need to check `chairs_made` is equal to `desired_chairs`. The result of this comparison should be assigned to the `stop_making_chairs` variable. Only then will I know when to stop making chairs.


#### Checking Things Are Not the Same (!=)

The `equal to` operator has an inverse version of itself, known as the `not equal to` operator. 

In short the `not equal to` will evaluate to `False` is the two values being compared are the same. It will be `True` when the two compared values are different. This is the opposite of the `equal to` comparator.

The `equal to` and `not equal to` operators can be used to compare strings and number (integers and floats) data types.

Here I'm checking that the film my friend wants to watch is not The Shape of Water (I can't watch it with other people, I cry too much at the end)

```python
friends_film_choice = 'The Shape of Water'
film_that_makes_me_cry = 'The Shape of Water'

no_crying = friends_film_choice != film_that_makes_me_cry

print('You will not cry at this film: {}'.format(no_crying))
```

Uh-oh, looks like they've chosen the film that will make me cry so the output is `You will not cry at this film: False`

One thing to note is that when comparing strings the comparators are really strict. A single character difference will change the result of the comparison. For example if I only have a capital letter difference between the two strings, they will be compared as totally different:

```python
friends_film_choice = 'the shape of water'
film_that_makes_me_cry = 'The Shape of Water'

no_crying = friends_film_choice != film_that_makes_me_cry

print('You will not cry at this film: {}'.format(no_crying))
```

The output will be `You will not cry at this film: True`, which is strange because as humans we know they're the same thing. Python is strict in these comparisons because in most cases it does actually matter.

There is a way around this. If you remember back to the first session you learned how to change the case of a string with the `.lower()` method. Using this method you can force both of the strings to be in lower-case, making the comparison consistent with what we expect:

```python
friends_film_choice = 'the shape of water'.lower()
film_that_makes_me_cry = 'The Shape of Water'.lower()

no_crying = friends_film_choice != film_that_makes_me_cry

print('You will not cry at this film: {}'.format(no_crying))
```

The output is back to what I expected `You will not cry at this film: False`. That's that sorted. Now I can focus on crying at an artful story of fish-man romance.


##### Exercise: Is the omlette safe to eat?

So that I don't give my friends food poisoning I need to check that the omlette is safe to eat. How am I going to do that? Well, like all of my other problems, with a Python program!

Using my in-depth knowledge of food science, I have determined that a omlette is safe to eat if it is not runny.

I started writing the program, but then the post man arrived to deliver my eBay purchase of a single spoon. He's what I got so far:

```python
is_runny = input('Is the omlette runny? (y/n)')

is_edible = 
```

I want you to finish my omlette safety checking program. Don't worry, I trust you. Te worst that could happen is my friends never stop telling the story of how I served them plates of raw eggs at a dinner party.

To finish my program you need to use the `not equal` comparison. Use this to check the value of `is_runny` is not equal to `'y'`. The result of this comparison should be assigned to the `is_edible` variable.

You'll also need to add output in this format `The omlette is safe to eat: True`.

#### Let's Cover Greater, Less and Their Variants at the Same Time

Our tour of comparators is realy picking up pace. We're looping back on ourselves and covering the `greater than or equal to` operator and its close siblings.

The `greater than or equal to` comparator has a twin. Their parents named it `less than or equal to` and it looks like `<=`. Like all other comparators it compares two values. In this case is checks whether the value on the left is smaller than or the same as the one on the right.

I'm like average levels of tall. It's only a problem when I'm visiting really small houses and Hobbiton.

Let's see if I can fit through a door:

```python
my_height = 182.1
door_height = 190

can_fit = my_height <= door_height

print('I can walk through this door: {}'.format(can_fit))
```

The output is `I can walk through this door: True`. Nice. No bending over for me.

Oh, wait, here comes another door!

```python
my_height = 182.1
door_height = 182.0

can_fit = my_height <= door_height

print('I can walk through this door: {}'.format(can_fit))
```

This time the output is `I can walk through this door: False`. Ouch.

There are another two comparators that you need to know about. The `less than` and `greater than` comparators. They're just like the `less than or equal to` and `greater than or equal to` comparators, but they won't return `True` if the compared values are the same.

The `greater than` operator looks like this `>` and the `less than` operator looks like this `<`. You might get direction of these mixed up from time to time. I found it was helpful to image that the symbol is a shark's mouth and it wants to eat the larger number.

The final thing to note about the four comparators (`>`, `<`, `>=` and `<=`) is that they work with number data types (integers and floats), but don't work with strings. It's easy for Python to know if `5` is greater than `6`, but not so much for Python to know if `"Air freshener"` is greater than `"Tomato"`. 


##### Exercise: How good was the party out of 5 stars

I've spent months preparing for this dinner party. I've counted numerous eggs multiple times, poured my blood sweat and tears into chairs that are definitely safe to sit on (don't let anyone tell you otherwise), and invested in a new spoon.

When the night is over I want to check that all my hard work paid off. That's right, I'm going to send my friends a survey.

Like all good reviews my dinner party will be rated using 1 to 5 stars. After I've received the ratings I will be heart broken if I receive 3 or less stars.

It's your job to write the program that will tell me that my friends rated my party more than 3 stars. Here you go. I've started it for you.

```python
friends_rating = 4
three_stars = 3

good_rating = 
```

Choose a comparator to decide how you want to compare my `friends_rating` to `three_stars`. Remember a score of `3` or lower is bad, whereas a score of more than `3` is good.

Make sure you output the result with a sentence.

#### Checking Something is in a List

Our final stop on our tour of comparators is a special one. It's the `in` comparator.

This one is special in that it can check whether one value is in a list of other values. 

```python

```

It can also check if one string is inside another string.


```python

```

### Comparing Multiple Things and Checking Opposites



#### and



Comparison | Result
---|---
`True and True` | `True`
`True and False` | `False`
`False and True` | `False`
`False and False` | `False`

#### or

I imagine you're trying to enter an ice-cream shop to buy some delicious and well priced ice-cream. The shop has two doors. To get into the shop only one of the doors needs to be open. If either of the doors or both of the doors is open you can get in.

```python
door_1_open = True
door_2_open = False

is_ice_cream_shop_open = door_1_open or door_2_open

print('I can have some ice-cream {}'.format(is_ice_cream_shop_open))
```

Because door 1 is open, I can get ice-cream. Even though the second door is locked, I can still get into the building for an icey treat.


Comparison | Result
---|---
`True or True` | `True`
`True or False` | `True`
`False or True` | `True`
`False or False` | `False`


#### not



### Putting It All Together

Comparators and logical operators


#### Keeping It Clean


When using operators and comparators together you can actually do a lot in a single line:

```python

valid_qty =  flowers_ordered > 0 and flowers_ordered <= 100 and (flowers_ordered % 5 == 0 or flowers_ordered % 12 == 0)
print('Valid qty of flowers {}'.format(valid_qty))
```

Any idea what the result of that is? No? Me neither. I just wrote that and it takes me quite a while to understand what's going on.

This is bad.

As you progress on your journey as a developer you'll find that being able to work quickly and without simple mistakes is linked to how readable the code is. 

Breaking down complex statements like the one above into smaller parts is one way to make the code more descriptive and easier to understand:

```python
flowers_ordered = 12

at_least_one_flower =  flowers_ordered > 0
no_more_than_100_flowers = flowers_ordered <= 100

in_multiples_of_five = flowers_ordered % 5 == 0
in_multiples_of_twelve = flowers_ordered % 12 == 0

not_too_many_or_few = at_least_one_flower and no_more_than_100_flowers
correct_multiples = in_multiples_of_five or in_multiples_of_twelve

valid_qty = not_too_many_or_few and correct_multiples

print('Valid qty of flowers {}'.format(valid_qty))
```

Now each part has a named variable that clearly explains the purpose of each comparison before they're all joined into the final result. 

I've managed to work out that I need to buy more than `0` flowers and `100` or less flowers. I also need to buy the flowers in multiples of `5` or `12`. 

Although there are more lines, the purpose of each one is clearly explained by the name of the variable. Although it takes me slightly longer to read, it is much faster for me to understand what it is doing and why it is doing it.

We can take this one step further by putting it all together in a function. 

```python

def valid_qty(flowers_ordered):
    at_least_one_flower =  flowers_ordered > 0
    no_more_than_100_flowers = flowers_ordered <= 100

    in_multiples_of_five = flowers_ordered % 5 == 0
    in_multiples_of_twelve = flowers_ordered % 12 == 0

    not_too_many_or_few = at_least_one_flower and no_more_than_100_flowers
    correct_multiples = in_multiples_of_five or in_multiples_of_twelve

    return not_too_many_or_few and correct_multiples


is_valid = valid_qty(12)

print('Valid qty of flowers {}'.format(is_valid))
```

Now all of my code is in a function it can be reused. It also makes the other parts of my code cleaner as the function name explains what it does concisely. It also means the other parts of the code don't need to know how to do this calculation, so the complexity can be kept hidden away from the code that uses the function.


## If Statements


### Truthy and Falsey


## Problem Solving Exercises



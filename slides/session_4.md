**Starter:** ???

---

![Code First: Girls](images/logo_large.png)

#### Python Session 4

----

This session:
1. Lists
1. Dictionaries

---

### Lists

----

**List:** an ordered collection of values

----

List are written inside square brackets and separated by commas


```python
lottery_numbers = [4, 8, 15, 16, 23, 42]
```

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
```

----

Lists can be made up of values of one or more data types

```python
orchid_row = ['Magnoliopsida', 12, 3, 8, 9, 'white']
```

----
List values can be accessed using their **index** in square brackets

```python
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']

print(student_names[2])
```

----

List indexes start counting from 0

```python
student_names = [
    'Diedre',    # index 0
    'Hank',      # index 1
    'Helena',    # index 2
    'Salome'     # index 3
]

print(student_names[0])
```

---

### For Loops ♥ Lists

----

Using lists and for loops together

----



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

Solution:

```python
import turtle

cat_names = ['Fluffy', 'Ginger', 'Whiskers', 'Rod']

for cat_name in cat_names:
    turtle.write(cat_name)
    turtle.forward(100)
    turtle.right(90)

turtle.done()

```

---


### Dictionaries

----

**Dictionary:** Stores a colleciton of labelled items. Each item has a key and a value

----

```python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}
```

----

Values in a dictionary are accessed using their keys
```python
person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

print(person['name'])
```

----

**Exercise:** Print the values of `name`, `post_code` and `street_number` from the dictionary

```python
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
```

**Extension:** Print the values of `longitude` and `latitude` from the inner dictionary

----

Solution:

```python
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name'])
print(place['post_code'])
print(place['street_number'])
```

----

Extension:

```python
print(place['location']['longitude'])
print(place['location']['latitude'])


location = place['location']

print(location['longitude'])
print(location['latitude'])
```

----

Putting dictionaries inside a list is very common

```python
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]

for person in people:
    print(person['name'])
    print(person['age'])
```

----

**Exercise:** Using a for loop, output the values `name`, `colour` and `price` of each dictionary in the list

```python
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
```

----

Solution

```python
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])
```

---

### Recap

----

This session:
1. Lists 
1. Dictionaries

----

**Homework:** Session 4 homework questions in your student guide

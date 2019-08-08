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
    'Salome'   # index 3
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

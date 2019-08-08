### Flask: Routing

----

**Flask:** A Python library for building programs that run on the web, including websites and APIs.

Flask manages things like routing and rendering templates so that you can focus on writing your application's code.

----


We want to install Flask using pip using the Terminal

``` command-line
pip install flask
```

----

Flask is installed along with the packages it depends on

``` command-line
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-0.12.2 itsdangerous-0.24
```

----

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'I am home'


app.run(debug=True)
```

Note: flask_home.py

----

After running the Python program, you can view the website at [localhost:5000](http://localhost:5000)

----

![A basic Flask website shown in the browser](images/flask_home.png)

----

The `@app.route()` code is a **function decorator**.

It tells Flask to run a function when someone goes to a specific url

The function should return a either `string` or a `response` (covered later)

----

This adds [localhost:5000/about/](http://localhost:5000/about/)

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'I am home'


@app.route('/about/')
def about():
    return 'This is a Flask website'


app.run(debug=True)
```



**Tip:** Remember to include the second forward slash after `'about'`

Note: flask_about.py

----

**Task:** Add an app route that returns your name when you go to `localhost:5000/hello/` in your browser

----

Solution

```python
from flask import Flask
app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'James'


app.run(debug=True)
```
---

### Flask: Dynamic Routes

----

So far our Flask app only has fixed routes

Flask can also handle dynamic routing


----

Change your code for the `'/hello/'` route

```python
@app.route('/hello/<name>/')
def hello(name):
    return 'Hello {}'.format(name)

```

In the web browser go to

- [http://localhost:5000/hello/kitty/](http://localhost:5000/hello/kitty/)
- [http://localhost:5000/hello/sailor/](http://localhost:5000/hello/sailor/)
- [http://localhost:5000/hello/friend/](http://localhost:5000/hello/friend/)

Note: flask_dynamic_routing

----

**Task:** I want to calculate the area of a circle using my Flask app. Use the following code as a starting point

```python
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area
```

For a circle with radius 5, the url should look like this [http://localhost:5000/circle/5/](http://localhost:5000/circle/5/)


----

Solution

```python
@app.route('/circle/<radius>/')
def circle_area(radius):
    radius = int(radius)
    area = 3.14 * (radius ** 2)

    return str(area)
```


----

DO NOT USE `input()` WITH FLASK


---

### Flask: HTML with Jinja

----

Jinja is a template format for using HTML with Python

Flask looks for Jinja templates in the `templates` folder

----

1. Create a Python file called `colours_html.py`

1. Next to the file create a `templates` folder

1. In the `templates` folder create a file called `colour.html`

----

![](images/flask_templates.png)

----

`colours_html.py`

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/colour/')
def show_colour():
    return render_template('colour.html')


app.run(debug=True)
```

----

`colour.html`

```html
<html>
    <body>
        <div style="color: red">
            This text is red
        </div>
    </body>
</html>
```

----

![](images/red_html.png)


----

Similar to string formatting, Jinja templates have arguments

```html
<html>
    <body>
        <div style="color: {{colour}}">
            This text is {{colour}}
        </div>
    </body>
</html>
```

----

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/colour/<colour>/')
def show_colour(colour):
    return render_template('colour.html', colour=colour)


app.run(debug=True)
```

----

**Task:** Create a new html file called `size.html`. When I go to `localhost:5000/size/12/` it should show some text in that font size

```html
<html>
    <body>
        <div style="font-size: {{size}}pt">
            This text is {{size}}
        </div>
    </body>
</html>
```

----

Solution
```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/size/<size>/')
def show_colour(size):
    return render_template('size.html', size=size)


app.run(debug=True)
```

----

You can use for loops to repeat blocks of HTML

```html
<html>
    <body>
    <ul>
    {% for fruit in fruits %}
        <li>fruit</li>
    {% endfor %}
    </ul>
    </body>
</html>
```

----

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/size/<size>/')
def show_fruits(size):
    fruits = ['apple', 'banana', 'pear']

    return render_template('fruit.html', fruits=fruits)


app.run(debug=True)
```

----

----

The course guide has an example of using if statements and css inside Jinja templates

---

### Flask: Forms

----

Covered in the course guide "Getting user generated data from your webpage to Python"

---
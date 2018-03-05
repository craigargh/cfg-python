from flask import Flask, render_template

app = Flask(__name__)


@app.route('/size/<size>/')
def show_colour(size):
    return render_template('size.html', size=size)


app.run(debug=True)

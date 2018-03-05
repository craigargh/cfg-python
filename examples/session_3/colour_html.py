from flask import Flask, render_template

app = Flask(__name__)


@app.route('/colour/<colour>/')
def show_colour(colour):
    return render_template('colour.html', colour=colour)


app.run(debug=True)

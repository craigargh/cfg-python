from flask import Flask, render_template

app = Flask(__name__)


@app.route('/colour/')
def show_colour():
    return render_template('colour_red.html')


app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/dogs/')
def get_dogs():
    # This should return 'Sheep Dog, German Sherphed, Shiba Inu'
    # However it only returns 'Sheep Dog, '
    # Change the code to correct the output

    dogs = ['Sheep Dog', 'German Sherphed', 'Shiba Inu']

    return_value = ''

    for dog in dogs:
        return_value = return_value + dog + ', '

        return return_value


app.run(debug=True)

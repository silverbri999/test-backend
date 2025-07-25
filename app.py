# app.py

from flask_cors import CORS
from flask import Flask
from flask import request 


app = Flask(__name__)
CORS(app)

# Define a route for the homepage "/"
@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/square/<int:number>')
def square(number):
    result = number * number
    return f"The square of {number} is {result}"

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import math
import os  # <-- import os to access environment variables

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/square/<int:number>')
def square(number):
    return jsonify({'result': number * number})

@app.route('/sin/<float:number>')
def sin(number):
    return jsonify({'result': math.sin(math.radians(number))})

@app.route('/cos/<float:number>')
def cos(number):
    return jsonify({'result': math.cos(math.radians(number))})

@app.route('/tan/<float:number>')
def tan(number):
    return jsonify({'result': math.tan(math.radians(number))})

@app.route('/sqrt/<float:number>')
def sqrt(number):
    return jsonify({'result': math.sqrt(number)})

if __name__ == '__main__':
    # Get port from environment variable (Render sets this), default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run the app on all network interfaces on the specified port
    app.run(host='0.0.0.0', port=port, debug=True)

# app.py
from flask import Flask, jsonify

app = Flask(__name__)

#@app.route('/')
#def home():
    #return jsonify(message="Hello level 400 FET, Quality Assurance!")

@app.route('/error')
def trigger_error():
    # This will raise an exception, causing a 500 error
    raise Exception("This is a deliberate error for testing purposes.")

if __name__ == '__main__':
    app.run(debug=True)
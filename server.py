from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/messages')
def messages():
    return {
        "messages": [
            {"text": "Hello", "user": "Nick", "timestamp": "2020-01-01T20:00:00Z"},
            {"text": "Hi", "user": "Jane" , "timestamp": "2020-01-01T00:00:00Z"},
            {"text": "How are you?", "user": "Jane" , "timestamp": "2020-01-01T00:00:00Z"}
        ]
    }
    

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My First Flask API!"

@app.route('/api/user')
def get_user():
    user = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
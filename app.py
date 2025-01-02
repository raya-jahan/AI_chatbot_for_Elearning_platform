from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import generate_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the AI Chatbot for E-learning platform!"


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return "Please use POST to send data to this endpoint."
    elif request.method == 'POST':
        data = request.get_json()
        prompt = data.get('prompt', '')
        response = generate_response(prompt)
        return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)

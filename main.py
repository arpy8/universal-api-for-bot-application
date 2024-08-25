import os
import requests
from flask import Flask, request, jsonify, abort

# CONSTANTS
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
DC_TOKEN = os.environ.get('DC_TOKEN')

app = Flask(__name__)

substitution_mapping = {
    'S': 'A', 'h': 'B', 'E': 'C', '0': 'D', 'd': 'E', 'M': 'F', '4': 'G',
    '_': 'H', 'K': 'I', '6': 'J', 'c': 'K', 'Q': 'L', 'N': 'M', 'B': 'N',
    'y': 'O', 'x': 'P', 'o': 'Q', 'U': 'R', 'Y': 'S', '3': 'T', '2': 'U',
    'a': 'V', 'J': 'W', 'K': 'X', 'g': 'Y', 'I': 'Z', 'e': '0', 'f': '1',
    '3': '2', 'Q': '3', '2': '4', 'H': '5', 'a': '6', 'G': '7', 't': '8',
    'Z': '9', 'h': '!',
}

def decode_token(obfuscated_token):
    reverse_mapping = {value: key for key, value in substitution_mapping.items()}
    decoded_token = ''.join(reverse_mapping.get(char, char) for char in obfuscated_token)
    return decoded_token

@app.before_request     
def check_auth():
    incoming_token = request.headers.get('Authorization')
    
    if not incoming_token:
        abort(401, 'Unauthorized access >:(')

    decoded_token = decode_token(incoming_token)

    if decoded_token != AUTH_TOKEN:
        abort(401, 'Unauthorized access >:(')

@app.route("/")
def index():
    return jsonify({"NOTE": "RAAAAAAHHHHHHHHHH!"})

@app.route("/data", methods=["POST"])
def send_data():
    try:
        channel_id = request.json.get("id")
        message = request.json.get("message")
        
        response = requests.post(
            url=f'https://discord.com/api/v10/channels/{str(channel_id)}/messages', 
            headers={
                'Authorization': f'Bot {DC_TOKEN}',
                'Content-Type': 'application/json',
            },
            json={
                'content': message,
            }
        )

        if response.status_code != 200:
                return jsonify({"error": "Error sending message"}), 500
        
    except Exception as e:
        print("Error sending data:", str(e))
        return jsonify({"error": "Error sending data"}), 500
    
if __name__ == "__main__":
    app.run(debug=True)

import os
import requests
from flask import Flask, request, jsonify, abort

# CONSTANTS
TOKEN = os.environ.get('DD_TOKEN')
DD_TOKEN = os.environ.get('DD_AUTH_TOKEN')

app = Flask(__name__)

substitution_mapping = {
    'S': 'अ', 'h': 'भ', 'E': 'च', '0': 'ड', 'd': 'ई', 'M': 'फ', '4': 'ग',
    '_': 'ह', 'K': 'इ', '6': 'ज', 'c': 'क', 'Q': 'ल', 'N': 'म', 'B': 'न',
    'y': 'ओ', 'x': 'प', 'o': 'क', 'U': 'र', 'Y': 'स', '3': 'त', '2': 'उ',
    'a': 'व', 'J': 'व', 'K': 'क्ष', 'g': 'य', 'I': 'श', 'e': '०', 'f': '१',
    '3': '२', 'Q': '३', '2': '४', 'H': '५', 'a': '६', 'G': '७', 't': '८',
    'Z': '९', 'h': '!',
}

@app.before_request
def check_auth():
    token = request.headers.get('Authorization')
    reverse_mapping = {value: key for key, value in substitution_mapping.items()}
    decoded_token = ''.join(reverse_mapping.get(char, char) for char in token)

    if decoded_token != DD_TOKEN:
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
                'Authorization': f'Bot {TOKEN}',
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
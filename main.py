import os
import requests
from flask import Flask, request, jsonify, abort

# CONSTANTS
TOKEN = os.environ.get('DD_TOKEN')
DD_TOKEN = os.environ.get('DD_AUTH_TOKEN')

headers={
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json',
}

app = Flask(__name__)

@app.before_request
def check_auth():
    token = request.headers.get('Authorization')
    if token != DD_TOKEN:
        abort(401, 'Unauthorized access >:(')

@app.route("/")
def index():
    return jsonify({"NOTE": "RAAAAAAHHHHHHHHHH!"})

def post_message_to_server(channel_id, message):
    try:
        api_url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
        message_data = {
            "content": message,
        }
        response = requests.post(api_url, json=message_data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print("Error sending message:", str(e))
        
@app.route("/data", methods=["POST"])
def send_data():
    try:
        if request.method == "POST":
            channel_id = request.json.get("id")
            message = request.json.get("message")
            
            post_message_to_server(channel_id, message)
            
            return jsonify({"status": "ok"})
        
    except Exception as e:
        print("Error sending data:", str(e))
        return jsonify({"error": "Error sending data"}), 500
    
if __name__ == "__main__":
    app.run()
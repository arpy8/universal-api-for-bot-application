import os
import requests

AUTH_TOKEN = os.environ["AUTH_TOKEN"]

def main():
    response = requests.get(
        url="https://universal-api.onrender.com/", 
        headers={
            "Authorization": AUTH_TOKEN
        }
    )
    if response.status_code == 200:
        try:
            note = response.json()["NOTE"]
            print(note)
        except requests.exceptions.JSONDecodeError:
            print("Error: Unable to decode JSON from the response.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()
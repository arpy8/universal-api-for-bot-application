import requests

AUTH_TOKEN = "ShE0dM4_K6KcQNBhyxoUY33aJKgIef3KQ2HaGtZ2hysUc825"

reverse_mapping = {value: key for key, value in substitution_mapping.items()}
decoded_token = ''.join(reverse_mapping.get(char, char) for char in AUTH_TOKEN)
decoded_token_bytes = decoded_token.encode('utf-8')
print(decoded_token_bytes)

def main():
    response = requests.get(
        url="https://universal-api.onrender.com/", 
        headers={
            "Authorization": AUTH_TOKEN.encode("utf-8")
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
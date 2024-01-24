import requests

AUTH_TOKEN = "अ!चडईफगहक्षजक्षक३मन!ओपकरस२२६वक्षयश०१२क्ष३४५६७८९४!ओsरक8४5"
substitution_mapping = {
    'S': 'अ', 'h': 'भ', 'E': 'च', '0': 'ड', 'd': 'ई', 'M': 'फ', '4': 'ग',
    '_': 'ह', 'K': 'इ', '6': 'ज', 'c': 'क', 'Q': 'ल', 'N': 'म', 'B': 'न',
    'y': 'ओ', 'x': 'प', 'o': 'क', 'U': 'र', 'Y': 'स', '3': 'त', '2': 'उ',
    'a': 'व', 'J': 'व', 'K': 'क्ष', 'g': 'य', 'I': 'श', 'e': '०', 'f': '१',
    '3': '२', 'Q': '३', '2': '४', 'H': '५', 'a': '६', 'G': '७', 't': '८',
    'Z': '९', 'h': '!',
}

reverse_mapping = {value: key for key, value in substitution_mapping.items()}
decoded_token = ''.join(reverse_mapping.get(char, char) for char in AUTH_TOKEN)
decoded_token_bytes = decoded_token.encode('utf-8')
print(decoded_token_bytes)

def main():
    response = requests.get(
        # url="https://universal-api.onrender.com/", 
        url="http://127.0.0.1:5000/",
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
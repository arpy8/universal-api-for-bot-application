import os, requests

def main():
    print(
        requests.get(
            url="https://universal-api.onrender.com/", 
            headers = {
                "Authorization": os.environ["AUTH_TOKEN"].encode("utf-8")
            }
        ).json()["NOTE"]
    )
    
if __name__ == "__main__":
    main()
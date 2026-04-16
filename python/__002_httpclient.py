import requests

def get_advice():
    # Calling a public API
    response = requests.get("https://api.adviceslip.com/advice")
    
    if response.status_code == 200:
        # Parsing the JSON data
        data = response.json()
        advice = data['slip']['advice']
        print(f"\n\U0001f4a1 Modern Wisdom: {advice}\n")
    else:
        print("Failed to get advice. Check your connection!")

if __name__ == "__main__":
    get_advice()


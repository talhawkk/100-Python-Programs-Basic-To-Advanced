import requests

def shorten_url_bitly(long_url, api_key):
    """Shortens a URL using the Bitly API."""
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url
    }

    response = requests.post(endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get("link")
    else:
        return f"Error: {response.json().get('message')}"

long_url = input("Enter the long URL to shorten: ")
api_key = "apni laga na bhai"  
short_url = shorten_url_bitly(long_url, api_key)

print("Short URL:", short_url)

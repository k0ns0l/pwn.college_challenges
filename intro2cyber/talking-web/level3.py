#!/usr/bin/python3
import requests
url = 'http://127.0.0.1'
try:
    response = requests.get(url)
    response.raise_for_status()

    # Print the content of the page
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

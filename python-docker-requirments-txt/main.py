import requests

url = 'https://checkip.amazonaws.com'

response = requests.get(url)

if response.status_code == 200:
    print(f"Response received successfully from {url}")
    print(f"Response content:\n{response.text.strip()}")
else:
    print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")

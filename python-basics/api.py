# How to connect to an API using Python

# module for working with APIs
# if not installed,
# install it with 'apt install python3-requests' for debian based linux distros
import requests

# API endpoint to get a random insult
# You can change the language with `lang=ru` (Russian) or other supported languages
# Set `type=json` to get a JSON response or `type=text` for plain text
base_url = "https://evilinsult.com/generate_insult.php?lang=en&type=text"

def get_insult():
  # get response from (url) and save it in 'response' variable
  response = requests.get(base_url)

  if response.status_code == 200:
    # For JSON response, uncomment the lines below:
    # response = response.json()
    # print(response['insult'])

     # For plain text response
    response = response.text
    print(response)
  else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

get_insult()
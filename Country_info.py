import requests
import json

#sending and recieving api request
response = requests.get("https://restcountries.com/v3.1/name/norway?fields=name")
print(response.status_code)

FilteredData = response.json()

print(FilteredData)
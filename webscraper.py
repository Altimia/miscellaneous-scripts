import requests
from bs4 import BeautifulSoup
import re

url = 'Enter your URL here'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Use a regular expression to find strings of exactly 40 hexadecimal characters
hex_strings = re.findall(r'[0-9a-fA-F]{40}', soup.text)

with open('hex_strings.txt', 'w') as f:
    for string in hex_strings:
        f.write(f'{string}\n')
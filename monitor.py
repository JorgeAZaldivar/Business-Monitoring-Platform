import requests     ## imports the requests python library 
url = "https://example.com"     ## Variable named url contains a string
response = requests.get(url)    ##requests.get(url) tells the requests library: Send an HTTP GET request to the address stored in url.
print(response.status_code)
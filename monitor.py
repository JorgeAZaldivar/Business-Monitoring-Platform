# This monitor now catches when a server is UP or has a Problem, HTTP Problems, DNS Failures, Connection Problems, and Timeout errors

import requests     ## imports the requests python library 
urls = ["https://example.com",
      "https://google.com",
      "https://httpstat.us/404"]  ## Variable named url is assigned to a value that contains a string

for url in urls:
    print(f"\nChecking: {url}")  ## Prints the string "Checking: " followed by the value of the variable url
    
    try:
        response = requests.get(url, timeout = 5)  ## Variable response assigned to requests.get(url), uses the library(requests) I imported,
        # .get() is a function provided by that library for making an HTTP GET request, url is the variable containing the website address
        #essentially means: Send an HTTP GET request to https://example.com.   5 second timeout to avoid waiting too long for a server response.

        print(f"HTTP Status: {response.status_code}") #response contains contains info returned by the server, .status_code asks what HTTP status code did the server return?
        response_time = response.elapsed.total_seconds()  ##calculates the elapsed time for the request in seconds

        if 200 <= response.status_code < 300: #if the status code is greater than or equal to 200 AND less than 300, means SUCCESS, print the statement below
                print("Website Status: UP")  ## ## Prints UP if the website is up and running
        else:
                print("Website Status: Problem")  ## Prints Problem if the website is not up and running

        print(f"Response Time: {response_time:.3f} seconds")  ## ## Prints the elapsed time for the request in seconds
        #.3f formats the response_time to 3 decimal places

    except requests.exceptions.RequestException as error:  ## Catches request-related exceptions that may occur during the request and assigns it to a variable named error
        print("Website status: Problem")
        print(f"Error: {error}")  ## Prints the error message if an exception occurs
        # except handles network/request failure

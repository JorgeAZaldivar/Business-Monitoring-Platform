# This monitor now catches when a server is UP or has a Problem, HTTP Problems, DNS Failures, Connection Problems, and Timeout errors

import requests     ## imports the requests python library 
from datetime import datetime ## imports the datetime library to get the current date and time(gives access to the datetime class))
import csv # Imports Python's CSV module so the program can read/write CSV files

urls = ["https://example.com",

      "https://google.com",

      "https://httpstat.us/404",
      ]  ## Variable named url is assigned to a value that contains a string

file = open("results.csv", "a", newline="") #File assigneed to open a file named results.csv in append moode("a") and store access to that  file in the variable file. newline="" ensures that new lines are handled correctly when writing to the CSV file.
writer = csv.writer(file) # Create a CSV writer object that knows it should write data into file. (Append mode means: it keeps the existing contents and adds new data at the end.)
if file.tell() == 0:    #File.tell() tells me the current position in the File, if its = to 0 that means the file is empty, so python executes the values following.
    writer.writerow([  # == 0 means if thi CSV file is currently empty, if yes, then it writes the headers 
            "Timestamp",
            "URL",
            "Status",
            "HTTP Status",
            "Response Time",
            "Error"
            ])

for url in urls:
    print(f"\nChecking: {url}")  ## Prints the string "Checking: " followed by the value of the variable url
    timestamp = datetime.now() ## Timestamp is assigneed to datetime.now() to for the current date and time
    print(f"Timestamp: {timestamp}")  ## Prints the string "Timestamp: " followed by the value of the variable timestamp
    
    try:
        response = requests.get(url, timeout = 5)  ## Variable response assigned to requests.get(url), uses the library(requests) I imported,
        # .get() is a function provided by that library for making an HTTP GET request, url is the variable containing the website address
        #essentially means: Send an HTTP GET request to https://example.com.   5 second timeout to avoid waiting too long for a server response.

        print(f"HTTP Status: {response.status_code}") #response contains contains info returned by the server, .status_code asks what HTTP status code did the server return?
        response_time = response.elapsed.total_seconds()  ##calculates the elapsed time for the request in seconds

        if 200 <= response.status_code < 300: #if the status code is greater than or equal to 200 AND less than 300, means SUCCESS, print the statement below
                status = "UP" # Assigns the string 'UP' to the variable status 
                print("Website Status: UP")  ## ## Prints UP if the website is up and running
        else:
                status = "Problem" # Assigns the string 'Problem' to the variable status
                print("Website Status: Problem")  ## Prints Problem if the website is not up and running

        print(f"Response Time: {response_time:.3f} seconds")  ## ## Prints the elapsed time for the request in seconds
        #.3f formats the response_time to 3 decimal places
        writer.writerow([
            timestamp,
            url,
            status,
            response.status_code,
            f"{response_time:.3f}",
            "None"
            ])  #This writes one row of data containing these 5 values into the CSV File.




    except requests.exceptions.Timeout as error:
        print ("Website Status: Problem")
        print(f"Error Type: Timeout")

        writer.writerow([
        timestamp,
        url,
        "Problem",
        "N/A",
        "N/A",
        "Timeout"
        ]) ## Writes a row of data into the CSV file indicating a timeout error occurred


    except requests.exceptions.ConnectionError as error:
        print("Website Status: Problem")
        print("Error Type: Connection Error")

        writer.writerow([
        timestamp,
        url,
        "Problem",
        "N/A",
        "N/A",
        "Connection Error"
        ]) ## Writes a row of data into the CSV file indicating a connection error occurred


    except requests.exceptions.RequestException as error:  ## Catches request-related exceptions that may occur during the request and assigns it to a variable named error
        print("Website status: Problem")
        print(f"Error: {error}")  ## Prints the error message if an exception occurs
        # except handles network/request failure
        writer.writerow([
            timestamp, 
            url, 
            "Problem",
            "N/A",
            "N/A",
            error
            ])



#!/bin/bash
# Script description: Sends a GET request to a URL and displays the body of the response for a 200 status code.

# Usage: ./get_response_body.sh http://localhost:5000
response=$(curl -s -w "%{http_code}" "$1")

# Check if the response code is 200 (OK) and display the body
if [ "$response" -eq 200 ]; then
    curl -s "$1"
else
    echo "Error: Received non-200 status code ($response)"
fi


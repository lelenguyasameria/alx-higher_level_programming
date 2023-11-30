#!/bin/bash
# Script description: Sends a POST request to a URL with custom variables and displays the body of the response.

# Usage: ./post_response_body.sh http://localhost:5000
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"


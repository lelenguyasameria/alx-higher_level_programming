#!/bin/bash
# Script description: Sends a request to a URL and displays the size of the response body in bytes.

# Usage: ./get_response_size.sh http://localhost:5000
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n' && echo " bytes"


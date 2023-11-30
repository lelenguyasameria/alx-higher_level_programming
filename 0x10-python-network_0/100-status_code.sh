#!/bin/bash
# Script description: Sends a request to a URL and displays only the status code of the response.

# Usage: ./get_status_code.sh http://localhost:5000
curl -s -o /dev/null -w "%{http_code}\n" "$1"


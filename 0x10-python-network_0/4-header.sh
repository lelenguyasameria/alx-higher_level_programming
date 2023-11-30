#!/bin/bash
# Script description: Sends a GET request to a URL with a custom header and displays the body of the response.

# Usage: ./get_response_body_with_header.sh http://localhost:5000
curl -s -H "X-School-User-Id: 98" "$1"


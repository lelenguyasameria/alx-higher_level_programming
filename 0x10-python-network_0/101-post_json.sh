#!/bin/bash
# Script description: Sends a JSON POST request to a URL with the contents of a file in the body.

# Usage: ./post_json_request.sh http://localhost:5000 filename.json
url="$1"
filename="$2"

if [ -z "$url" ] || [ -z "$filename" ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

curl -s -X POST -H "Content-Type: application/json" -d "@$filename" "$url"


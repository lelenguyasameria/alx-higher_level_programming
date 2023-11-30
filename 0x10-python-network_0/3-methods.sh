#!/bin/bash
# Script description: Displays all HTTP methods the server will accept for a given URL.

# Usage: ./get_http_methods.sh http://localhost:5000
curl -sI -X OPTIONS "$1" | grep -i "allow" | awk '{print $2}'


#!/bin/bash
# Script description: Makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with a message.

# Usage: ./catch_me.sh
curl -s -L -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me


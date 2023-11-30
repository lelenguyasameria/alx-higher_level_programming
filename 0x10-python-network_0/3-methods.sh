#!/bin/bash
# Script description: Displays all HTTP methods the server will accept for a given URL.
curl -sI "$1" | grep 'Allow' | cut -d " " -f2-

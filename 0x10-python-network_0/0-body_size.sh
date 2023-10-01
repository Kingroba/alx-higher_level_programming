#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Error: No URL provided."
    exit 1
fi

# Sends a request to the provided URL and displays the size of the response body in bytes
curl -s "$1" | wc -c


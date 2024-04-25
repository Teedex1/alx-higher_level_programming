#!/bin/bash
# send a request to a URL with curl, and displays the size
curl -s "$1" | wc -c

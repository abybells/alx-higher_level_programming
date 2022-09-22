#!/bin/bash
# Script that sends a GET request to a given URL with a header variable and displays body of response
curl -sH "X-School-User-Id: 98" "$1"

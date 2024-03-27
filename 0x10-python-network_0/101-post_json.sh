#!/bin/bash
# JSON POST request to a URL passed as the firs
curl -sH "Content-Type: application/json" --data "$(cat "$2")" "$1"

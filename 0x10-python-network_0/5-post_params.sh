#!/bin/bash
# akes in a URL, sends a POST request to the passed UR
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

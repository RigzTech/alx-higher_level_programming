#!/usr/bin/python3
"""
script to send post request to passed url with email and display
body as response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    response = requests.post(sys.argv[1], data=email)
    print(response.text)

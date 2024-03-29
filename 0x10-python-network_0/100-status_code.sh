#!/bin/bash
#JSON POST request to a URL passed as the first
curl -so dev/null -w "%{http_code}" "$1"

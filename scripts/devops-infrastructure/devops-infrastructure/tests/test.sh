#!/bin/bash

URL=http://localhost
EXPECTED_STATUS=200
EXPECTED_BODY="<title>Welcome to nginx!</title>"

status=$(curl -s -o /dev/null -w "%{http_code}" $URL)
body=$(curl -s $URL)

if [[ "$status" -ne "$EXPECTED_STATUS" ]]; then
    echo "FAILED: Expected status $EXPECTED_STATUS but got $status"
    exit 1
fi

if [[ "$body" != *"$EXPECTED_BODY"* ]]; then
    echo "FAILED: Expected body to contain '$EXPECTED_BODY'"
    exit 1
fi

echo "SUCCESS"
#!/bin/bash
# the script send a GET request and display only the body of status code 200 of the response
curl -sL -fail -X GET "$1";

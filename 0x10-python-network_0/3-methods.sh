#!/bin/bash
# display options/methods server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

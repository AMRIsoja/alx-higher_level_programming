#!/bin/bash
# display options/methods server will accept
curl -sX OPTIONS -I "$1"

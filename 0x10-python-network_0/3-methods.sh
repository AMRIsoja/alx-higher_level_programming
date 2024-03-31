#!/bin/bash
# display options/methods server will accept
curl -X OPTIONS -I "$1"

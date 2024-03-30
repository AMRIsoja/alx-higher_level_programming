#!/bin/bash
response_body=$(curl -s -w "%{size_download}" $1)
echo $response_body

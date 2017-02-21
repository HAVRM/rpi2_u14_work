#!/bin/sh -xv

echo "Content-Type: video/mp4"
echo "Content-Length: $LENGTH"
echo ""
FILE="FAIRYTAIL_179.mp4"
LENGTH=$(wc -c $FILE | awk '{print $1}')
cat $FILE

#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DATA=`date '+%m%d_%H%M_%S'`
echo "<html><body>${DATA}</body></html>"
sleep 5s
DATA=`date '+%m%d_%H%M_%S'`
echo "<html><body><br>${DATA}</body></html>"


#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DATA=`date '+%m%d_%H%M_%S'`
echo "<html><body>${DATA}"
sleep 5s
DATA=`date '+%m%d_%H%M_%S'`
echo "<br>${DATA}</body></html>"


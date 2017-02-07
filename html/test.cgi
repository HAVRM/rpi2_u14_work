#!/bin/sh -xv

DATA=`date '+%m%d_%H%M_%S'`
echo "Content-Type: text/html"
echo ""
echo "<html><body>${DATA}</body></html>"
#sleep 5s
#DATA=`date '+%m%d_%H%M_%S'`
#echo "<html><body>${DATA}</body></html>"

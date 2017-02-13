#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DATA=`date '+%m%d_%H%M_%S'`
MEM=`cat /proc/meminfo | tr '\n' ' '`
echo "<html><body>${DATA}<br>${MEM[@]}</body></html>"


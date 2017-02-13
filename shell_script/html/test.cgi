#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DATA=`date '+%m%d_%H%M_%S'`
MEM=`cat /proc/meminfo | tr -s ' '`
MEM=`echo ${MEM} | sed -e s/\n/<br>/g`
echo "<html><body>${DATA}<br>${MEM}</body></html>"


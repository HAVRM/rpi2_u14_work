#!/bin/sh -xv
echo "Content-Type: text/html"
echo ""
DATA=`date '+%m%d_%H%M_%S'`
echo "<html><body>test${DATA}</body></html>"


#!/bin/sh -xv
echo "Content-Type: text/html"
echo ""
DATE=`date '+%m%d_%H%M_%S'`
echo "<html><body>test${DATE}</body></html>"


#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DF=`df -BM | tr '\n' '_'`
DF=`echo ${DF} | sed -e "s/Mounted\ on/Mounted-on/g"`
DF=`echo ${DF} | sed -e "s/_/\<\/td\>\<\/tr\>\<tr\>\<td\>/g"`
DF=`echo ${DF} | sed -e "s/\ /\<\/td\>\<td\>/g"`
echo "<html><body><table border=0><tr><td>${DF}</td></tr></table></body></html>"

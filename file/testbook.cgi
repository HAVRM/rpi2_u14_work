#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
DATA=`echo "havrm" | sudo -S sh cutbook.cgi`
#mkdir temp_kusen_01
#cp kusen_01.pdf temp_kusen_01/kusen_01.pdf
#cd temp_kusen_01
#pdftk kusen_01.pdf burst kusen_01_part_%04d.pdf
echo "<html><body>${PLACEcutbook2}</body></html>"
echo "<html><body><p><object data=\"file/temp_kusen_01/kusen_01_part_005.pdf\" type=\"application/pdf\" width=\"1280\" height=\"960\"></body></html>"


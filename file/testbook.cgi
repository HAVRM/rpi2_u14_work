#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
mkdir temp_kusen_01
cp kusen_01.pdf temp_kusen_01
cd temp_kusen_01
pdftk kusen_01.pdf burst kusen_01_part_%04d.pdf
echo "<html><body><p><object data=\"kusen_01_part_005.pdf\" type=\"application/pdf\" width=\"1280\" height=\"960\"></body></html>"


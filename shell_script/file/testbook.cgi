#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
mkdir -m 777 temp_kusen_01
cp kusen_01.pdf temp_kusen_01/kusen_01.pdf
cd temp_kusen_01
pdftk kusen_01.pdf burst output kusen_01_part_%04d.pdf
echo "<html><body><p><object data=\"temp_kusen_01/kusen_01_part_0005.pdf\" type=\"application/pdf\" width=\"1280\" height=\"960\"></object></p></body></html>"


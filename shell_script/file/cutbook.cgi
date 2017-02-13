#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
PLACEcutbook=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "説明"
		echo ". cutbook.sh"
		return 0
	fi
fi
#write progrum
#cd ~/file
mkdir temp_kusen_01
cp kusen_01.pdf temp_kusen_01/kusen_01.pdf
cd temp_kusen_01
pdftk kusen_01.pdf burst output kusen_01_part_%04d.pdf
cd $PLACEcutbook
. testbook.cgi

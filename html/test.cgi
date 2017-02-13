#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
#DATA=`date '+%m%d_%H%M_%S'`
#MEM=`cat /proc/meminfo | tr -s ' '`
#MEM=`echo "${MEM}" | sed 's/\ kB/\ kB\<br\>/g'`
#echo "<html><body>${DATA}<br>${MEM}</body></html>"
MEM=(`cat /proc/meminfo | tr -s ' '`)
I=0
SUBI=1
MTT=0
MFR=0
for arg in ${MEM[@]}
do
	if [ ${arg} = "MemTotal:" ]
	then
		MTT=${MEM[$SUBI]}
		MTT=`expr ${MTT} / 100000`
	elif [ ${arg} = "MemFree:" ]
	then
		MFR=${MEM[$SUBI]}
		MFR=`expr ${MFR} / 100000`
	fi
	I=`expr ${I} + 1`
	SUBI=`expr ${SUBI} + 1`
done
echo "${MTT}/${MFR}"

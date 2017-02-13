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
		MTT=`expr ${MTT} / 1000`
	elif [ ${arg} = "MemFree:" ]
	then
		MFR=${MEM[$SUBI]}
		MFR=`expr ${MFR} / 1000`
	fi
	I=`expr ${I} + 1`
	SUBI=`expr ${SUBI} + 1`
done
MTT=`expr ${MTT} - ${MFR}`
if [ ${MTT} = 0 ]
then
	MTT=`expr ${MTT} + 1`
	MFR=`expr ${MFR} - 1`
elif [ ${MFR} = 0 ]
then
	MTT=`expr ${MTT} - 1`
	MFR=`expr ${MFR} + 1`
fi
echo "<html><body>${MTT}/${MFR}</body></html>"

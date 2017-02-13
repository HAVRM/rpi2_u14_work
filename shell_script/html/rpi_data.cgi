#!/bin/sh -xv

echo "Content-Type: text/html"
echo ""
total=$(free -m | awk '/Mem:/{print $2;}')
free=$(free -m | awk '/-\/+/{print $4;}')
total=`expr $total - $free`
temp=`cat /sys/class/thermal/thermal_zone0/temp`
temp1=`expr $temp / 1000`
temp=`expr $temp % 1000`
temp="${temp1}.${temp}"
intr=`vmstat | awk 'NR==3 {print $11}'` #in
cpu=`top -b -n 1 | awk 'NR==3 {print $2"/"$4"/"$8"/"$10}'` #us,sy,id,wa
cpu=`echo ${cpu} | sed -e 's/0\.//g'`
cpu=`echo ${cpu} | sed -e 's/\.//g'`
echo "<html><body>/${total}/${free}/${temp}/${intr}/${cpu}</body></html>"

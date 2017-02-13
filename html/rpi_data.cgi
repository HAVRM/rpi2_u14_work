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
cpu=`vmstat | awk 'NR==3 {print $11"/"$13"/"$14"/"$15"/"$16}'` #in,us,sy,id,wa
echo "<html><body>/${total}/${free}/${temp}/${cpu}</body></html>"

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
cpu=`top -b -n 1 | awk 'NR==3 {print $2"_"$4"_"$6"_"$8"_"$10}'` #us,sy,ni,id,wa
data=`date +%N | cut -c -2`
data=`date +%Y/%m/%d\&nbsp\;%H:%M:%S.`${data}
time=`date +%s.%N`
net=`cat /proc/net/dev | awk '/wlan0:/{print $10"_"$2}'`
echo "<html><body>_${total}_${free}_${temp}_${intr}_${cpu}_${data}_${time}_${net}</body></html>"

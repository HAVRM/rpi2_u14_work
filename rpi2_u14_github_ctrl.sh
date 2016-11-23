#!/bin/bash

PASS="havrm"
PLACE=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "自分のgithubに関連することのコントロール"
		echo ". github_ctrl.sh (pull)"
		return 0
	fi
fi
COM=$1
NCOM=$#
DATA=`date '+%m%d_%H%M_%S'`
. move_all_sh.sh hiro2git hiroki.mine.0614.163 hiroki Buffalo-G-1CC0 kyrnnknhkwxvm havrm
cd ~/rpi2_u14_work
if [ ${NCOM} = 1 ]
then
	if [ ${COM} = "pull" ]
	then
		git fetch rpi2_u14_work
		git merge rpi2_u14_work/master
		echo ${PASS} | sudo -S cp -rf apache_html /var/www/html
		cp -rf auto_pdf/auto_get_pdf.sh ~/auto_pdf/auto_get_pdf.sh
		return 0
	fi
fi
git add -A
git commit -m "${DATA}"
git push rpi2_u14_work master
cd $PLACE

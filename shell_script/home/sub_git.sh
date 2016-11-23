#!/bin/bash

PASS="***"
PLACE=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "自分のgithubに関連することのコントロール"
		echo ". sub_git.sh (pull)"
		return 0
	fi
fi
COM=$1
NCOM=$#
DATA=`date '+%m%d_%H%M_%S'`
. move_all_sh.sh *** *** *** *** *** *** ***
cd ~/rpi2_u14_work
if [ ${NCOM} = 1 ]
then
	if [ ${COM} = "pull" ]
	then
		git fetch rpi2_u14_work
		git merge rpi2_u14_work/master
		return 0
	fi
fi
git add -A apache_html
git add -A auto_pdf
git add -A shell_script
git commit -m "${DATA}"
git push rpi2_u14_work master
cd $PLACE

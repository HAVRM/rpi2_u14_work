#!/bin/bash

PLACE=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "自分のgithubに関連することのコントロール"
		echo ". rpi2_u14_github_ctrl.sh"
		return 0
	fi
fi
DATA=`date '+%m%d_%H%M_%S'`
. move_all_sh.sh hiro2git hiroki.mine.0614.163 hiroki Buffalo-G-1CC0 kyrnnknhkwxvm havrm
cd ~/rpi2_u14_work
git add -A
git commit -m "${DATA}"
git push work master
cd $PLACE

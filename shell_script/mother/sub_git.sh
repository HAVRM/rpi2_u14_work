#!/bin/bash

PLACE=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "rpi2のgithubに関連することのコントロール。母艦用"
		echo ". sub_git.sh (オプション)"
		echo "        pull : fetch & merge"
		echo "        push : add & push"
		return 0
	fi
fi
COM=$1
NCOM=$#
DATA=`date '+%m%d_%H%M_%S'`
cd ~/rpi2_u14_work
if [ ${NCOM} = 1 ]
then
	if [ ${COM} = "pull" ]
	then
		git fetch rpi2_u14_work
		git merge rpi2_u14_work/mother
	elif [ ${COM} = "push" ]
	then
		git fetch rpi2_u14_work
		git merge rpi2_u14_work/mother
		. sub_move.sh ***
		git add -A
		git commit -m "${DATA}"
		git push rpi2_u14_work mother
	fi
fi
cd $PLACE

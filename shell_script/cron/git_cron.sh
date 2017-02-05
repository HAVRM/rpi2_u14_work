#!/bin/bash

PLACEgit_cron=`pwd`
if [ $# != 0 ]
then
	if [ $1 = "-h" ]
	then
		echo "rpi2用git関連cron操作。\"chmod a+x\"の実行が必要"
		echo ". git_cron.sh"
		return 0
	fi
fi
#write progrum
cd ~/rpi2_u14_work
DATA=(`git branch --list`)
DATA2=(`git branch --list --color`)
FIL=(`ls`)
declare -i I
I=0
for arg in ${DATA[@]}
do
	for arg2 in ${FIL[@]}
	do
		if [ $arg = $arg2 ]
		then
			break
		fi
	done
	if [ $arg != $arg2 ]
	then
		arg2="_"${arg}"[m"
		arg3="_"${DATA2[$I]}
		if [ $arg2 != $arg3 ]
		then
			BCH=$arg
			break
		fi
	fi
	I=`expr $I + 1`
done
if [ BCH = "master" ]
then
	cd ~
	. rpi2_u14_github_ctrl.sh
	cd ~/rpi2_u14_work
fi
git fetch rpi2_u14_work
git checkout mother
git merge rpi2_u14_work/mother
FNAME=(`find ./ -name "*.*"`)
for arg in ${FNAME[@]}
do
	if [ `echo ${arg} | grep -i ".git"` ]
	then
		:
	elif [ `echo ${arg} | grep -i "./shell_script/"` ]
	then
		arg=${arg#*/}
		arg2=${arg#*/}
		if [ `echo ${arg} | grep -i "home"` ]
		then
			arg2=${arg2#*/}
		fi
		cp -f ${arg} ~/${arg2}
		sed -i -e "s/***/***/g" ~/${arg2}
	fi
done
cd $PLACEgit_cron

echo "***" | sudo -S userdel -r ubuntu
if [ $? = 0 ]
then
	#rm -rf .rm_user_ru14su_sub.sh
	sed -i -e "s/.\ .rm_user_ru14su_sub.sh//" /home/***/.bashrc
fi

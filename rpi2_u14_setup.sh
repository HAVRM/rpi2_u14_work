#!/bin/bash

#インターネット接続状態で実行
#raspberry pi 2 ubuntu14.04用
#下のNAME,PASS,GITNAME,GITMAIL,GITPASSの中を編集するGIT..はgithubにおけるもの
#インストールするものは関数化されていて一番最後のupdate_upgrade以下の行が
#それぞれ何をインストールするかを指定している。インストールしなくていい物は
#それが書かれている先頭に'#'をつければいい。
#例: ros_install->#ros_install

NAME="havrm" #PC username ___@...:~$
PASS="havrm" #PC password
GITNAME="HAVRM" #github username
GITMAIL="hiroki.mine.0614.163@gmail.com" #github mail address
GITPASS="hiro2git" #github password
VNCPASS="***" #tigerVNC password

update_upgrade()
{
echo "---update_upgrade---"
echo $PASS | sudo -S apt-get update | tr '\n' '\r'
echo ""
echo $PASS | sudo -S apt-get -y upgrade | tr '\n' '\r'
}

github_setting()
{
echo "---github_setting---"
cd ~
update_upgrade
mkdir rpi2_u14_work
cd ~/rpi2_u14_work
git init
git remote rm rpi2_u14_work
git remote add rpi2_u14_work https://${GITNAME}:${GITPASS}@github.com/HAVRM/rpi2_u14_work.git
git fetch rpi2_u14_work
git merge rpi2_u14_work/master
git config --global user.name "${GITNAME}"
git config --global user.email "${GITMAIL}"
cp -rf auto_pdf ~/auto_pdf
. rpi2_u14_github_ctrl.sh push
echo "#!/bin/bash

echo $PASS | sudo -S sh -c 'echo \"0 0,6,12,18 * * * . /home/${NAME}/auto_pdf/auto_get_pdf.sh
0 1 * * * ./home/${NAME}/update_upgrade.sh\" >>/var/spool/cron/crontabs/${NAME}'" >.rpi2_u14_setup_sub.sh
. .rpi2_u14_setup_sub.sh
rm -rf .rpi2_u14_setup_sub.sh
cd ~
}

other_install()
{
echo "---other_install---"
cd ~
update_upgrade
echo $PASS | sudo -S apt-get -y install imagemagick rar unrar pdftk git expect ffmpeg
cd ~
}

shell_install()
{
echo "---shell_install---"
cd ~
update_upgrade
rm -rf rm_~_file.sh update_upgrade.sh make_shellscript.sh 1>/dev/null 2>&1
wget https://raw.githubusercontent.com/HAVRM/work/master/shell_script/home/rm_~_file.sh
wget https://raw.githubusercontent.com/HAVRM/work/master/shell_script/home/update_upgrade.sh
wget https://raw.githubusercontent.com/HAVRM/work/master/shell_script/home/make_shellscript.sh
sed -i -e "s/\*\*\*/${PASS}/" ~/update_upgrade.sh
. ~/rm_~_file.sh
}

echo "yor name is ${NAME}, password is ${PASS}"
echo "your github name is ${GITNAME}, mail is ${GITMAIL}, password is ${GITPASS}"
update_upgrade
other_install
github_setting
shell_install
update_upgrade
cd ~

#!/bin/bash
for i in $(cat /home/myCode/users.txt)
	do
		useradd $i
		echo "123456" | passwd --stdin $i
		chage -d 0 $i
	done

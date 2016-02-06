#!/bin/bash

for i in $(cat /home/myCode/users.txt)
	do
		userdel -f -r $i
	done

#!/bin/bash
PROJECT_PATH="/home/ec2-user/sib/backups/1 /home/ec2-user/sib/backups/2 /home/ec2-user/sib/backups/3"
for DIR in $PROJECT_PATH
do
echo "These files in  $DIR will be deleted:"
cd $DIR
ls -tr | head -n -5
ls -tr | head -n -5 | xargs rm
done

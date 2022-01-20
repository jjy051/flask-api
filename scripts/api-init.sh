#!/bin/bash

# setting target api url
if [ -z "$1" ]
then
  echo -e "You missed  target api url argument. \n If you want to set target api url, please type it. \n Otherwise just hit the Enter key.\n [Enter if you want to go through with default api url: 'localhost:5000']"
  read api_url
  if [ -z $api_url ]; then api_url='localhost:5000'; fi
else
  api_url=$1
fi

echo "target api url: $api_url"
sleep 1s
echo "let's go!!!"


# target api url health check
http -v GET $api_url/ping
echo -e  "[API Health Check] \n does it work? \n If you want to go on, hit Enter"
read check


# this is initial data load
http -v POST $api_url/sign-up name=jaeyoung email=jaeyoung@gmail.com password=test1234 profile='ddd'
http -v POST $api_url/sign-up name=aaa email=aaa@gmail.com password=test4321 profile='ddd'
http -v POST $api_url/sign-up name=bbb email=bbb@gmail.com password=bbb1234 profile='ddd'
http -v POST $api_url/sign-up name=ccc email=ccc@gmail.com password=ccc1234 profile='ddd'
http -v POST $api_url/sign-up name=ddd email=ddd@gmail.com password=ddd1234 profile='ddd'
http -v POST $api_url/sign-up name=eee email=eee@gmail.com password=eee1234 profile='ddd'


# this is a first tweet data upload
http -v POST $api_url/tweet id=1 tweet="My First Tweet"
http -v POST $api_url/tweet id=2 tweet="I am aaa"
http -v POST $api_url/tweet id=3 tweet="I am bbb"
http -v POST $api_url/tweet id=4 tweet="I am ccc"
http -v POST $api_url/tweet id=5 tweet="I am ddd"
http -v POST $api_url/tweet id=6 tweet="I am eee"



# see users to check whether initial data upload has done without any problem
# http -v GET $api_url/view-users


# ask whether follow initialization go or not
echo -e "go on [follow initialization]? [yes/no]:"
read word

if [ $word = "no" ]
then
  echo "good bye"
else
  http -v POST $api_url/follow id=1 follow=2
  http -v POST $api_url/follow id=1 follow=3
  http -v POST $api_url/follow id=1 follow=4
  http -v POST $api_url/follow id=2 follow=5
fi


#!/bin/bash

if [ -z $1 ]
then
  echo -e "[Please type flask python app name] \n Otherwise 'app.py' will be runnig by default"
  read flask_app_name
  if [ -z $flask_app_name ]; then flask_app_name='app.py'; fi
else
  flask_app_name=$1
fi
  

FLASK_ENV=development FLASK_APP=$flask_app_name FLASK_DEBUG=1 flask run

nohup python setup.py runserver --host=0.0.0.0 &

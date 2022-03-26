#!/bin/bash
echo "Welcome to the OrderSystem Application. I am here to guide you through the installation"
# Ask if user has python3 version 3.9 installed
if hash python3 ; then
    echo "Python is installed"
else
    echo "Python is not installed. Please install Python to run this application"
    exit 1
fi

if ! python3 -c 'import sys; assert sys.version_info[:2] >= (3,8)' > /dev/null; then 
echo "Python 3.9 is not installed. There may be some compatibility issues"
else echo "Correct Python version is installed" 
fi

echo "installing python3 virtual environment..."
python3 -m venv .venv
echo "Activating Python3 virtual environment..."
source .venv/bin/activate
echo "Exporting needed variables from .venv file..."
pip install -r requirements.txt

if [ -f .env ];then
  set -a
  source .env
  set +a
# export $(grep -v '^#' .env | xargs -d '\n')
#   export $(cat .env | sed 's/#.*//g' | xargs)
fi

while true 
do
  printf 'How would you like to run the application? \n 1. Local Python Testing \n 2. Flask Rest API using Postman \n 3. Docker container using Postman \n'
  read execution_choice
  if [ $execution_choice == "1" ];then
    echo "Running OrderSystem Application locally. Please enter the meal (Ex: Breakfast, Lunch, Dinner) and the order (ex: 1,2,3,4). Press 'Ctrl + C' when you want to exit"
    python local.py
    break
  elif [ $execution_choice == "2" ];then
    echo "Running OrderSystem using Flask locally. Please use Postman and follow instructions in Readme.md on how to use the API"
    flask run
    break
  elif [ $execution_choice == "3" ];then
    echo "Running OrderSystem using a Docker Container. Please use Postman and follow instructions in Readme.md on how to use the API"
    docker image build -t intervieworder . || echo "Please check system has docker installed"
    docker run -it -p 127.0.0.1:5000:5000 -d intervieworder
    break
  else
    echo 'Invalid choice'
  fi
done
## Order System
This project is an OrderSystem that takes an an order and returns the correct order.

### **Table of Contents**
- [Prerequisites for Project](#prequisites)
- [Modules Used and Reason](#modules)
- [Setup Application](#setup-application)
- [Running Application](#running-application)
- [Running pytest](#running-pytest)
- [Logging](#logging)
- [Cleanup](#cleanup)

## Prerequisites for Project
- Python 3.9
- Linux/Mac OS
- Docker (If testing with Docker)
- Postman (If testing with Flask or Docker)
- Kubernetes (maybe)

## Modules Used and Reason

| Module Name | Reason | Install with pip |
| --- | --- |
| [logging](https://www.geeksforgeeks.org/logging-in-python/) | Helps log what is happening in the code for easier debugging | Built-in |
| [json](https://realpython.com/lessons/what-is-json/) | Module that makes it easier to parse json data from string and work with json | Built-in |
| [os](https://www.geeksforgeeks.org/os-module-python-examples/) | Module that makes it easier to insteract with the operating system such as getting the environment variables | Built in |
| [abc](https://www.geeksforgeeks.org/abstract-base-class-abc-in-python/) | Abstract Base Class to allow for creating of abstract methods that could be overwritten | Built in |
| [flask](https://pythonbasics.org/what-is-flask-python/) | Web framework module that assists with routing | pip install Flask |
| [dotenv](https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn) | Module flask can use to load the environment variables from a `.env` file | pip install python-dotenv |
| [pytest](https://docs.pytest.org/en/7.1.x/) | Module that allows for better testing of the application than unittest | pip install pytest |

## Setup Application
### Setup and Run Application With shell script
Ensure Python version 3.9 is installed. Version 3.8 may have compatibility issues

cd into the root of Application Directory. It is the folder where this Readme is located

`chmod +rx setup.sh`

`.setup.sh`

### Manually
Ensure Python version 3.9 is installed. Version 3.8 may have compatibility issues

cd into the root of Application Directory. It is the folder where this Readme is located

Install Python virtual environment
`python3 -m venv .venv`

Activate Python Virtual Environment
`source .venv/bin/activate`

Install Modules needed
`pip install -r requirements.txt`

Export needed environment variables
`set -a`
`source .env`
`set +a`


## Running Application
Once 'How to set up application' steps are done. You could now use the application.

### Locally without Flask
To run locally without using Postman:

cd into the root of Application Directory. It is the folder where this Readme is located

Confirm that you have python version 3.9 installed `python3 --version`

Run `python3 local.py` and follow the steps. For meal, enter a choice of Breakfast, Lunch or Dinner (do not use any quotes). For order, enter the number as 1,2,3,4 (do not use any quotes)

Example below:

![](images/local_run_example.png)

### Locally with Flask
Ensure Postman is installed. Postman can be installed by navigating to the following link `https://www.postman.com/downloads/`

cd into the root of Application Directory. It is the folder where this Readme is located

Run the following command `flask run`

Navigate to Postman

Application will be running on IP: 127.0.0.1 on Port 5000 (127.0.0.1:5000)

For Params:

Enter a key of `meal` with the meal you are interest in as the value

Enter a key or `order` with the order that you are interested in as a value

### Locally with Docker
Ensure Postman is installed. Postman can be installed by navigating to the following link `https://www.postman.com/downloads/`

Ensure Docker is installed. Docker can be installed by navigating to the following link `https://docs.docker.com/get-docker/`

cd into the root of Application Directory. It is the folder where this Readme is located

Run the following commands in your terminal:
`docker image build -t intervieworder .`

`docker run -it -p 127.0.0.1:5000:5000 -d intervieworder`

Save the id that gets returned

Navigate to Postman

Application will be running on IP: 127.0.0.1 on Port 5000 (127.0.0.1:5000)

For Params:

Enter a key of `meal` with the meal you are interest in as the value

Enter a key or `order` with the order that you are interested in as a value


## Running pytest
cd into the root of Application Directory. It is the folder where this Readme is located

Run the following command to set environment variables:

`set -a`
`source .env`
`set +a`

cd into `tests` folder

Run `pytest order_system.py`

## Logging:
Logging is currently default to showing Warning and Errors in the application.
To Change it, set the environment variable LOG_LEVEL to the desired level. Example: `export LOG_LEVEL="INFO"` to see info log messages

## Cleanup:
remove environment variables in the .env
`unset <variable name in .env file>`

If you are using the application in a docker container
`docker stop <container_id that you copied>`
`docker rm <container_id that you copied>`
`docker image rm intervieworder`
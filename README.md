# Flask JWT Rest Starter Application

Inspired by:

https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb

and

```Building Serverless Python Web Services with Zappa```

This starter project is meant as an accelerator to create restful flask application.  It uses JWT tokens for both access and refresh.

This project can work with either Python3.7 or Python3.6.  However, if you need to deploy this starter application on AWS you will need to use Python3.6.

model.py has the UserModel defined as both a 3.7 DataClass or a 3.6 NamedTuple.

## Http-client test file

*rest_test.http* is a http client test file.

*http-client.env.json* defines different environments when running either locally or on AWS.


## Setup

* git clone this repo
* create virtual python environment
* source the python environtment
* pip install -r requirements.txt


## Run

Run ```python main.py```

Open the ```rest_test.http``` file

this is a test script to exercise the endpoints.  When running a test case, you will be prompted for the environment.


## Zappa

if you are going to use Zappa, this requires python3.6 **not** python3.7

zappa init

zappa deploy dev

zappa update dev

zappa undeploy dev --remove-logs




# damage-calculator
A simple web app to calculate weapon damage for a set of parameters. 

## Requirements
+ Python 3.7
+ VirtualEnv


## Setup
+ Navigate to project folder
+ Create venv
  + Unix: python3 -m venv venv
  + Windows: py -3 m venv venv
+ Activate venv
  + Unix: . venv/bin/activate
  + Windows: venv\Scripts\activate
+ Install requirements
  + pip install -r requirements.txt
+ Set application path
  + Unix: export FLASK_APP=app.py
  + Windows
    + cmd: set FLASK_APP=app.py
    + Powershell: $env:FLASK_APP = "app.py"
+ Run application
  + All environments: flask run
+ Navigate to URL and use the app!

## Tests
Tests are located in /weapon/tests/tests.py
I used nosetest to run them, which should be installed from the requirements.txt
Should just need to run "nosetests" in any environment.

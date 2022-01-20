# This is a sumamry about infra installation to build api

### 1. conda install (flaks setting)
- download conda package from website -> make virtual env, and source activate that python vir.env
- flask package install (pip install flask)
- flask api source code write


### 2. http test
- FLASK_ENV=development FLASK_APP=app.py FLASK_DEBUG=1 flask run
    - run flask server
    - refer to 'flask_api_run_command.sh'
- brew install httpie 
    - 'http -v GET http://localhost:5000/ping'
    - and check whether the response comes back properly
    - to automation initial database setting, use api-init.sh


### 3. mysql install
- brew install mysql
- mysql.server start
- mysql_secure_isntallation 
    - setting root user password
- mysql -u root -p
    - connect mysql db system
- create databases and tables
    - in mysql command (refer to mysql_setting.txt)

- sqlarchemy install (pip install sqlarchemy)
- package install (pip install mysql-connector-python)


### 4. authentication
- pip install bcrypt
- pip install PyJWT

- source code refactoring
    - password hashing through bcrypt
    - access token generating through jwt (PyJWT)
    - login_required decorator function make and insert before activating other functions


### 5. frontend
- source code build
    - frontend source code make
- python -m http.server
    - run the above command on the directory of frontend source code
    - Independent of flask backend server, it will deploy front-end web server
    - http://localhost:8000

- flask code refactoring
    - pip install flask-cors -> to connect frontend and backend server
    - minor flask source code refactoring


### 6. unit test
- pip install pytest
- 'test_endpoint.py' source code write 
    - prefix 'test_' necessary
    - testing database and config needed
    - although unit-test, http endpoint communication is neededd to test properly
    - by using test_client() (in flask), can solve it!

- after making 'test_endpoint.py' source code, run 'pytest' command


### 7. AWS deployment
- "refers to aws_infra.txt"
    - 1) AWS RDS
    - 2) AWS EC2
    - 3) Deployment
    - 4) Load Balancer


### 8.Layered Architecture
- refactoring overall folder directories and source codes as layered architecture
- there are three layers
    - view (presentation layer)
        - it describes endpoint communication
        - it depends other two layers
    - service (business layer)
        - it describes business logic such as user behavior (sign-up, login, follow, unfollow) and tweet behaivor (add tweet, view tweet timeline)
        - it depends on below layer (persistance layer), but is independents on above layer (presentation layer)
    - model (persistance layer)
        - it describes behaivors in databases such as create, view and so on
        - it is independents on other above layers
- besides, unit-test is also expanded based on three layers
    - at first, test folder created
    - in test folder, unit test created following three layers
        - to test model layer -> test_model.py
        - to test serivce layer -> test_service.py
        - to test view layer -> test_view.py

- some package import issues happen
    - module, package concept is important -> refer to troubleshooting file
    - add __init__.py in order to clarify package structure and for python interpreter to properly search and import packages (modules)
    - "python -m aaa.py"
        - python run command with module option
        - by doing, can clarify a parent package and can solve relative package import errors





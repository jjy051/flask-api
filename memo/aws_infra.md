# AWS Infra Setting

### 1. AWS RDS (MySQL setting)
- create mysql parameter group with settig cetrain parameter options
- create mysql database with that msyql parameter group
    - setting several things such as mysql engine version, vpc, free tier cost, connect paramter group and so on
- after creating rdb, edit security rules to allow every inbound traffic within tcp port 3306
- in mac terminal, 
    - we can connect AWS RDS we just made,
    - by typing 'mysql -h <endpoint> -u <master username> -p'

- let inital databases created and inserted values
    - refers to script/mysql-init file


### 2. AWS EC2
- "Ubuntu Server 18.04 LTS" AMI + "t2.micro" instance type launch
- to test load balance, launch 2 number of instances
- key pair(.pem) (if necessary) created and saved in a proper directory

- after creating ec2, let do proper security setting 
    - ssh connection setting (type: ssh, protocol: tcp, port range: 22, source: anywhere)
    - http connection setting (type: custom tcp rule, protocol: tcp, port range: 5000, source: anywhere)
    
- let connect ec2 instance
    - 'ssh -i <pem key 경로> ubuntu@<ec2 instance public ip addr>'
    - if necessary, add 'sudo'


### 3. Deployment (배포)
- setup.py write (for a production deployment)
    - pip install flask-twisted
    - pip install flask_script
    - write setup.py source code

- there are env conflict on flask_script package and flask (> 2.0.0)
    - to solve it, manually revise "package import" line like below
    - on "~/miniconda3/envs/api/lib/python3.7/site-packages/flask_script/__init__.py"
    - "from flask._compat import text_type" -> "from ._compat import text_type"
        - it needs to do the same revise across all ec2 instances

- requirments.text create
    - for installing dependency on ec2 instances,
    - pip freezee > requirements.text
    - then, ec2 instances install dependencies through that requirements.text later

- ec2 instances setting
    - from git remote repository, clone source codes including requirements.text
    - miniconda installation (+ bash path add)
    - python=3.7 virtual env created and activated
    - pip install -r requirements.txt
    - "nohup python setup.py runserver --host=0.0.0.0 &"
        - it will be continued after ssh session terminated
        - and it also runs background mode
        - it can be terminated by "kill <PID>"
    - if relative import error occurs,
        - go to parent directory by "cd .."
        - and run nohup python command with module option like below
        - "nohup python -m api_project.setup runserver --host=0.0.0.0 &"


### 4. Load Balancer
- on AWS, setting Load Balancer (not that special things to do)
- AWS LB DNS
    - "python-test-2009106037.ap-northeast-2.elb.amazonaws.com"
    - get connection through 5000 port




####### unit test config #######
test_db = {			
    'user'     : 'root',
    'password' : 'rootroot',
    # 'host'     : 'python-backend-test.ctdr1njko4lr.ap-northeast-2.rds.amazonaws.com',
    'host': 'localhost',
    'port'     : 3306,
    'database' : 'miniter_test'
}

test_config = {		
    'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
    'JWT_SECRET_KEY' : 'SOME_SUPER_SECRET_KEY',
    'JWT_EXP_DELTA_SECONDS' : 7 * 24 * 60 * 60,
    'S3_BUCKET': 'cdn-bucket-for-flask-api',
    'S3_ACCESS_KEY': 'check',
    'S3_SECRET_KEY': 'check',
    'S3_BUCKET_URL': 'https://cdn-bucket-for-flask-api.s3.ap-northeast-2.amazonaws.com/test/'
}

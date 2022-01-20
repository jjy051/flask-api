
db = {
  'user': 'root',
  'password': 'rootroot',
  # 'host': 'python-backend-test.ctdr1njko4lr.ap-northeast-2.rds.amazonaws.com',
  'host': 'localhost',
  'port': 3306,
  'database': 'miniter'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
JWT_SECRET_KEY = 'thisistestkey'
JWT_EXP_DELTA_SECONDS : 7 * 24 * 60 * 60

UPLOAD_DIRECTORY = './profile_pictures'

S3_BUCKET = 'cdn-bucket-for-flask-api'
S3_ACCESS_KEY = 'check credential' 
S3_SECRET_KEY = 'check credential'
S3_BUCKET_URL = f"https://{S3_BUCKET}.s3.ap-northeast-2.amazonaws.com/"
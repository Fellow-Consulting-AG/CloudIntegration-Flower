import os


APP_ENV = os.getenv('APP_ENV')
IS_DEBUG = os.getenv('IS_DEBUG')
IS_TESTING = os.getenv('IS_TESTING')
SECRET_KEY = os.getenv('SECRET_KEY')
CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
ADMINS = os.getenv('ADMINS')

APPLICATION_NAME = os.getenv('APPLICATION_NAME')



#CELERY
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
CELERY_TASK_RESULT_EXPIRES = 300

CORE_VERSION = os.getenv('CORE_VERSION')
#db.engine.connect().execute(db.select([db.Table('alembic_version', db.MetaData(), autoload=True, autoload_with=db.engine)])).fetchall()[:1][0][0]



# S3 or Spaces
S3_KEY = os.getenv('S3_KEY')
S3_SECRET= os.getenv('S3_SECRET')
S3_BUCKET= os.getenv('S3_BUCKET')


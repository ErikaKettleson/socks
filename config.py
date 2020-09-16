import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    API_KEY = '4bd51f1d-3eb1-4e34-929e-8c10e5926fca'
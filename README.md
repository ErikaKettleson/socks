# socks

Add API_KEY to root level config.py file 

______

import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'default'
  
  API_KEY = 'YOUR_API_KEY'

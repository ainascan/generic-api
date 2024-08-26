import os

import s3fs

HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8181

def required_env(key):
    value = os.getenv(key)
    
    if value is None:
        raise Exception(f'{key} is not set in environment variables')
    
    return value


def initialize():
    global HTTP_HOST, HTTP_PORT
    
    HTTP_HOST = os.getenv('HTTP_HOST', HTTP_HOST)
    HTTP_PORT = int(os.getenv('HTTP_PORT', HTTP_PORT))
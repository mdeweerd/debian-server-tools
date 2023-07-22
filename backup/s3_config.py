# -*- coding: utf-8 -*-

# Configuration for s3_set_cache_control.py

AWS_ACCESS_KEY = '<aws access key>'
AWS_SECRET_KEY = '<aws secret key>'
AWS_BUCKET_NAME = '<aws bucket name>'
# 365 days
AWS_HEADERS = {
    'Cache-Control':'max-age=31536000, public'
}
AWS_ACL = 'public-read'

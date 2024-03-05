import os
from configparser import ConfigParser


server = os.getenv('SERVER', "production")
# server = 'develop'
p = lambda s, p: s if (server == "production") else p
platform = p("web_prod", "web_s")
print(platform)
parser = ConfigParser()
parser.read('pytest.ini')
client = parser[platform]['client']
password = parser[platform]['pass']
base_url = parser['server'][server]
cf_access_client_id = parser['heders']['client_id']
cf_access_client_secret = parser['heders']['client_secret']







def get_client():
    return client

def get_accesstoken(accessToken):
    accesstoken = parser[platform][accessToken]
    return accesstoken

def get_email(email):
    email = parser[platform][email]
    return email

def get_password():
    return password

def get_base_url():
    return base_url

def get_x_token(token):
    x_xsrf_token = parser[platform][token]
    return x_xsrf_token







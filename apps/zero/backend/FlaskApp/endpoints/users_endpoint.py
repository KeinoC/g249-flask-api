import time
from configs import CONFIGS
import requests;
import math
from flask import Blueprint,request
import json
from urllib.parse import urlparse

myusers =Blueprint("users", __name__, url_prefix="/healthz")

@myusers.route('/users/get',methods=['GET'])
def get_users():
  if request.method == 'GET':
    users = request.get()
  
  
  return { },200



@myusers.route('/test',methods=['GET'])
def mytest_users():
  return {
    "msg":request.url,
    "code": CONFIGS.endpointMsgCodes["success"]
  },200

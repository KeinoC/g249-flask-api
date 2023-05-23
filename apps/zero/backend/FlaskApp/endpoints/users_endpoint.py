import time
# from configs import CONFIGS
import requests;
import math
from flask import Blueprint,request
import json
from urllib.parse import urlparse

myusers =Blueprint("users", __name__, url_prefix="/users")

@myusers.route('/get',methods=['GET'])
def get_users():
  if request.method == 'GET':
    users = request.get()
  return { users },200


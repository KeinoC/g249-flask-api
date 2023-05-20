


import json
import os
import random
from utils.env_vars import ENV_VARS
from utils.singleton_exception import SingletonException
from utils.local_deps import  local_deps
local_deps()
from pypdf import PdfReader
import sentry_sdk



class SentryManager():
  init= False
  def __init__(self):
    if(self.init):
      raise SingletonException
    else:
      self.init = True


  def init_sentry(self):
    sentry_sdk.init(
      dsn="",
      environment="Flask_{}".format(ENV_VARS.get("FLASK_BACKEND_ENV")),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )





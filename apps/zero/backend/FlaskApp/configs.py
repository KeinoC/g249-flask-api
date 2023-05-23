import os
from managers.cron_task_runner import CronTasksRunner
from managers.sentry_manager import SentryManager
from db.sql_server_manager import SQLServerManager
from db.postgres_manager import PostgresManager
from managers.watchdog_manager import WatchdogManager
from utils.env_vars import ENV_VARS
from utils.local_deps import  local_deps
local_deps()
import boto3


class DevConfigs:

  endpointMsgCodes = {
    'success':'OK',
    'error':'ERROR',
  }


  app= {
    'access_control_allow_origin':['https://example.com:4200','https://example.com:4201'],
    'server_name':'example.com:5000',
    'domain_name':'https://example.com:5000',
    'flask_env':'development',
    'frontend_angular_app_url':'https://example.com:4200',
    'frontend_angular_app_domain':'example.com'
  }

  def __init__(self):
    None

  # https://rnacentral.org/help/public-database
  # postgres_manager = PostgresManager({
  #   "user":"reader",
  #   "pass":"NWDMCE5xdipIjRrp",
  #   "host":"hh-pgsql-public.ebi.ac.uk",
  #   "port":"5432",
  #   "db":"pfmegrnargs",
  # })
  sentry_manager = SentryManager()
  cron_task_runner =  CronTasksRunner()
  watchdog_manager = WatchdogManager()



class TestConfigs(DevConfigs):
  None

class PreviewConfigs(DevConfigs):

  def __init__(self) -> None:
    super().__init__()
    self.app['flask_env'] = 'production'
    self.app['access_control_allow_origin'] = ["https://ui.dev.example.co"]
    self.app.pop('server_name')
    self.app.pop('domain_name')
    self.app['frontend_angular_app_url'] = "https://ui.dev.example.co"
    self.app['frontend_angular_app_domain'] = "ui.dev.example.co"

class ProdConfigs(DevConfigs):

  def __init__(self) -> None:
    super().__init__()
    self.app['flask_env'] = 'production'
    self.app['access_control_allow_origin'] = ["https://www.example.co"]
    self.app.pop('server_name')
    self.app.pop('domain_name')
    self.app['frontend_angular_app_url'] = "https://www.example.co"
    self.app['frontend_angular_app_domain'] = "www.example.co"



CONFIGS:DevConfigs= {
  'PROD':lambda x:ProdConfigs(),
  'PREVIEW':lambda x:PreviewConfigs(),
  'DEV':lambda x:DevConfigs(),
  'TEST':lambda x:TestConfigs(),
}[ENV_VARS.get("FLASK_BACKEND_ENV")](None)











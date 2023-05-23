import os
from utils.singleton_exception import SingletonException
from utils.local_deps import  local_deps
local_deps()
from sqlalchemy.engine.create import create_engine

class SQLServerManager():
  init= False
  client = None
  sqlalchemy_0_engine = ""
  sqlalchemy_0_conn = ""
  def __init__(self,conn_obj):
    if(self.init):
      raise SingletonException
    else:
      self.init = True
      self.set_up_sql_conn(conn_obj)


  def set_up_sql_conn(self,conn_obj):
      global sqlalchemy_0_engine
      conn_string = "mssql+pyodbc://{}@{}/{}?driver={}".format(
        conn_obj["pass"],
        conn_obj["host"],
        conn_obj["db"],
        conn_obj.get("driver") if conn_obj.get("driver") else "ODBC+Driver+17+for+SQL+Server"

      )
      self.sqlalchemy_0_engine = create_engine(os.environ.get("SQLALCHEMY_PYMSSQL_0_CONN_STRING"),pool_pre_ping=True)
      self.sqlalchemy_0_conn = self.sqlalchemy_0_engine.connect()


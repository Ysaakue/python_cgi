import sqlite3

class Banco():
  __table_name = ""
  __attributes = {}
  def __init__(self):
    self.conexao = sqlite3.connect("../banco.sqlite")
    self.createTable()

  def set_table_name(self,table_name):
    self.__table_name = table_name

  def createTable(self):
    pass

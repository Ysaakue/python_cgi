from Database import Banco

class User(Banco):
  __table_name = "users"
  __attributes = {
    "email": "",
    "password": ""
  }

  def __init__(self):
    self.conexao = sqlite3.connect("../banco.sqlite")
    self.createTable()

  def createTable(self):
    c = self.conexao.cursor()
    c.execute("""create table if not exists {} (
                  id integer primary key autoincrement ,
                  email text,
                  password text
                )""".format(
                  self.__table_name,
                ))
    self.conexao.commit()
    c.close()

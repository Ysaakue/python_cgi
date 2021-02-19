import sqlite3

class User():
  __id= ""
  __name= ""
  __birth_date= ""
  __weight= ""
  __height= ""
  __email= ""
  __password= ""

  def __init__(self,id=0,name="",birth_date="",weight="",height="",email="",password=""):
    self.conexao = sqlite3.connect("./banco.sqlite")
    self.createTable()
    self.__id = id
    self.__name = name
    self.__birth_date = birth_date
    self.__weight = weight
    self.__height = height
    self.__email = email
    self.__password = password

  def createTable(self):
    c = self.conexao.cursor()
    c.execute(
      """create table if not exists users (
        id integer primary key autoincrement ,
        name text,
        birth_date text,
        weight text,
        height text,
        email text,
        password text
      )"""
    )
    self.conexao.commit()
    c.close()

  def save(self):
    c = self.conexao.cursor()
    sql = """insert into users (name,birth_date,weight,height,email,password)
      values ('{}','{}','{}','{}','{}','{}')""".format(
        self.__name,self.__birth_date,self.__weight,
        self.__height,self.__email,self.__password
      )
    c.execute(sql)
    self.conexao.commit()
    self.__id = c.lastrowid
    c.close()
    return self.__id

  def getId(self):
    return self.__id

  def getEmail(self):
    return self.__email

  def getPassword(self):
    return self.__password

  def getAttributes(self):
    return {
      "name": self.__name,
      "birth_date": self.__birth_date,
      "weight": self.__weight,
      "height": self.__height,
      "email": self.__email,
      "password": self.__password
    }

  @staticmethod
  def find_by(options={}):
    conexao = sqlite3.connect("./banco.sqlite")
    c = conexao.cursor()
    sql = "select * from users where"
    for item in options.items():
      sql += " " + str(item[0]) + " = '" + str(item[1]) + "'"
    sql += ";"
    c.execute(sql)
    conexao.commit()
    for row in c:
      user = User(
        id= row[0],
        name= row[1],
        birth_date= row[2],
        weight= row[3],
        height= row[4],
        email= row[5],
        password= row[6]
      )
    c.close()
    if 'user' in locals():
      return user
    else:
      return User()

  @staticmethod
  def login(email="",password=""):
    conexao = sqlite3.connect("./banco.sqlite")
    c = conexao.cursor()
    c.execute("select * from users where email = '{}' and password = '{}';".format(email,password))
    conexao.commit()
    for row in c:
      user = User(
        id= row[0],
        name= row[1],
        birth_date= row[2],
        weight= row[3],
        height= row[4],
        email= row[5],
        password= row[6]
      )
    c.close()
    if 'user' in locals():
      return user
    else:
      return None

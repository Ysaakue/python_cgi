import cgi,sys
import json
import sqlite3

form = cgi.FieldStorage()

email = form.getvalue("email")
password = form.getvalue("password")
confirm_password = form.getvalue("confirm_password")

dic = {}

if(password != confirm_password):
  dic["status"] = "error"
  dic["message"] = "As senhas não são iguais."
else:
  conexao = sqlite3.connect("./banco.sqlite")
  c = conexao.cursor()
  c.execute(
    "create table if not exists users (id integer primary key autoincrement ,email text,password text);"
  )
  conexao.commit()
  c.execute(
    """insert into users (email,password)
    values ('{}','{}')"""
    .format(email,password)
  )
  conexao.commit()
  id = c.lastrowid
  c.close()
  if id == None:
    dic["status"] = "error"
    dic["message"] = "Ouve um problema no processaento, verifique seus dados e tente novamente."
  else:
    dic["status"] = "success"
    dic["message"] = "Cadastro realizado com sucesso"
    dic["data"] = {}
    dic["data"]["email"] = email
    dic["data"]["password"] = password
    dic["data"]["id"] = id

sys.stdout.write("Content-Type: application/json\n\n")
sys.stdout.write(json.dumps(dic))

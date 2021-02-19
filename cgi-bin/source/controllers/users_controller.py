import cgi,sys
import json
import sqlite3
from models.user import User

form = cgi.FieldStorage()

action = form.getvalue("action")
confirm_password = form.getvalue("confirm_password")

dic = {}
user = User(
    name= form.getvalue("name"),
    weight= form.getvalue("weight"),
    height= form.getvalue("height"),
    birth_date= form.getvalue("birth_date"),
    email= form.getvalue("email"),
    password= form.getvalue("password")
  )

if action == "sign_up":
  if User.find_by(options={"email": user.getEmail()}).getEmail() == user.getEmail():
    dic["status"] = "error"
    dic["message"] = "Email já cadastrado."
  elif(user.getPassword != confirm_password):
    dic["status"] = "error"
    dic["message"] = "As senhas não são iguais."
  else:
    if user.save() == None:
      dic["status"] = "error"
      dic["message"] = "Ouve um problema no processaento, verifique seus dados e tente novamente."
    else:
      dic["status"] = "success"
      dic["message"] = "Cadastro realizado com sucesso"
      dic["user"] = user.getAttributes()
elif action == "sign_in":
  if User.login(email=user.getEmail(),password=user.getPassword()) != None:
    dic["status"] = "success"
    dic["user"] = User.find_by(options={"email": user.getEmail()}).getAttributes()
  else:
    dic["status"] = "error"
    dic["message"] = "Email ou senha incorretos"
    dic["user"] = user.getAttributes()
else:
  dic["status"] = "error"
  dic["message"] = "A ação que você deseja realizar é inválida."

sys.stdout.write("Content-Type: application/json\n\n")
sys.stdout.write(json.dumps(dic))

import cgi,sys
import json
import sqlite3
from models.user import User

form = cgi.FieldStorage()

action = form.getvalue("action")
name = form.getvalue("name")
weight = form.getvalue("weight")
height = form.getvalue("height")
birth_date = form.getvalue("birth_date")
email = form.getvalue("email")
password = form.getvalue("password")
confirm_password = form.getvalue("confirm_password")

dic = {}
user = User(
    name=name,
    weight=weight,
    height=height,
    birth_date=birth_date,
    email=email,
    password=password
  )

if action == "sign_up":
  if User.find_by(options={"email": email}).getEmail() == user.getEmail():
    dic["status"] = "error"
    dic["message"] = "Email já cadastrado."
  elif(password != confirm_password):
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
  pass
else:
  dic["status"] = "error"
  dic["message"] = "A ação que você deseja realizar é inválida."

sys.stdout.write("Content-Type: application/json\n\n")
sys.stdout.write(json.dumps(dic))

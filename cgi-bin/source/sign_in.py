#! /usr/bin/env python3
import cgitb, cgi
from libs.tags import *

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER = "display: flex;align-items: center;justify-content: center;flex-direction: column;"

enc_print(
  init_html(
    inside= head(
      inside="<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
      "<!-- HTML 4 -->"+
      "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>"+
      "<!-- HTML5 -->"+
      "<meta charset='UTF-8'/>",
      title="Index"
    ) +
    body(
      inside=div(
        inside= form(
          input_tag(
            label=True,
            label_text="Email: ",
            placeholder="Digite seu email"
          )+
          br(2)+
          input_tag(
            label=True,
            label_text="Senha: ",
            placeholder="Digite sua senha",
            type="password"
          )
        )+
        p(
          "Ainda não cadastrado?"+
          a(
            text="Realizar cadastro",
            href="sign_up.py"
          )
        ),
        styles= DISPLAY_FLEX_CENTER + "min-height: 100%;"
      )
    )
  )
)

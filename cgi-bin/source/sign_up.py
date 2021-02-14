#! /usr/bin/env python3
import cgitb, cgi
from libs.tags import *

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER = "display: flex;align-items: center;justify-content: center;flex-direction: column;"

enc_print(
  init_html(
    inside= head(
      inside="<meta charset='UTF-8'>"+
      "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
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
          br(1)+
          input_tag(
            label=True,
            label_text="Senha: ",
            placeholder="Digite sua senha",
            type="password"
          )+
          br(1)+
          input_tag(
            label=True,
            label_text="Confirmação de senha: ",
            label_styles="display:absolute;",
            placeholder="Redigite sua senha",
            type="password"
          ),
          styles= DISPLAY_FLEX_CENTER
        )+
        p(
          "Já cadastrado?"+
          a(
            text="Realizar login",
            href="./sign_in.py"
          )
        ),
        styles= DISPLAY_FLEX_CENTER + "min-height: 100%;"
      )
    )
  )
)

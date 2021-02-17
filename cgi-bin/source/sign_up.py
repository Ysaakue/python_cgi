#! /usr/bin/env python3
import cgitb, cgi
from libs import tags

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER = "display: flex;align-items: center;justify-content: center;flex-direction: column;"

tags.enc_print(
  tags.init_html(
    inside= tags.head(
      inside="<meta charset='UTF-8'>"+
      "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"+
      "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
      title="Index"
    ) +
    tags.body(
      inside= tags.div(
        inside= tags.form(
          tags.input_tag(
            label=True,
            label_text="Email: ",
            placeholder="Digite seu email",
            id="email"
          )+
          tags.br(1)+
          tags.input_tag(
            label=True,
            label_text="Senha: ",
            placeholder="Digite sua senha",
            type="password",
            id="password"
          )+
          tags.br(1)+
          tags.input_tag(
            label=True,
            label_text="Confirmação de senha: ",
            label_styles="display:absolute;",
            placeholder="Redigite sua senha",
            type="password",
            id="confirm_password"
          )+
          tags.button(
            inside="Cadastro",
            type="submit",
            styles="margin-top:17px;"
          ),
          id="form",
          method= "post",
          styles= DISPLAY_FLEX_CENTER
        )+
        tags.p(
          "Já cadastrado?"+
          tags.a(
            text="Realizar login",
            href="./sign_in.py"
          ),
          styles="margin-top:0px;"
        ),
        styles= DISPLAY_FLEX_CENTER + "min-height: 100%;"
      )+
      tags.script(
        inside="$(document).ready(function(){"+
          "$('#form').submit(function(e){"+
            "e.preventDefault();"+
            "var email = $('#email').val();"+
            "var password= $('#password').val();"+
            "var confirm_password= $('#confirm_password').val();"+
            "$.ajax({"+
              "type: 'POST',"+
              "url: 'controllers/users_controller.py',"+
              "data: {email:email,password:password,confirm_password:confirm_password},"+
              """success:function(res){
                  if(res['status'] == 'success'){
                    alert('O seu cadastro foi efetuado com sucesso');
                  }else if(res['status'] == 'error'){
                    alert('Ocorreu um erro durante seu cadastro: '+res['message']);
                  } else {
                    alert('Ocorreu um erro imprevisto.')
                  }
                },"""+
              "error:function(xhr,errmsg,err){ alert(xhr.status + ': ' + xhr.responseText);}"+
            "});"+
          "});"+
        "});"
      )
    )
  )
)

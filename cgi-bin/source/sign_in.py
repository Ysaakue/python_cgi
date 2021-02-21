#! /usr/bin/env python3
import cgitb, cgi
from libs import tags

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER_COLUMN = "display: flex;align-items: center;justify-content: center;flex-direction: column;"

tags.enc_print(
  tags.init_html(
    inside= tags.head(
      inside="<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
      "<!-- HTML 4 -->"+
      "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>"+
      "<!-- HTML5 -->"+
      "<meta charset='UTF-8'/>",
      title="Login"
    ) +
    tags.body(
      inside= tags.div(
        inside= tags.form(
          tags.input_tag(
            label=True,
            label_text="Email: ",
            placeholder="Digite seu email",
            id= "email"
          )+
          tags.br(2)+
          tags.input_tag(
            label=True,
            label_text="Senha: ",
            placeholder="Digite sua senha",
            type="password",
            id="password"
          )+
          tags.button(
            inside="Entrar",
            type="submit",
            styles="margin-top:17px;"
          ),
          id="form",
          method= "post",
          styles= DISPLAY_FLEX_CENTER_COLUMN
        )+
        tags.p(
          "Ainda não cadastrado?"+
          tags.a(
            text="Realizar cadastro",
            href="sign_up.py"
          )
        ),
        styles= DISPLAY_FLEX_CENTER_COLUMN + "min-height: 100%;"
      )+
      tags.script(
        inside=
        """
        $(document).ready(function(){
          $('#form').submit(function(e){
            e.preventDefault();
            var email = $('#email').val();
            var password= $('#password').val();
            $.ajax({
              type: 'POST',
              url: 'controllers/users_controller.py',
              data: {
                action: 'sign_in',
                email:email,
                password:password,
              },
              success:function(res){
                  if(res['status'] == 'success'){
                    window.location.href = './home.py';
                  }else if(res['status'] == 'error'){
                    alert('Ocorreu um erro durante seu login: '+res['message']);
                  } else {
                    alert('Ocorreu um erro imprevisto.')
                  }
                },
              error:function(xhr,errmsg,err){ alert(xhr.status + ': ' + xhr.responseText);}
            });
          });
        });"""
      )
    )
  )
)

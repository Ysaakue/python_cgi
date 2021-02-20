#! /usr/bin/env python3
import cgitb, cgi
from libs import tags

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER_COLUMN = "display: flex;align-items: center;justify-content: center;flex-direction: column;"
DISPLAY_FLEX_CENTER_ROW = "display: flex;align-items: center;justify-content: center;flex-direction: row;"

tags.enc_print(
  tags.init_html(
    inside= tags.head(
      inside="<meta charset='UTF-8'>"+
      "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"+
      "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
      """
      <style>
        .modal {
          display: none; /* Hidden by default */
          position: fixed; /* Stay in place */
          z-index: 1; /* Sit on top */
          padding-top: 100px; /* Location of the box */
          left: 0;
          top: 0;
          width: 100%; /* Full width */
          height: 100%; /* Full height */
          overflow: auto; /* Enable scroll if needed */
          background-color: rgb(0,0,0); /* Fallback color */
          background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
        }

        .modal-content {
          background-color: #fefefe;
          margin: auto;
          padding: 20px;
          border: 1px solid #888;
          width: 80%;
        }
      </style>
      """
      ,
      title="Cadastro"
    ) +
    tags.body(
      inside= tags.div(
        styles= DISPLAY_FLEX_CENTER_COLUMN + "min-height: 100%;",
        inside= tags.form(
          tags.div(
            styles= DISPLAY_FLEX_CENTER_ROW,
            inside=tags.input_tag(
              label=True,
              label_text="Nome: ",
              placeholder="Digite seu nome",
              id="name",
              div_margin=3
            )+
            tags.input_tag(
              label=True,
              label_text="Email: ",
              placeholder="Digite seu email",
              id="email",
              div_margin=3
            )
          )+
          tags.br(1)+
          tags.div(
            styles= DISPLAY_FLEX_CENTER_ROW,
            inside=tags.input_tag(
              label=True,
              label_text="Peso(Kg): ",
              placeholder="Digite seu peso",
              id="weight",
              div_margin=3
            )+
            tags.input_tag(
              label=True,
              label_text="Altura(m): ",
              placeholder="Digite seu altura",
              id="height",
              div_margin=3
            )
          )+
          tags.br(1)+
          tags.div(
            styles= DISPLAY_FLEX_CENTER_ROW + "width: 100%;",
            inside=tags.input_tag(
              label=True,
              label_text="Data de Nasciemnto: ",
              placeholder="Digite sua data de nascimento",
              id="birth_date",
              type="date",
              styles="width: 100%;",
              div_width="100%"
            )
          )+
          tags.br(1)+
          tags.div(
            styles= DISPLAY_FLEX_CENTER_ROW,
            inside=tags.input_tag(
              label=True,
              label_text="Senha: ",
              placeholder="Digite sua senha",
              type="password",
              id="password",
              div_margin=3
            )+
            tags.input_tag(
              label=True,
              label_text="Confirmação de senha: ",
              label_styles="display:absolute;",
              placeholder="Redigite sua senha",
              type="password",
              id="confirm_password",
              div_margin=3
            )
          )+
          tags.button(
            inside="Cadastro",
            type="submit",
            styles="margin-top:17px;"
          ),
          id="form",
          method= "post",
          styles= DISPLAY_FLEX_CENTER_COLUMN
        )+
        tags.p(
          "Já cadastrado?"+
          tags.a(
            text="Realizar login",
            href="./sign_in.py"
          ),
          styles="margin-top:0px;"
        )
      )+
      tags.div(
        id= "myModal",
        classes= "modal",
        inside= tags.div(
          classes= "modal-content",
          inside=tags.p(
            inside= "",
            id= "modal-text"
          )+
          tags.div(
            styles= DISPLAY_FLEX_CENTER_ROW,
            inside= tags.button(
              styles= "margin: 5px",
              id= "confirm",
              inside="Confirmar"
            )+
            tags.button(
              styles= "margin: 5px",
              id= "cancel",
              inside= "Cancelar"
            )
          )
        )
      )+
      tags.script(
        inside="""$(document).ready(function(){
          var email_input = $('#email');
          var weight_input = $('#weight');
          var birth_date_input = $('#birth_date');
          var height_input = $('#height');
          var name_input = $('#name');
          var password_input = $('#password');
          var confirm_password_input = $('#confirm_password');

          var modal = document.getElementById("myModal");
          var confirm = document.getElementById("confirm");
          var cancel = document.getElementById("cancel");
          var modalText = document.getElementById("modal-text");

          function setModalText(){
            modalText.innerHTML = '<h3> Confirme os seus dados</h3>'+
            'Nome: '+ name_input.val() + '<br>' +
            'Email: ' + email_input.val() + '<br>' +
            'Peso: ' + weight_input.val() + '<br>' +
            'Altura: ' + height_input.val() + '<br>' +
            'Data de nasciemnto: ' + birth_date_input.val() + '<br>';
          }

          $('#form').submit(function(e){
            e.preventDefault();
            setModalText();
            modal.style.display = "block";
          });

          function clearForm() {
            email_input.val('');
            weight_input.val('');
            birth_date_input.val('');
            height_input.val('');
            name_input.val('');
            password_input.val('');
            confirm_password_input.val('');
          }

          // When the user clicks the button, open the modal 
          confirm.onclick = function() {
            $.ajax({
              type: 'POST',
              url: 'controllers/users_controller.py',
              data: {
                action: 'sign_up',
                email: email_input.val(),
                weight: weight_input.val(),
                birth_date: birth_date_input.val(),
                height: height_input.val(),
                name: name_input.val(),
                password :password_input.val(),
                confirm_password: confirm_password_input.val()
              },
              success:function(res){
                if(res['status'] == 'success'){
                  alert('O seu cadastro foi efetuado com sucesso');
                  clearForm();
                }else if(res['status'] == 'error'){
                  alert('Ocorreu um erro durante seu cadastro: '+res['message']);
                } else {
                  alert('Ocorreu um erro imprevisto.')
                }
                modal.style.display = "none";
              },
              error:function(xhr,errmsg,err){
                alert(xhr.status + ': ' + xhr.responseText);
                modal.style.display = "none";
              }
            });
          }

          cancel.onclick = function closeModal() {
            modal.style.display = "none";
          }
        });"""
      )
    )
  )
)

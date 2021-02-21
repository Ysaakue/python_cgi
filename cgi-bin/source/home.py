#! /usr/bin/env python3
import cgitb, cgi
from libs import tags
from controllers.models.user import User

cgitb.enable(display=0, logdir="./")

DISPLAY_FLEX_CENTER = "display: flex;align-items: center;justify-content: center;flex-direction: column;"

tags.enc_print(
  tags.init_html(
    inside= tags.head(
      inside="<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
      "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>"+
      "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
      "<!-- HTML 4 -->"+
      "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>"+
      "<!-- HTML5 -->"+
      "<meta charset='UTF-8'/>"+
      """
      <style>
        table, td, th {
          border: 1px solid black;
        }

        table {
          width: 100%;
          border-collapse: collapse;
        }
      </style>
      """,
      title="Index"
    ) +
    tags.body(
      inside=tags.button(
        inside="Apagar todos os registros",
        onClick="destroyAll()",
        styles="margin: 10px;"
      )+
      tags.table(
        header= True,
        content= User.allToTable(),
        styles= "border-collapse: collapse;"
      )+
      tags.script(
        """
        function destroyAll(){
          $.ajax({
            type: 'POST',
            url: 'controllers/users_controller.py',
            data: {
              action: 'delete'
            },
            success:function(res){
                if(res['status'] == 'success'){
                  location.reload();
                }else if(res['status'] == 'error'){
                  alert('Ocorreu um erro durante seu login: '+res['message']);
                } else {
                  alert('Ocorreu um erro imprevisto.')
                }
              },
            error:function(xhr,errmsg,err){ alert(xhr.status + ': ' + xhr.responseText);}
          });
        }
        """
      )
    )
  )
)

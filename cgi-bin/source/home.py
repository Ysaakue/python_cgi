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
      tags.table(
        header= True,
        content= User.allToTable(),
        styles= "border-collapse: collapse;"
      )
    )
  )
)

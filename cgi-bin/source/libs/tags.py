import sys

def a(href="#",text="",classes="",id="",styles=""):
  return(
    "<a href='"+href+"' class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    text+
    "</a>"
  )

def body(inside,classes="",id="",styles=""):
  return(
    "<body class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</body>"
  )

def br(repeat=1):
  return "<br>"*repeat

def button(inside,type="",onClick="",classes="",id="",styles=""):
  return(
    "<button class='"+classes+"' id='"+id+"' style='"+styles+"' onClick='"+onClick+"' >"+
    inside+
    "</button>"
  )

def div(inside,classes="",id="",styles=""):
  return(
    "<div class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</div>"
  )

def enc_print(string='', encoding='utf8'):
  sys.stdout.buffer.write(string.encode(encoding) + b'\n')

def form(inside,action="",method="",classes="",id="",styles=""):
  return(
    "<form action='"+action+"' method='"+method+"' class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</form>"
  )

def h1(inside,classes="",id="",styles=""):
  return(
    "<h1 class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</h1>"
  )

def head(inside,title=""):
  return(
    "<head>"+
    "<title>"+title+"</title>"+
    inside +
    "</head>"
  )

def init_html(inside,classes="",id="",styles=""):
  print("Content-type:text/html; charset=utf-8\r\n\r\n")
  return (
    "<html>"+
    inside +
    "</html>"
  )

def input_tag(value="",div_margin=0,div_width="",label=False,label_text="",type="text",label_classes="",label_id="",label_styles="",classes="",id="",styles="",placeholder=""):
  string = ""
  if label:
    string += "<div style='margin: "+str(div_margin)+"px; width: "+div_width+";'><label for='"+id+"' class='"+label_classes+"' id='"+label_id+"' style='"+label_styles+"'>"+label_text+"</label><br>"
  string += "<input type='"+type+"' id='"+id+"' name='"+id+"' value='"+value+"' placeholder='"+placeholder+"' style='"+styles+"'>"
  if label:
    string += "</div>"
  return string

def p(inside,classes="",id="",styles=""):
  return(
    "<p class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</p>"
  )

def script(inside):
  return(
    "<script>"+
    inside+
    "</script>"
  )

def select(value="",options=[],div_margin=0,label=False,label_text="",type="text",label_classes="",label_id="",label_styles="",classes="",id="",styles="",placeholder=""):
  string = ""
  if label:
    string += "<div style='margin: "+str(div_margin)+"px;'><label for='"+id+"' class='"+label_classes+"' id='"+label_id+"' style='"+label_styles+"'>"+label_text+"</label><br>"
  string += "<select type='"+type+"' id='"+id+"' name='"+id+"' value='"+value+"' placeholder='"+placeholder+"'>"
  for option in options:
    string += "<option value='"+option.lower()+"'>"+option+"</option>"
  string += "<select>"
  if label:
    string += "</div>"
  return string

def span(inside,classes="",id="",styles=""):
  return(
    "<span class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
    inside+
    "</span>"
  )

def table(header=False,content=[],classes="",id="",styles=""):
  string = "<table class='"+classes+"' id='"+id+"' style='"+styles+"'>"
  for i in range(len(content)):
    string += "<tr>"
    for j in content[i]:
      if i == 0 and header:
        string += "<th>"
      else:
        string += "<td>"
      string += str(j)
      if i == 0 and header:
        string += "</th>"
      else:
        string += "</td>"
    string += "</tr>"

  string += "</table>"
  return string

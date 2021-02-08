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

def div(inside,classes="",id="",styles=""):
	return(
		"<div class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
		inside+
		"</div>"
	)

def enc_print(string='', encoding='utf8'):
	sys.stdout.buffer.write(string.encode(encoding) + b'\n')

def form(inside,classes="",id="",styles=""):
	return(
		"<form class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
		inside+
		"</form>"
	)

def head(inside,title=""):
	return(
		"<head>"+
		"<title>"+title+"</title>"+
		inside +
		"</head>"
	)

def h1(inside,classes="",id="",styles=""):
	return(
		"<h1 class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
		inside+
		"</h1>"
	)

def init_html(inside,classes="",id="",styles=""):
	print("Content-type:text/html; charset=utf-8\r\n\r\n")
	return (
		"<html>"+
		inside +
		"</html>"
	)

def input_tag(value="",label=False,label_text="",type="text",label_classes="",label_id="",label_styles="",classes="",id="",styles="",placeholder=""):
	string = ""
	if label:
		string += "<label for='"+id+"' class='"+label_classes+"' id='"+label_id+"' style='"+label_styles+"'>"+label_text+"</label>"
	string += "<input type='"+type+"' id='"+id+"' name='"+id+"' value='"+value+"' placeholder='"+placeholder+"'>"
	return string

def p(inside,classes="",id="",styles=""):
	return(
		"<p class='"+classes+"' id='"+id+"' style='"+styles+"'>"+
		inside+
		"</p>"
	)
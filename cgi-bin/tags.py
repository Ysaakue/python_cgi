def body(inside,classes="",ids="",styles=""):
	return(
		"<body class='"+classes+"' id='"+ids+"' style='"+styles+"'>"+
		inside+
		"</body>"
	)

def head(inside):
	return(
		"<head>"+
		inside +
		"</head>"
	)

def h1(inside,classes="",ids="",styles=""):
	return(
		"<h1 class='"+classes+"' id='"+ids+"' style='"+styles+"'>"+
		inside+
		"</h1>"
	)

def init_html(inside,classes="",ids="",styles=""):
	print("Content-type:text/html\r\n\r\n")
	return (
		"<html lang='en'>"+
		inside +
		"</html>"
	)

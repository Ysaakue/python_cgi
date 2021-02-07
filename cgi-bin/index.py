#! /usr/bin/env python3
import cgitb, cgi
import tags

cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

# nome = form.getvalue("nome")
# idade = int(form.getvalue("idade"))
nome = "nome"
idade = 1

print(
	tags.init_html(
		inside= tags.head(
			"<meta charset='UTF-8'>"+
			"<meta http-equiv='X-UA-Compatible' content='IE=edge'>"+
			"<meta name='viewport' content='width=device-width, initial-scale=1.0'>"+
			"<title>Index</title>"
		) +
		tags.body(
			inside= tags.h1(
				"Hello, %s com %i anos" % (nome,idade)
			),
			styles= "background-color: red"
		)
	)
)

import web

urls = (
    '/', 'index' ,
		'/pag1','pag1',
		'/pag2','pag2'
)

class index:
    def GET(self):
        return """<html>
										<head>
										<link rel="stylesheet" type="text/css" href="/static/css/style.css" media="screen"/>
										</head>
										<body><p>Estilo de parrafo</p>
										</body>
									</html>"""
class pag1:
		def GET(self):
			return """<html>
										<head>
										<link rel="stylesheet" type="text/css" href="/static/css/style.css" media="screen"/>
										</head>
										<body><h1>Esta es la pagina 1</h1>
										</body>
									</html>"""


class pag2:
		def GET(self):
			return """<html>
										<head>
										<link rel="stylesheet" type="text/css" href="/static/css/style.css" media="screen"/>
										</head>
										<body><h2>Esta es la pagina 2</h2>
										</body>
									</html>"""

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))



if __name__ == "__main__":
	app = web.application(urls, globals())
	app.notfound = notfound
	app.run()


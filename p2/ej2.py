
import web

urls = (
    '/', 'index' 
)

class index:
    def GET(self):
        return """<html>
										<head>
										<link rel="stylesheet" type="text/css" href="/css/style.css" media="screen" />
										</head>
										<body><p>Estilo de párrafo</p>
										</body>
									</html>"""

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

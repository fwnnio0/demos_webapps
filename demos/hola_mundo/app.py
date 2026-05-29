import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola Mundo'

if __name__ == "__main__":
    app.run()
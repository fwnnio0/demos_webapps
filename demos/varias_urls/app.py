import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/productos', 'Productos',
)

app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo'

class Clientes:
    def GET(self):
        return 'Clientes'

class Productos:
    def GET(self):
        return 'Productos'

if __name__ == "__main__":
    app.run()

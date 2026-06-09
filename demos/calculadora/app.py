import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)

app = web.application(urls, globals(), autoreload=False)
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Calculadora:
    def GET(self):
        titulo = "Calculadora"
        descripcion = "Esta es una pequeña calculadora"
        return render.calculadora(titulo, descripcion)
    
    def POST(self):
        formulario = web.input()
        numero1 = formulario['numero_1']

        return numero1

if __name__ == "__main__":
    app.run()

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
        return render.calculadora(titulo, descripcion, "")

    def POST(self):
        formulario = web.input()
        numero1 = float(formulario['numero_1'])
        numero2 = float(formulario['numero_2'])
        resultado = numero1 + numero2

        titulo = "Calculadora"
        descripcion = "Esta es una pequeña calculadora"
        return render.calculadora(titulo, descripcion, resultado)

if __name__ == "__main__":
    app.run()

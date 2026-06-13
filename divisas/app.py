import web

urls = (
    '/', 'Index',
    '/divisas', 'Divisas'
)
app = web.application(urls, globals())
render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()
    
class Divisas:
    def GET(self):
        return render.divisas(0, 0, "")

    def POST(self):
        cantidad = float(web.input()['cantidad'])
        moneda = web.input()['moneda']
        
        if moneda == 'usd':
            resultado = cantidad * 18.50  # 1 USD = 18.50 MXN
            simbolo = "USD → MXN"
        elif moneda == 'eur':
            resultado = cantidad * 20.30  # 1 EUR = 20.30 MXN
            simbolo = "EUR → MXN"
        elif moneda == 'cad':
            resultado = cantidad * 13.80  # 1 CAD = 13.80 MXN
            simbolo = "CAD → MXN"
        else:
            resultado = 0
            simbolo = ""
            
        return render.divisas(cantidad, round(resultado, 2), simbolo)

if __name__ == "__main__":
    app.run()
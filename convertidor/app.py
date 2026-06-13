import web

urls = (
    '/','Index',
    '/convertidor', 'Convertidor'
)

app = web.application(urls, globals())
render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()
    
class Convertidor:
    def GET(self):
        return render.convertidor(0, "")  # celsius, fahrenheit

    def POST(self):
        celsius = float(web.input()['celsius'])
        fahrenheit = (celsius * 9/5) + 32
        return render.convertidor(celsius, fahrenheit)

if __name__ == "__main__":
    app.run()
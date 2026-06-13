import web

urls = (
    '/', 'Index',
    '/imc', 'IMC'
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class IMC:
    def GET(self):
        return render.imc(0, 0, 0, "")
    
    def POST(self):
        peso = float(web.input()['peso'])
        altura = float(web.input()['altura'])
        
        # Fórmula IMC = peso / altura²
        imc = peso / (altura * altura)
        
        # Clasificación
        if imc < 18.5:
            estado = "Bajo peso"
        elif imc < 25:
            estado = "Peso normal"
        elif imc < 30:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"
            
        return render.imc(peso, altura, round(imc, 2), estado)

if __name__ == "__main__":
    app.run()
import web
import math

urls = (
    '/', 'Index',
    '/calculadora','Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class Calculadora:
    def GET(self):
        numero_1 = 0
        numero_2 = 0
        resultado = 0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero_1 = float(formulario['numero_1'])
        numero_2 = float(formulario['numero_2'])
        operacion = formulario.get('operacion', '')

        if operacion == 'sumar':
            resultado = numero_1 + numero_2
        elif operacion == 'restar':
            resultado = numero_1 - numero_2
        elif operacion == 'multiplicar':
            resultado = numero_1 * numero_2
        elif operacion == 'dividir':
            if numero_2 != 0:
                resultado = numero_1 / numero_2
            else:
                resultado = "Error: no se puede dividir entre 0"
        elif operacion == 'raiz':
            if numero_1 >= 0:
                resultado = math.sqrt(numero_1)
            else:
                resultado = "Error: raíz de número negativo"
        elif operacion == 'potencia':
            resultado = numero_1 ** numero_2
        elif operacion == 'modulo':
            if numero_2 != 0:
                resultado = numero_1 % numero_2
            else:
                resultado = "Error: módulo entre 0"
        elif operacion == 'limpiar':
            numero_1 = 0
            numero_2 = 0
            resultado = 0
        else:
            resultado = "Operación no válida"

        return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
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

        try:
            numero_1 = float(formulario['numero_1'])
            numero_2 = float(formulario['numero_2'])
        except ValueError:
            numero_1 = 0
            numero_2 = 0
            resultado = "Error: mete solo números"
            return render.calculadora(numero_1, numero_2, resultado)

        operacion = formulario['operacion']

        # Sumar
        if operacion == 'sumar':
            resultado = numero_1 + numero_2

        # Restar
        elif operacion == 'restar':
            resultado = numero_1 - numero_2

        # Multiplicar
        elif operacion == 'multiplicar':
            resultado = numero_1 * numero_2

        # Dividir
        elif operacion == 'dividir':
            if numero_2 != 0:
                resultado = numero_1 / numero_2
            else:
                resultado = "Error: no se puede dividir entre 0"

        # Raíz cuadrada de numero_1
        elif operacion == 'raiz':
            if numero_1 >= 0:
                resultado = math.sqrt(numero_1)
            else:
                resultado = "Error: raíz de número negativo"

        # Potencia numero_1 ** numero_2
        elif operacion == 'potencia':
            resultado = numero_1 ** numero_2

        # Módulo
        elif operacion == 'modulo':
            if numero_2 != 0:
                resultado = numero_1 % numero_2
            else:
                resultado = "Error: módulo entre 0"

        # Limpiar
        elif operacion == 'limpiar':
            numero_1 = 0
            numero_2 = 0
            resultado = 0

        else:
            resultado = "Operación no válida"

        print(f"El tipo de dato es: {type(numero_1)}")

        return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()
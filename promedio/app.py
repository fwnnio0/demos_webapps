import web 

urls = (
    '/', 'Index',
    '/promedio', 'Promedio'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class Promedio:
    def GET(self):
        return render.promedio(0, 0, 0, 0, "")
    
    def POST(self):
        calificacion1 = float(web.input()['calificacion1'])
        calificacion2 = float(web.input()['calificacion2'])
        calificacion3 = float(web.input()['calificacion3'])
        promedio = (calificacion1 + calificacion2 + calificacion3) / 3
        
        if promedio >= 6:
            mensaje = "Aprobado"
        else:
            mensaje = "Reprobado"
            
        return render.promedio(calificacion1, calificacion2, calificacion3, promedio, mensaje)

if __name__ == "__main__":
    app.run()   
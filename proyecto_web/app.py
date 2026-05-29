import web

urls = (
    '/',              'Inicio',
    '/sesion',        'IniciarSesion',
    '/perfil',        'Perfil',
    '/contacto',      'Contacto',
    '/cerrar',        'CerrarSesion',
    '/registro',      'Registro',
    '/configuracion', 'Configuracion',
    '/notificaciones','Notificaciones',
    '/acerca',        'Acerca',
    '/panel',         'Panel',
)

app = web.application(urls, globals())
render = web.template.render('plantillas/', base='base')


class Inicio:
    def GET(self):
        return render.inicio()

class IniciarSesion:
    def GET(self):
        return render.sesion()

class Perfil:
    def GET(self):
        return render.perfil()

class Contacto:
    def GET(self):
        return render.contacto()

class CerrarSesion:
    def GET(self):
        return render.cerrar()

class Registro:
    def GET(self):
        return render.registro()

class Configuracion:
    def GET(self):
        return render.configuracion()

class Notificaciones:
    def GET(self):
        return render.notificaciones()

class Acerca:
    def GET(self):
        return render.acerca()

class Panel:
    def GET(self):
        return render.panel()


if __name__ == "__main__":
    app.run()
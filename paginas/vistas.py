from flask import render_template

class PaginaBase:
    ruta = "/"
    titulo = "Página"
    mensaje = "Bienvenido."

    def mostrar(self):
        return render_template("pagina.html",
                               titulo=self.titulo,
                               mensaje=self.mensaje)

class PaginaInicio(PaginaBase):
    ruta = "/"
    titulo = "Inicio"
    mensaje = "Bienvenido a la página de inicio."

class PaginaLogin(PaginaBase):
    ruta = "/login"
    titulo = "Login"
    mensaje = "Bienvenido a este tu espacio."

class PaginaRegistro(PaginaBase):
    ruta = "/registro"
    titulo = "Registro"
    mensaje = "Crea tu cuenta aquí."

class PaginaPerfil(PaginaBase):
    ruta = "/perfil"
    titulo = "Mi Perfil"
    mensaje = "Esta es tu información personal."

class PaginaDashboard(PaginaBase):
    ruta = "/dashboard"
    titulo = "Dashboard"
    mensaje = "Aquí están tus estadísticas."

class PaginaMensajes(PaginaBase):
    ruta = "/mensajes"
    titulo = "Mensajes"
    mensaje = "Tu bandeja de mensajes."

class PaginaNotificaciones(PaginaBase):
    ruta = "/notificaciones"
    titulo = "Notificaciones"
    mensaje = "Tus alertas y avisos recientes."

class PaginaConfiguracion(PaginaBase):
    ruta = "/configuracion"
    titulo = "Configuración"
    mensaje = "Ajusta las opciones de tu cuenta."

class PaginaAyuda(PaginaBase):
    ruta = "/ayuda"
    titulo = "Ayuda"
    mensaje = "¿Necesitas ayuda? Estamos aquí."

class PaginaSalir(PaginaBase):
    ruta = "/logout"
    titulo = "Cerrar Sesión"
    mensaje = "Has cerrado sesión. ¡Hasta pronto!"

PAGINAS = [
    PaginaInicio, PaginaLogin, PaginaRegistro, PaginaPerfil,
    PaginaDashboard, PaginaMensajes, PaginaNotificaciones,
    PaginaConfiguracion, PaginaAyuda, PaginaSalir,
]

def registrar_rutas(app):
    for pagina in PAGINAS:
        objeto = pagina()

        def crear_vista(obj):
            def vista():
                return obj.mostrar()
            vista.__name__ = obj.__class__.__name__
            return vista

        app.add_url_rule(objeto.ruta, objeto.__class__.__name__, crear_vista(objeto))
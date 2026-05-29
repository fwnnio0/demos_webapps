from flask import render_template

class BasePage:
    ruta = "/"
    titulo = "Página"
    mensaje = "Bienvenido."

    def mostrar(self):
        return render_template("pagina.html",
                               titulo=self.titulo,
                               mensaje=self.mensaje)

class PaginaInicio(BasePage):
    ruta = "/"
    titulo = "Inicio"
    mensaje = "Bienvenido a la página de inicio."

class PaginaLogin(BasePage):
    ruta = "/login"
    titulo = "Login"
    mensaje = "Bienvenido a este tu espacio."

class PaginaRegistro(BasePage):
    ruta = "/registro"
    titulo = "Registro"
    mensaje = "Crea tu cuenta aquí."

class PaginaPerfil(BasePage):
    ruta = "/perfil"
    titulo = "Mi Perfil"
    mensaje = "Esta es tu información personal."

class PaginaDashboard(BasePage):
    ruta = "/dashboard"
    titulo = "Dashboard"
    mensaje = "Aquí están tus estadísticas."

class PaginaMensajes(BasePage):
    ruta = "/mensajes"
    titulo = "Mensajes"
    mensaje = "Tu bandeja de mensajes."

class PaginaNotificaciones(BasePage):
    ruta = "/notificaciones"
    titulo = "Notificaciones"
    mensaje = "Tus alertas y avisos recientes."

class PaginaConfiguracion(BasePage):
    ruta = "/configuracion"
    titulo = "Configuración"
    mensaje = "Ajusta las opciones de tu cuenta."

class PaginaAyuda(BasePage):
    ruta = "/ayuda"
    titulo = "Ayuda"
    mensaje = "¿Necesitas ayuda? Estamos aquí."

class PaginaSalir(BasePage):
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
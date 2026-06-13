import web

urls = (
    '/', 'Index',
    '/login', 'Login'
)
app = web.application(urls, globals())
render = web.template.render('views')

USUARIO = "admin"
PASSWORD = "1234"

class Index:
    def GET(self):
        return render.index()

class Login:
    def GET(self):
        return render.login("", "")

    def POST(self):
        user = web.input()['usuario']
        pwd = web.input()['password']
        
        if user == USUARIO and pwd == PASSWORD:
            mensaje = "Bienvenido " + user
        else:
            mensaje = "Usuario o contraseña incorrectos"
            
        return render.login(user, mensaje)

if __name__ == "__main__":
    app.run()
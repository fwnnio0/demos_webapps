import web

urls = [
    '/', 'Index',
    '/parametros', 'Parametros'
]

app = web.application(urls, globals(), autoreload=False)
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Parametros:
    def GET(self):
        titulo = "Pagina con parametros"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit vestibulum mattis neque, pretium non faucibus habitant mus himenaeos varius a ante. Habitasse mollis mus conubia erat in taciti donec integer porttitor quisque, sollicitudin habitant rutrum suspendisse hac himenaeos risus litora vivamus penatibus, viverra placerat montes dictum tristique cras ornare ac molestie. Lobortis nec gravida vivamus habitasse auctor leo tempor magna et, nisl nunc nascetur ac duis nibh neque commodo, mattis parturient sociosqu ultrices inceptos phasellus dictumst in. Inceptos bibendum posuere hac semper dui convallis nibh sed etiam velit elementum sagittis, morbi augue rhoncus pharetra leo vestibulum penatibus interdum arcu mi porta. Massa posuere class varius per curae habitasse congue non interdum fames tellus euismod, ligula vulputate erat fermentum purus lobortis etiam accumsan venenatis quam tempus. Nascetur sollicitudin vulputate turpis ac dictumst tortor luctus nostra, velit praesent ornare primis fringilla sagittis dui mollis malesuada, hendrerit felis sem maecenas vitae diam phasellus."""
        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()

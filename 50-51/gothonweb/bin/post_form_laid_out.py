import web

urls = ('/hello', 'Index')

post_form_laid_out = web.application(urls, globals())

render = web.template.render('templates/', base = "layout")

class Index(object):
    def GET(self):
        return render.hello_form_laid_out()

    def POST(self):
        form =  web.input(name='Nobody', greet='Hello')
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return  render.index_laid_out(greeting = greeting)
        else:
            return "ERROR: greet is required."

if __name__ == '__main__':
    post_form_laid_out.run()

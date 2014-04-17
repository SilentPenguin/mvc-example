from mvc.controller.controller import Controller

class HelloWorld(Controller):
    #@get
    def index(self):
        return View(template = './views/helloworld/index')
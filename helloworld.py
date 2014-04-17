from mvc.controller.controller import Controller

class HelloWorld(Controller):
    #@get
    def index(self):
        return self.view(template = './mvcexample/views/helloworld/index.pyhtml')
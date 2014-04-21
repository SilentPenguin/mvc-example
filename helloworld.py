from mvc.controller.controller import Controller
from mvc.controller.dispatch import get, post
from mvc.modelbinding.models import Model, Field

class UserModel(Model):
    name = Field(validate = '^[\w ]+$')

class HelloWorld(Controller):
    @get
    def index(self):
        model = UserModel(self.request)
        return self.view(model, './mvcexample/views/helloworld/form.pyhtml')
    
    @index.post
    def index(self):
        model = UserModel(self.request)
        if model.valid:
            return self.view(model, './mvcexample/views/helloworld/index.pyhtml')
        else:
            # model doesn't /have/ to be a Model class, it's passed to the
            # templateas is
            return self.view(model, './mvcexample/views/helloworld/form.pyhtml')
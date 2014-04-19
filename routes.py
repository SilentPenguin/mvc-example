from mvc.routing.route import Route
from helloworld import HelloWorld
from mvc.application.application import Application

route_map = Application.route_map
route_map += Route('/', HelloWorld.index)
route_map += Route('/hello/world', HelloWorld.index)
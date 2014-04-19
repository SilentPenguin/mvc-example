from mvc.routing.route import Route
from helloworld import HelloWorld
from mvc.settings.settings import route_map

route_map += Route('/', HelloWorld.index)
route_map += Route('/hello/world', HelloWorld.index)
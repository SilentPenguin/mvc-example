from mvc.routing.route import route_map, Route
from helloworld import HelloWorld

route_map += Route('/', HelloWorld.index)
route_map += Route('/hello/world', HelloWorld.index)
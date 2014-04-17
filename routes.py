from mvc.routing.route import Route
from helloworld import HelloWorld

route_table = Route()

route_table += Route('', HelloWorld.index)
route_table += Route('/hello/world' HelloWorld.index)
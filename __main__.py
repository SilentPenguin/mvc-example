import sys
sys.path.append('/Users/seppy/Documents')

import routes
from mvc.wsgi.interface import Interface, TestServer

interface = Interface()

if __name__ == '__main__':
    server = TestServer(interface)
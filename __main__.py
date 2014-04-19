import sys
sys.path.append('/Users/seppy/Documents')

import routes
from mvc.application.application import Application

app = Application(run_server = __name__ is '__main__')
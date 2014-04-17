import sys
sys.path.append('/Users/seppy/Documents')

from mvc.wsgi.interface import Interface
import settings

interface = Interface(settings)
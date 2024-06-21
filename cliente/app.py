

import os, sys, threading

from PyQt5.QtWidgets import QApplication

from src.socket.connect import Manager_connect
from src.main import VPrincipal


obj = Manager_connect()


def load_ui():
    app = QApplication(sys.argv)
    my_app = VPrincipal(obj)
    my_app.show()
    sys.exit(app.exec_())


obj.start()

print (obj.is_alive())


try:
    load_ui()
except:
    obj.close_connexion()

























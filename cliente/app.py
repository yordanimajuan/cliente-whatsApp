

import os, sys, threading

from PyQt5.QtWidgets import QApplication

from src.socket.connect import Manager_connect
from src.main import VPrincipal



def load_ui():
    app = QApplication(sys.argv)
    my_app = VPrincipal()
    my_app.show()
    sys.exit(app.exec_())

load_ui()


























import sys, os

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow



class VPrincipal(QMainWindow):
	
    def __init__(self,con):
        super(VPrincipal, self).__init__()
        path = os.getcwd() + '/src/ui/principal.ui'
        loadUi(path  ,self)

        self.con_server = con
        
        
        self.lineEdit.returnPressed.connect(self.load_msg)

        

    def clear_text(self):
        self.lineEdit.clear()

    def load_msg(self):
    
        text = self.lineEdit.text()+'\n'

        if self.con_server.send_msg(text):

            self.textBrowser.append('''
            <style>
                .burbuja{          
                    font-size:12px;
                    color: #fff;
                    text-align:left;         
                    margin: 5 50 10 5;
                    background-color:#00aa7f;
                }                                        
            </style>
            <body>            
                <div class="cuerpo_msj">
                    <div class="burbuja">
                    '''+text+'''
                    </div>
                </div>        
            </body>
            ''')  
        self.clear_text()
    



import sys, os

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow



class VPrincipal(QMainWindow):
	
    def __init__(self):
        super(VPrincipal, self).__init__()
        path = os.getcwd() + '/src/ui/principal.ui'
        loadUi(path  ,self)
        
        
        self.lineEdit.returnPressed.connect(self.load_msg)


    def load_msg(self):
        print ('enviado')
        text = self.lineEdit.text()+'\n'

        self.textBrowser.insertHtml('''
      <style>

        .burbuja{
          padding:10 10 10 10;
          background-color:#00aa7f;
          border:2px solid #666666;
          font-size:12px;
          color: #fff;
          line-height:1.3em;
                                
          float: left;
                                
          
          position:relative;
          text-align:left;
          width:300px;
          
          border-radius: 50%;
          margin: 5 50 10 5;
          margin-left: -20px;
          border-width:15px 30px 15px 15px;
        }        
        .tiempo {
          width: 80%;
          height: 50px;
          float: left;
          padding: 10px; /* 10px padding */
          border: 2px solid red;
        }               
      </style>
      <body>            
          <div class="cuerpo_msj">
            <div class="burbuja">
              '''+text+'''
            </div>
            <span class="tiempo"><i class="icon-clock"></i> hace 15 min</span>
          </div>        
      </body>
      ''')

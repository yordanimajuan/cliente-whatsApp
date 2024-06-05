

from PyQt5.uic import loadUi
from PyQt5 import QtCore
#from PyQt5.QtWidgets import QMainWindow, QApplication,  Qt
from PyQt5.QtWidgets import * 





app = QApplication([])
ui = loadUi('./src/ui/principal.ui')

#ui.textBrowser.setSource(QtCore.QUrl.fromLocalFile("./src/index.html"))

def send_msg():
    print ('enviado')
    text  = ui.lineEdit.text()+'\n'
    ui.textBrowser.insertHtml('''
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
        border-color: #ddd !important;
        
        

        
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

    ui.lineEdit.clear()


ui.lineEdit.returnPressed.connect(send_msg)



ui.show()
app.exec()
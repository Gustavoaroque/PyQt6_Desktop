import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,QWidget,QPushButton,QGroupBox,QLabel,QLineEdit,QVBoxLayout,QGridLayout,QHBoxLayout

)

from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QIcon, QFont, QFontDatabase,QPixmap
#from PyQt6.QtGui import QFontDatabase




class LogIn(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.setWindowTitle("Log In")

        layout = QGridLayout()
        layout.setColumnMinimumWidth(0,50)
        layout.setColumnMinimumWidth(1,250)
        layout.setColumnMinimumWidth(2,50)

        layout_form = QGridLayout()
        

        self.setLayout(layout)

        #Import
        QFontDatabase.addApplicationFont("C:\\Users\\Programador_4\\Documents\\Fonts\\static\\Montserrat-Medium.ttf")
        QFontDatabase.addApplicationFont("C:\\Users\\Programador_4\\Documents\\Fonts\\static\\Montserrat-Thin.ttf")

        
        self.label1 = QLabel("Username: ")
        self.label1.setFont(QFont("Montserrat Thin",12))        
        layout_form.addWidget(self.label1,0,0)
        
        # Q
        self.label2 = QLabel("Username: ")
        layout_form.addWidget(self.label2,1,0)
        self.label2.setFont(QFont("Montserrat Medium",12))        
        #label.setFont(QFont("Verdana",20))
        #QFontDatabase.addApplicationFont("RUTA")

        #id = QFontDatabase.addApplicationFont("Ruta")
        #families = QFontDatabase.applicationFontFamilies(id)
        #label.setFont(QFont(families[0],160))

        self.input1 = QLineEdit()
        layout_form.addWidget(self.input1,0,1)
        
        self.input2 = QLineEdit()
        layout_form.addWidget(self.input2,1,1)

        layout.addLayout(layout_form,0,1)

        button = QPushButton("Iniciar Sesion", self)
        button.setStyleSheet("height:30px; width:100px;")
        button2 = QPushButton("Cerrar", self)
        # button.move(50,50) #Moves the button
        # button.clicked #Clicked is a event that trigger a signal, and when this signal is detected will call a 
        # function

        # button.clicked.connect(self.close) #The function .close() will `close` the window

        #button.setFizedSize(width,height) #Change the size of the object button
        #button.setGeometry(x,y,width,height) #Is a setFixedSize and move function togethee
        button.setFixedWidth(100)
        button.clicked.connect(self.change_state)


        layout.addWidget(button,2,1,Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button2,2,2,Qt.AlignmentFlag.AlignCenter)
        
        print(layout.columnCount())
    
    def display(self):
        print(self.input1.text())
        print(self.input2.text())
        # print(self.layout.co)
    
    def change_state(self): 
        print(self)




class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont("C:\\Users\\Programador_4\\Documents\\Fonts\\static\\Montserrat-Medium.ttf")
        QFontDatabase.addApplicationFont("C:\\Users\\Programador_4\\Documents\\Fonts\\static\\Montserrat-Thin.ttf")

        self.setWindowTitle("FreshCut")
        main = QGridLayout()
        navbar = QHBoxLayout()
        FirstTwoTables = QHBoxLayout()

        #Image
        image = QLabel()
        pixmap = QPixmap("C:\\Users\\Programador_4\\Documents\\Programs\\PyQt\\first_test\\azocar_logo.png")  # Replace with your image path
        resize_image = pixmap.scaledToHeight(100)
        image.setPixmap(resize_image)

        #LogOut Btn 
        logOut_btn = QPushButton("Log Out")
        logOut_btn.setStyleSheet("height:30px; width:100px;")
        logOut_btn.clicked.connect(self.close)


        com_box = QGroupBox()
        com_box.setStyleSheet("QGroupBox { border: 1px solid blue; border-radius: 20px;}")  # Add border style
        com_box.setFixedHeight(250)
        com_box.setFixedWidth(600)

        plu_box = QGroupBox()
        plu_box.setStyleSheet("QGroupBox { border: 1px solid blue; border-radius: 20px;}")  # Add border style
        plu_box.setFixedHeight(250)
        plu_box.setFixedWidth(600)
        # self.label1.setFont(QFont("Montserrat Thin",12))        

        chart_com = QVBoxLayout()
        chart_plu = QVBoxLayout()

        #Items COM
        label_com = QLabel("Estado de Comunicacion: Habilitado")
        start_com= QPushButton("Inicar comunicacion")
        close_com = QPushButton("Cerrar comunicacion")
        close_com.setFixedWidth(200)
        start_com.setFixedWidth(200)
        close_com.setStyleSheet("height:60px;width:300px;")
        start_com.setStyleSheet("height:60px;width:300px;")

        #Items PLU
        label_plu = QLabel("Datos PLU:")
        update_plu= QPushButton("Actualizar PLU")
        delete_plu = QPushButton("Borrar PLU")
        update_plu.setFixedWidth(200)
        delete_plu.setFixedWidth(200)
        update_plu.setStyleSheet("height:60px;width:300px;")
        delete_plu.setStyleSheet("height:60px;width:300px;")

        #Comm Button Section
        btn_section_com = QHBoxLayout()
        # btn_section_com.addStretch(1)
        btn_section_com.addWidget(start_com)
        # btn_section_com.addStretch(1)
        btn_section_com.addWidget(close_com)
        # btn_section_com.addStretch(1)
        
        #PLU buttons Section
        btn_section_plu = QHBoxLayout()
        # btn_section_plu.addStretch(1)
        btn_section_plu.addWidget(update_plu)
        # btn_section_plu.addStretch(1)
        btn_section_plu.addWidget(delete_plu)
        # btn_section_plu.addStretch(1)

        btn_section_plu.setContentsMargins(20,20,20,20)
        btn_section_com.setContentsMargins(20,20,20,20)
        # Adding to The layout
        chart_com.addWidget(label_com)
        chart_com.addLayout(btn_section_com)

        #Adding to the layout
        chart_plu.addWidget(label_plu)
        chart_plu.addLayout(btn_section_plu)

        #Grouping
        com_box.setLayout(chart_com)
        plu_box.setLayout(chart_plu)

        # FirstTwoTables.addStretch(1)
        FirstTwoTables.addWidget(com_box)
        # FirstTwoTables.addStretch(1)
        FirstTwoTables.addWidget(plu_box)
        # FirstTwoTables.addStretch(1)
        

        navbar.addWidget(image)
        navbar.addStretch(1)
        navbar.addWidget(logOut_btn)

        main.addLayout(navbar,0,0)
        main.addLayout(FirstTwoTables,1,0)
        self.setLayout(main)



app= QApplication(sys.argv)
app.setStyleSheet("""
                  
    LogIn {
                  background-color:#fbfbf2;
    }
                    """)

window = HomePage()
window.showFullScreen()
sys.exit(app.exec())



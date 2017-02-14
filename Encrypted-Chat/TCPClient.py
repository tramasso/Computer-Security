import socket
from threading import Thread
from PyQt4 import QtCore, QtGui
import sys
import os
import SDES
import RC4
ip = '' #PlainText
key = '' #PlainText_3
port = ''
nick = '' #PlainText_4
text = '' #PlainText_5
nick2 = ''
cript = 'SDES'
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_first(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, first):
        first.setObjectName(_fromUtf8("first"))
        first.resize(430, 220)

        self.textBrowser = QtGui.QTextBrowser(first)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.lineEdit = QtGui.QLineEdit(first)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 141, 21))
        self.lineEdit.insert(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit_2 = QtGui.QLineEdit(first)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 60, 81, 21))
        self.lineEdit_2.insert(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        #self.pushButton_2 = QtGui.QPushButton(first)
        #self.pushButton_2.setGeometry(QtCore.QRect(310, 370, 91, 31))
        #self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #self.pushButton_2.clicked.connect(lambda: inicia())
        self.lineEdit_3 = QtGui.QLineEdit(first)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 100, 181, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.lineEdit_4 = QtGui.QLineEdit(first)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 100, 151, 21))
        self.lineEdit_4.insert(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.label = QtGui.QLabel(first)
        self.label.setGeometry(QtCore.QRect(20, 60, 21, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(first)
        self.label_2.setGeometry(QtCore.QRect(235, 60, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(first)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 31, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(first)
        self.label_4.setGeometry(QtCore.QRect(235, 100, 41, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        #self.lineEdit_5 = QtGui.QLineEdit(first)
        #self.lineEdit_5.setGeometry(QtCore.QRect(10, 330, 291, 71))
        #self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.label_5 = QtGui.QLabel(first)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 400, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(first)
        self.label_6.setGeometry(QtCore.QRect(100, 150, 400, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))

       	self.label_7 = QtGui.QLabel(first)
       	self.label_7.setGeometry(QtCore.QRect(50,120,120,20))
       	self.label_7.setObjectName(_fromUtf8("label_7"))

       	self.font = QtGui.QFont()
       	self.font.setPointSize(11)
       	self.label_7.setFont(self.font)

        self.pushButton = QtGui.QPushButton(first)
        self.pushButton.setDefault(True)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 70, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: startConnection())
        self.pushButton.setStyleSheet("background-color: cyan")

        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)
        self.lineEdit_3.returnPressed.connect(self.pushButton.click)
        self.lineEdit_4.returnPressed.connect(self.pushButton.click)

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        first.setWindowTitle(_translate("first", "Chat Criptografado", None))
        self.textBrowser.setHtml(_translate("first", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		"p, li { white-space: pre-wrap; }\n"
		"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
		"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
     
        self.pushButton.setText(_translate("first", "Conectar", None))
        #self.pushButton_2.setText(_translate("first", "Send(RC4)", None))
        self.label.setText(_translate("first", "IP:", None))
        self.label_2.setText(_translate("first", "Port:", None))
        self.label_3.setText(_translate("first", "Key:", None))
        self.label_4.setText(_translate("first", "Nick:", None))
        self.label_5.setText(_translate("first","Preencha os campos abaixo para estabelecer a conexao: ",None))
        self.label_7.setText(_translate("first","Minimo 2 caracteres",None))
    
    def newWindow3(self,s):
        self.window3 = Ui_ChatCriptografado(s)
        #self.window3.closed.connect(self.close)
        self.window3.show()
        self.hide()


class Ui_ChatCriptografado(QtGui.QWidget):
    closed = QtCore.pyqtSignal()
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self,s):
        QtGui.QWidget.__init__(self)
        self.setupUi(self,s)

   

    def setupUi(self, ChatCriptografado,s):
    	self.sockt = s

        ChatCriptografado.setObjectName(_fromUtf8("ChatCriptografado"))
        ChatCriptografado.resize(430, 400)

        self.textBrowser = QtGui.QTextBrowser(ChatCriptografado)
        self.textBrowser.setGeometry(QtCore.QRect(15, 30, 400, 250))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

       

        self.pushButton = QtGui.QPushButton(ChatCriptografado)
        self.pushButton.setGeometry(QtCore.QRect(310, 295, 100, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
       
        menu = QtGui.QMenu()
        menu.addAction('SDES',self.selectSDES)
        menu.addAction('RC4',self.selectRC4)
        self.pushButton.setMenu(menu)

        self.pushButton_2 = QtGui.QPushButton(ChatCriptografado)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 335, 90, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: sendMessage(self.sockt))


        self.PlainTextEdit = QtGui.QPlainTextEdit(ChatCriptografado)
        self.PlainTextEdit.setGeometry(QtCore.QRect(15, 300, 290, 80))
        self.PlainTextEdit.setObjectName(_fromUtf8("textEdit"))

        self.pushButton_3 = QtGui.QPushButton(ChatCriptografado)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 0, 50, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3.clicked.connect(lambda: self.changeKey())


        self.label_2 = QtGui.QLabel(ChatCriptografado)
        self.label_2.setGeometry(QtCore.QRect(20, 5, 70, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))


        self.lineEdit = QtGui.QLineEdit(ChatCriptografado)
        self.lineEdit.setGeometry(QtCore.QRect(90, 5, 260, 20))
        self.lineEdit.insert(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.pushButton_3.click)

        self.retranslateUi(ChatCriptografado)
        QtCore.QMetaObject.connectSlotsByName(ChatCriptografado)

    def retranslateUi(self, ChatCriptografado):
        ChatCriptografado.setWindowTitle(_translate("ChatCriptografado", "ChatCriptografado", None))
        self.textBrowser.setHtml(_translate("ChatCriptografado", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
	"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
	"p, li { white-space: pre-wrap; }\n"
	"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.pushButton.setText(_translate("ChatCriptografado", "SDES", None))
        self.pushButton_2.setText(_translate("ChatCriptografado", "Send", None))
        self.pushButton_3.setText(_translate("ChatCriptografado","OK",None))

        self.label_2.setText(_translate("ChatCriptografado","Mudar Key: ",None))

    def selectSDES(self):
        self.pushButton.setText(_translate("ChatCriptografado","SDES",None))
        global cript
        cript = 'SDES'
    def selectRC4(self):
        self.pushButton.setText(_translate("ChatCriptografado","RC4",None))
        global cript
        cript = 'RC4'
    def closeEvent(self,event):
        self.closed.emit()
        event.accept 
        self.sockt.close()
        os._exit(1)
    def changeKey(self):
    	global key
    	key = self.lineEdit.displayText()
    	self.lineEdit.clear()
    def setText(self,text):
        self.textBrowser.append(text)





	

def sendMessage(s):
		
		encMessage = ''
		message = str(ex.window3.PlainTextEdit.toPlainText())
		if (cript == 'SDES'):
			encMessage = SDES.encryptMessage(str(key),message)
		if(cript == 'RC4'):
			encMessage = RC4.RC4(str(key),message)
		s.send(encMessage)
		ex.window3.textBrowser.append("<div style='color:green;'>Sent: </div>" + message  )
		ex.window3.PlainTextEdit.clear()

def receiveMessage(s):

	while True:

		data = s.recv(1024)
		if not data:
			break

		message = str(data)
		
		if (cript == 'SDES'):
			decMessage = SDES.decryptMessage(str(key),message)
		if(cript == 'RC4'):
			decMessage = RC4.RC4(str(key),message)
		ex.window3.textBrowser.append("<div style='color:red;'>Received: </div>" + decMessage )
	s.close()	

def Connect():
	global nick2
	global nick
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind(('0.0.0.0',int(port)))
		s.listen(1)
		c, addr = s.accept()
		ex.hide()
		ex.newWindow3(c)
	
		ex.window3.textBrowser.append("Connection from: "  + str(addr) )
		#print ("Connection from: " + str(addr))

		t1 = Thread( target = receiveMessage, args = (c,)).start()
		#t2 = Thread( target = sendMessage, args = (c,)).start()
	except:

		s.connect((str(ip),int(port)))
		addr = (str(ip),int(port))
		#ex.closeWindow2()
		ex.hide()
		ex.newWindow3(s)

		ex.window3.textBrowser.append("Connected to: " + str(addr))
		#print ("Connected to: " + str(addr))

		t1 = Thread( target = receiveMessage, args = (s,)).start()
		#t2 = Thread( target = sendMessage, args = (s,)).start()

def startConnection():
    global ip
    ip = ex.lineEdit.displayText()
    global port
    port = ex.lineEdit_2.displayText()
    global key 
    key = ex.lineEdit_3.displayText()
    global nick
    nick = ex.lineEdit_4.displayText()
    if(ip != '' and port != ''and key != ''and nick != '' and len(key) > 1):
    	
        Connect()

    


    else:
        ex.label_6.setText(_translate("firstConnection","<font style='color: red;'>Por favor preencha todos os campos acima</font>",None))
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_first()
    ex.show()

    
   
    sys.exit(app.exec_())


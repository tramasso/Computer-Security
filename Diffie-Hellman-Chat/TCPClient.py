import socket
from threading import Thread
from PyQt4 import QtCore, QtGui
from diffie import diffieHellman
from Gui import Ui_ChatCriptografado
import sys
import os
import RC4
ip = '' #PlainText
key = '' #PlainText_3
port = ''
text = '' #PlainText_5
#cript = 'RC4'
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

        self.label = QtGui.QLabel(first)
        self.label.setGeometry(QtCore.QRect(20, 60, 21, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(first)
        self.label_2.setGeometry(QtCore.QRect(235, 60, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_5 = QtGui.QLabel(first)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 400, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(first)
        self.label_6.setGeometry(QtCore.QRect(100, 150, 400, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))


        self.pushButton = QtGui.QPushButton(first)
        self.pushButton.setDefault(True)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 70, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: startConnection())
        self.pushButton.setStyleSheet("background-color: cyan")

        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)
  

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

        self.label_5.setText(_translate("first","Preencha os campos abaixo para estabelecer a conexao: ",None))
       
    
    def newWindow3(self,s):
        self.window3 = Ui_ChatCriptografado(s,key)
        #self.window3.closed.connect(self.close)
        self.window3.show()
        self.hide()




def receiveMessage(s):

	while True:

		data = s.recv(1024)
		if not data:
			break

		message = str(data)
		decMessage = RC4.RC4(str(key),message)
		ex.window3.textBrowser.append("<div style='color:red;'>Received: </div>" + decMessage )
	s.close()	

def Connect():

	global key
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dh = diffieHellman()
	try:
		s.bind(('',int(port)))
		s.listen(1)
		c, addr = s.accept()
		ex.hide()
		

		

		ya = dh.getY()
		c.send(str(ya))
		yb = long(c.recv(1024))
		key = dh.getKey(yb)
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


		ya = dh.getY()
		s.send(str(ya))
		yb = long(s.recv(1024))
		key = dh.getKey(yb)
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
    if(ip != '' and port != ''):
    	
        Connect()

    


    else:
        ex.label_6.setText(_translate("firstConnection","<font style='color: red;'>Por favor preencha todos os campos acima</font>",None))
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_first()
    ex.show()

    
   
    sys.exit(app.exec_())


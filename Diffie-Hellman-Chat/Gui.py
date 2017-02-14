import socket
from PyQt4 import QtCore, QtGui
import os
import RC4

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

class Ui_ChatCriptografado(QtGui.QWidget):
    closed = QtCore.pyqtSignal()
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self,s,k):
        QtGui.QWidget.__init__(self)
        self.setupUi(self,s,k)

   
    def setupUi(self, ChatCriptografado,s,k):
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
        menu.addAction('RC4',self.selectRC4)
        self.pushButton.setMenu(menu)

        self.pushButton_2 = QtGui.QPushButton(ChatCriptografado)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 335, 90, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(lambda: self.sendMessage(k))


        self.PlainTextEdit = QtGui.QPlainTextEdit(ChatCriptografado)
        self.PlainTextEdit.setGeometry(QtCore.QRect(15, 300, 290, 80))
        self.PlainTextEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(ChatCriptografado)
        QtCore.QMetaObject.connectSlotsByName(ChatCriptografado)

    def retranslateUi(self, ChatCriptografado):
        ChatCriptografado.setWindowTitle(_translate("ChatCriptografado", "ChatCriptografado", None))
        self.textBrowser.setHtml(_translate("ChatCriptografado", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
	"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
	"p, li { white-space: pre-wrap; }\n"
	"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
	"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

        self.pushButton.setText(_translate("ChatCriptografado", "RC4", None))
        self.pushButton_2.setText(_translate("ChatCriptografado", "Send", None))
     
    
    def selectRC4(self):
        self.pushButton.setText(_translate("ChatCriptografado","RC4",None))

    def closeEvent(self,event):
        self.closed.emit()
        event.accept 
        self.sockt.close()
        os._exit(1)
    def setText(self,text):
        self.textBrowser.append(text)


    def sendMessage(self,key):
		s = self.sockt
		encMessage = ''
		message = str(self.PlainTextEdit.toPlainText())
		encMessage = RC4.RC4(str(key),message)
		s.send(encMessage)
		self.textBrowser.append("<div style='color:green;'>Sent: </div>" + message  )
		self.PlainTextEdit.clear()
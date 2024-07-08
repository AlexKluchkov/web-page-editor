from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMenuBar, QMenu

#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import os
import sys

class Ui_MainWindow(object):
    path = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 851, 641))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuweb_site = QtWidgets.QMenu(self.menubar)
        self.menuweb_site.setObjectName("menuweb_site")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionSave_as.setFont(font)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCreate_new_page = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_page.setObjectName("actionCreate_new_page")
        self.actionChange_option = QtWidgets.QAction(MainWindow)
        self.actionChange_option.setObjectName("actionChange_option")
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_as)
        self.menuweb_site.addAction(self.actionCreate_new_page)
        self.menuweb_site.addAction(self.actionChange_option)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuweb_site.menuAction())

        self.addFunction()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuweb_site.setTitle(_translate("MainWindow", "web site"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCreate_new_page.setText(_translate("MainWindow", "Create new page"))
        self.actionChange_option.setText(_translate("MainWindow", "Change option"))

    def addFunction(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.save_as_file)
        self.actionCreate_new_page.triggered.connect(self.CreateWebPage)


    def CreateWebPage(self):
        main_text = self.textEdit.toPlainText()
        file = open('index.html', 'w')
        file.write("<!DOCTYPE html>\n")
        file.write("    <html>\n")
        file.write("        <head>\n")
        file.write("            <meta charset=\"utf-8\">\n")
        file.write("            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        file.write("            <meta name=\"keywords\" content=\"вебсайт\">\n")
        file.write("            <title>New website</title>\n")
        file.write("        </head>\n")
        file.write("        <body>\n")
        file.write("            <p>" + str(main_text) + "</p>")
        file.write("        </body>\n")
        file.write("    </html>\n")
        file.close()

    def save_file(self):
        if(path == ""):
            path, _ = QFileDialog.getSaveFileName()
        save_as_file()

    def save_as_file(self):
        f = open(path, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()

    def open_file(self):
        options = QFileDialog.getOpenFileName()[0]
        if(options == ""):
            return 0
        f = open(options, 'r')
        self.textEdit.setText(f.read())
        f.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
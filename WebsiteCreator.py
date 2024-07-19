from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMenuBar, QMenu

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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setGeometry(QtCore.QRect(40, 90, 800, 501))
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
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_as)
        self.menuweb_site.addAction(self.actionCreate_new_page)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuweb_site.menuAction())

        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(40, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

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
        self.label.setText(_translate("Form", "Website title"))
        self.label_2.setText(_translate("Form", "Website header"))

    def addFunction(self):
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.save_as_file)
        self.actionCreate_new_page.triggered.connect(self.CreateWebPage)


    def CreateWebPage(self):
        main_text = self.textEdit.toPlainText()
        web_site_title = "New web site title"
        web_site_header = "new web site header"
        if(self.lineEdit.text() != ""):
            web_site_title = self.lineEdit.text()
        if(self.lineEdit_2.text() != ""):
            web_site_header = self.lineEdit_2.text()
        self.CreateHTMLfile(main_text, web_site_title, web_site_header)
        self.CreateCSSfile()

    def CreateHTMLfile(self, MainText, web_site_title, web_site_header):
        file = open('index.html', 'w')
        file.write("<!DOCTYPE html>\n")
        file.write("    <html>\n")
        file.write("        <head>\n")
        file.write("            <meta charset=\"utf-8\">\n")
        file.write("            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        file.write("            <meta name=\"keywords\" content=\"website\">\n")
        file.write("            <title>"+ web_site_title +"</title>\n")
        file.write("            <link rel=\"stylesheet\" href=\"main.css\" />")
        file.write("        </head>\n")
        file.write("        <body>\n")
        file.write("            <div id=\"header\">")
        file.write("                <h1>")
        file.write("                    " + web_site_header)
        file.write("                </h1>")
        file.write("            </div>")
        file.write("            <div id=\"main\">")
        file.write("                <p>" + str(MainText) + "</p>")
        file.write("            </div>")
        file.write("        </body>\n")
        file.write("    </html>\n")
        file.close()

    def CreateCSSfile(self):
        file = open('main.css', 'w')
        file.write("*{ margin:0; padding:0; }\n")
        file.write("body { background-color: #3f4849; }")
        file.write("#main { background-color: #ffffff; height: auto; min-width: 1140px; margin-left: 350px; margin-right: 350px; margin-bottom: 50px; border: 3px solid silver; }")
        file.write("#header { height: 50px; width: 100%; text-align: center; background-color: orange; margin-bottom: 25px;}")
    def save_file(self):
        if(path == ""):
            path, _ = QFileDialog.getSaveFileName()
        save_as_file()

    def save_as_file(self):
        f = open(path, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()

    def open_file(self):
        options = QFileDialog.getOpenFileName(self.centralwidget, 'Open file', '', 'txt (*.txt);; docx(*.docx)')[0]
        if(options == ""):
            return 0
        f = open(options, 'r')
        self.textEdit.setText(f.read())
        f.close()

    def set_web_site_title(self, title):
        self.web_site_title = title

    def set_web_site_header(self, header):
        self.web_site_header = header

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

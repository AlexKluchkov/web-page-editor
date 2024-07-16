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
        MainWindow.setCentralWidget(self.textEdit)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
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
        self.CreateHTMLfile(main_text)
        self.CreateCSSfile()

    def CreateHTMLfile(self, MainText):
        file = open('index.html', 'w')
        file.write("<!DOCTYPE html>\n")
        file.write("    <html>\n")
        file.write("        <head>\n")
        file.write("            <meta charset=\"utf-8\">\n")
        file.write("            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
        file.write("            <meta name=\"keywords\" content=\"вебсайт\">\n")
        file.write("            <title>New website</title>\n")
        file.write("            <link rel=\"stylesheet\" href=\"main.css\" />")
        file.write("        </head>\n")
        file.write("        <body>\n")
        file.write("            <div id=\"header\">")
        file.write("                <h1>")
        file.write("                    new web site")
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
        file.write("body { background-color: #AFEEEE; }")
        file.write("#main { background-color: white; height: auto; min-width: 1140px; margin-left: 350px; margin-right: 350px; margin-bottom: 50px; border: 3px solid silver; }")
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



class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        ClssDialog.resize(self, 440, 350)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnSave)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Change option")
        self.pushButton.setText("Save option")

    def btnSave(self):
        self.close()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.ui.actionChange_option.triggered.connect(self.openDialog)

    def openDialog(self):
        dialog = ClssDialog(self)
        dialog.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())

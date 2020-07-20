#obtained from https://stackoverflow.com/questions/43011228/how-can-i-click-a-pushbutton-on-my-pyqt5-code-and-allow-it-to-execute-run-anothe

from PyQt5 import QtCore, QtGui, QtWidgets
import randomArt
from artScreen import artScreen
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Help"))

        # When push button it runs open_file which runs stroopy
        self.pushButton.clicked.connect(self.open_file)
    
    def open_file(self):
        art_screen_size = [526,526]
        screen = artScreen(art_screen_size)
        screen.updateScreen(randomArt.randomArt(art_screen_size))
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
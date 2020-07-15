import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
import stroopy_words

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
       
        self.setWindowTitle('Main Program')
        self.resize(800, 400)
        self.setStyleSheet("QMainWindow { background-color: black; color: white }")
       
        label = QLabel('This is the main program window')
        label.setStyleSheet("QLabel { color: white }")
        btn1 = QPushButton('Set Baseline')
        btn2 = QPushButton('Start')
        btn1.setStyleSheet("QPushButton { max-width: 15em}")
        btn2.setStyleSheet("QPushButton { max-width: 15em}")
        
        layout1 = QVBoxLayout()
    
        layout2 = QHBoxLayout()
        layout2.addWidget(btn1)
        layout2.addWidget(btn2)

        layout1.addWidget(label)
        layout1.addLayout(layout2)

        self.widget = QWidget()
        self.widget.setLayout(layout1)
        self.setCentralWidget(self.widget)
        
        btn1.clicked.connect(self.showBaseline)
        btn2.clicked.connect(self.showDialog)
 
    def showBaseline(self):
        stroopy_words.main()

    def showDialog(self):
        DispDlg = QDialog(self)
        DispDlg.setWindowTitle("Display")
        DispDlg.resize(300, 300)
        DispDlg.exec_()
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
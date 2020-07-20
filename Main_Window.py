import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QInputDialog
from Image_Manipulation.artScreen import artScreen
from Image_Manipulation.randomArt import randomArt
import stroopy_words
import record

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
        
        btn1.clicked.connect(self.RecordBaseline)
        btn2.clicked.connect(self.open_artScreen)
    

    def open_artScreen(self):
        art_screen_size = [526,526]
        screen = artScreen(art_screen_size)
        screen.updateScreen(randomArt(art_screen_size))

    def RecordBaseline(self):
        default = 120
        minTime = 5
        maxTime = 300
        increment = 5
        time,ok = QInputDialog.getInt(self, "Enter recording duration", "Time (s):", default, minTime, maxTime, increment)
        if ok:
            record.record(time, 'csvtest.txt')
            stroopy_words.present(time)

    #def showWords(self):
    #    stroopy_words.present(time)
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
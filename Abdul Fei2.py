from PyQt5.QtWidgets import QMainWindow,QWidget, QApplication, QPushButton, QLabel
app = QApplication([])
window = QMainWindow()
label =QLabel(window)
label.setText("Label1")
label.move(200, 0)
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()
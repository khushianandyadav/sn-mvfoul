from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Test PyQt5 Window')
layout = QVBoxLayout()
label = QLabel('If you see this, PyQt5 works fine!')
layout.addWidget(label)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())

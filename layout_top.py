import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Layout at the Top Example")

    layout = QVBoxLayout()

    top_layout = QVBoxLayout()  # Create the layout you want to place at the top

    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")

    top_layout.addWidget(button1)
    top_layout.addWidget(button2)

    layout.addLayout(top_layout)  # Add the top layout to the main layout

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

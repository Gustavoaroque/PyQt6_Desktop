import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Image Resize Example")

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout()

    image_label = QLabel()

    original_pixmap = QPixmap("C:\\Users\\Programador_4\\Documents\\Programs\\PyQt\\first_test\\azocar_logo.png")  # Replace with your image path
    resized_pixmap = original_pixmap.scaledToWidth(200)  # Replace 200 with the desired width

    image_label.setPixmap(resized_pixmap)
    layout.addWidget(image_label)

    central_widget.setLayout(layout)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

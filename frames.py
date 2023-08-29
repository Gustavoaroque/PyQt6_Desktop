import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QFrame

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Layout Border Example")

    layout = QVBoxLayout()

    # Create a QFrame to wrap the layout
    frame = QFrame()
    frame.setFrameShape(QFrame.Shape.Box)
    frame.setLineWidth(2)  # Border width
    frame.setStyleSheet("border-color: blue;")  # Border color

    inner_layout = QVBoxLayout()

    inner_layout.addWidget(QWidget())  # Example widget inside the layout

    frame.setLayout(inner_layout)  # Set the inner layout on the frame
    layout.addWidget(frame)  # Add the frame to the main layout

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

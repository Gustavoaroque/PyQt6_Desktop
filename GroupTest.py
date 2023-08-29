import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGroupBox, QLabel, QPushButton

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Styling QGroupBox")

    layout = QVBoxLayout()

    group_box = QGroupBox("Group Box Title")
    group_box.setStyleSheet("QGroupBox { border: 2px solid blue; border-radius: 5px; }")  # Add border style

    inner_layout = QVBoxLayout()

    label = QLabel("Label inside the group box")
    button = QPushButton("Button inside the group box")

    inner_layout.addWidget(label)
    inner_layout.addWidget(button)

    group_box.setLayout(inner_layout)  # Set inner layout for the group box

    layout.addWidget(group_box)  # Add the group box to the main layout

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QR Wi-Fi Reader")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout for central widget
        layout = QVBoxLayout()

        # Label for welcome message
        label = QLabel("Welcome to QR Wi-Fi Reader", self)
        label.setStyleSheet("font-size: 18px;")
        layout.addWidget(label)

        # Button to scan QR code
        scan_button = QPushButton("Scan QR Code", self)
        scan_button.clicked.connect(self.scan_qr)  # Conecta a la función scan_qr
        layout.addWidget(scan_button)

        # Set layout for central widget
        central_widget.setLayout(layout)

    def scan_qr(self):
        # This function will be called when the button is clicked
        print("Scan QR button clicked!")

    def run(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.run()
    sys.exit(app.exec_())

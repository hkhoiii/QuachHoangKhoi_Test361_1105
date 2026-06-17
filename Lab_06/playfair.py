import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.playfair_cipher import Ui_MainWindow  # Import giao diện đã thiết kế

# 1. Thuật toán Playfair của bạn đặt ở đây
def encrypt_playfair(text, key):
    # Logic mã hóa của bạn tại đây
    return f"Ciphertext của '{text}' với key '{key}'"

def decrypt_playfair(text, key):
    # Logic giải mã của bạn tại đây
    return f"Plaintext của '{text}' với key '{key}'"

# 2. Lớp điều khiển giao diện
class PlayfairWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện nút bấm
        self.ui.pushButton.clicked.connect(self.handle_encrypt)
        self.ui.pushButton_2.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        text = self.ui.textEdit.toPlainText()
        key = self.ui.textEdit_2.toPlainText()
        result = encrypt_playfair(text, key)
        self.ui.textEdit_4.setPlainText(result) # Hiển thị ra ô Cipher text

    def handle_decrypt(self):
        text = self.ui.textEdit_3.toPlainText()
        key = self.ui.textEdit_2.toPlainText() # Hoặc ô key khác nếu bạn thiết kế riêng
        result = decrypt_playfair(text, key)
        self.ui.textEdit_2.setPlainText(result) # Hiển thị kết quả

# 3. Khởi chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairWindow()
    window.show()
    sys.exit(app.exec_())
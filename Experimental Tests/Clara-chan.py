import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsOpacityEffect, QSystemTrayIcon
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QTimer, QRect

class ClaraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clara")
        self.setGeometry(100, 100, 300, 200)

        self.icon_label = QLabel(self)
        self.icon_label.setGeometry(10, 10, 30, 30)
        self.icon_label.setPixmap(QPixmap("icon.png"))
        self.icon_label.mousePressEvent = self.toggle_sprite

        self.sprite_label = QLabel(self)
        self.sprite_label.setGeometry(50, 50, 200, 150)
        self.sprite_label.setPixmap(QPixmap("dance.gif"))
        self.sprite_label.hide()

        self.sprite_opacity = QGraphicsOpacityEffect()
        self.sprite_label.setGraphicsEffect(self.sprite_opacity)
        self.sprite_opacity.setOpacity(0.9)

        self.sprite_visible = False

    def toggle_sprite(self, event):
        if not self.sprite_visible:
            self.sprite_label.show()
            self.sprite_visible = True
        else:
            self.sprite_label.hide()
            self.sprite_visible = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clara_app = ClaraApp()
    clara_app.show()
    sys.exit(app.exec())

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider

class YourWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.volume_label = QLabel("Volume: 100%", self)
        self.layout.addWidget(self.volume_label)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(125)
        self.volume_slider.setValue(100)
        self.volume_slider.sliderReleased.connect(self.change_volume)
        self.layout.addWidget(self.volume_slider)

    def change_volume(self):
        volume_value = self.volume_slider.value()
        self.volume_label.setText(f"Volume: {volume_value}%")
        # Your additional logic for handling the volume change goes here

if __name__ == "__main__":
    app = QApplication([])
    widget = YourWidget()
    widget.show()
    app.exec()

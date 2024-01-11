from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QSlider, QLabel
from PySide6.QtGui import QIcon, QPixmap                       
from PySide6.QtCore import Qt
import sys

class MidiPlayer(QMainWindow):                                      
    def __init__(self):                                             
        super().__init__()                                          
                                                                    
        self.setWindowTitle(" Kaboom Symphony (v0.0.1) Alpha")                          
        self.setGeometry(700, 300, 400, 250)                        
                   
        # Set window icon
        my_pixmap = QPixmap(".\icon.png")
        my_icon = QIcon(my_pixmap)
        self.setWindowIcon(my_icon)           
                                                                    
        self.central_widget = QWidget(self)                         
        self.setCentralWidget(self.central_widget)                  

        self.layout = QVBoxLayout(self.central_widget)              

        self.btn_open = QPushButton("Open MIDI File", self)         
        self.btn_open.clicked.connect(self.open_file)               
        self.layout.addWidget(self.btn_open)                        
                                                                    
        self.btn_play = QPushButton("Play", self)                   
        self.btn_play.clicked.connect(self.play_midi)               
        self.layout.addWidget(self.btn_play)                        

        self.btn_stop = QPushButton("Stop", self)                   
        self.btn_stop.clicked.connect(self.stop_midi)               
        self.layout.addWidget(self.btn_stop)                        
                                                                    
        # Volume Slider Widget                                      
        self.volume_label = QLabel("Volume: 100%", self)            
        self.layout.addWidget(self.volume_label)                    
                                                                    
        self.volume_slider = QSlider(Qt.Horizontal, self)           
        self.volume_slider.setMinimum(0)                            
        self.volume_slider.setMaximum(125)                          
        self.volume_slider.setValue(100)                            
        self.volume_slider.valueChanged.connect(self.change_volume) 
        self.layout.addWidget(self.volume_slider)                   
                                                                    
        # Pitch Slider Widget                                       
                                                                    
        self.slider_pitch_bend = QSlider(Qt.Horizontal, self)       
        self.slider_pitch_bend.setMinimum(-8192)                    
        self.slider_pitch_bend.setMaximum(8191)                     
        self.slider_pitch_bend.setValue(0)                          
        self.layout.addWidget(QLabel("Pitch"))                      
        self.layout.addWidget(self.slider_pitch_bend)
        
        # Theme                 
        DefaultDarkTheme = (".\DarkTheme.css")                                  
        self.setStyleSheet(DefaultDarkTheme)
        
        

        
def main():                                                         
    app = QApplication(sys.argv)                                    
    player = MidiPlayer()                                           
    player.show()                                                   
    sys.exit(app.exec())                                            


if __name__ == "__main__":                                          
    main()
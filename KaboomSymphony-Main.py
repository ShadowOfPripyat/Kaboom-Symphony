import sys                                                          
import pygame                                                       
import pygame.midi                                                  
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QSlider, QLabel
from PySide6.QtGui import QIcon, QPixmap                       
from PySide6.QtCore import Qt, QFile, QTextStream                              
                                                                    
                                                                    
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

        # Load theme from External css                                                 
        theme_file = QFile("DarkTheme.css")
        theme_file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(theme_file)
        self.setStyleSheet(stream.readAll())                                                          
                                                                    
        self.file_path = ""                                         
                                                                    
        pygame.init()                                               
        pygame.mixer.init()                                         

    def open_file(self):                                            
        options = QFileDialog.Options()                             
        file_name, _ = QFileDialog.getOpenFileName(                 
            self, "Open MIDI File", "",                             
            "MIDI Files (*.mid);;All Files (*)", options=options    
        )                                                           
                                                                    
        if file_name:                                               
            self.file_path = file_name                              
            pygame.mixer.music.load(self.file_path)                 
            pygame.mixer.music.play()                               
            self.set_pitch_bend()                                   
                                                                    
    def play_midi(self):                                            
        if self.file_path:                                          
            pygame.mixer.music.load(self.file_path)                 
            pygame.mixer.music.play()                               

    def stop_midi(self):                                            
        pygame.mixer.music.stop()                                   
                                                                    
    def change_volume(self):                                        
        volume = self.volume_slider.value()                         
        pygame.mixer.music.set_volume(volume / 100.0)               
        self.volume_label.setText(f"Volume: {volume}%")             
                                                                    
    def set_pitch_bend(self):                                       
        pitch_value = self.slider_pitch_bend.value()                
        pygame.midi.init()                                          
        output = pygame.midi.Output(0)                              
        output.set_instrument(0)                                    
        output.pitch_bend(pitch_value)                              
        output.close()                                              



def main():                                                         
    app = QApplication(sys.argv)                                    
    player = MidiPlayer()                                           
    player.show()                                                   
    sys.exit(app.exec())                                            


if __name__ == "__main__":                                          
    main()                                                           
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import pygame
pygame.init()
pygame.mixer.music.load("mono.mp3")

class xmusic(App):
    def build(self):
        b = BoxLayout(orientation="vertical")
        btn = Button(text="Play",on_press=self.xplay)
        btn2 = Button(text="Stop",on_press=self.xstop)
        b.add_widget(btn)
        b.add_widget(btn2)
        return b
    def xplay(self,instance):
        if pygame.mixer.music.get_busy():
            pass
        else:
            pygame.mixer.music.play()
    def xstop(self,instance):
        pass
        pygame.mixer.music.stop()
    
if __name__=='__main__':
    xmusic().run()
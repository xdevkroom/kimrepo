from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import gps,vibrator,tts,battery
from kivymd.toast import toast
from kivy.network.urlrequest import UrlRequest
import arabic_reshaper
import bidi.algorithm
import webbrowser
from gtts import gTTS as gts
import pygame
pygame.init()
pygame.mixer.music.load("mono.mp3")


g = gts("مرحبا بك في كيفي موبايل لتطوير تطبيقات الاندرويد",lang="ar")
g.save("mono.mp3")
url="http://192.168.43.249/LED=ON"
a = str(battery.status)

class myapp(App):
    
    #tts.speak("hello kivymd مرحبا you welcome")
    toast(a)
    def build(self):
        #webbrowser.open("http://www.google.com")
        
        self.text = "مرحبا"
        self.shape = arabic_reshaper.reshape(self.text)
        self.bi = bidi.algorithm.get_display(self.shape)
        b1=BoxLayout(orientation="vertical")
            
        self.textin=TextInput(text=self.bi,input_type='number',multiline=False,font_name="arial")
        self.label = Label(text=self.bi,font_name="arial")
        butn1= Button(text=self.bi,on_press=self.ledon,font_name="arial")
        butn2= Button(text="Play",on_press=self.xplay)
        butn3= Button(text="Stop",on_press=self.xstop)
        butn4= Button(text="Quick",on_press=self.press)
  
        b1.add_widget(self.textin)
        b1.add_widget(self.label)
        b1.add_widget(butn1)
        b1.add_widget(butn2)
        b1.add_widget(butn3)
        b1.add_widget(butn4)
        
       
        return b1
    def press(self,instance):
        vibrator.vibrate()
        text = self.textin.text
        shape = arabic_reshaper.reshape(text)
        bi = bidi.algorithm.get_display(shape)
        self.label.text=bi
        toast(self.textin.text)
    def ledon(self,instance):
        self.b = UrlRequest(url,verify=False)
    def xplay(self,instance):
        if pygame.mixer.music.get_busy():
            pass
        else:
            pygame.mixer.music.play()
    def xstop(self,instance):
        pygame.mixer.music.stop()
    
            
    

if __name__=='__main__':
     myapp().run()
     
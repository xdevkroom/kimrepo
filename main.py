from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from arabic_reshaper import  reshape
from bidi.algorithm import get_display


sound = SoundLoader.load('club.ogg')
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)


class xmusic(App):
    def build(self):
        b = BoxLayout(orientation="vertical")
        lab = Label(text = self.reshaper("مرحبا بك في بايثون "),font_name="arial")
        btn = Button(text=self.reshaper("تشغيل"),font_name="arial",on_press=self.xplay)
        btn2 = Button(text=self.reshaper("ايقاف"),font_name="arial",on_press=self.xstop)
        b.add_widget(lab)
        b.add_widget(btn)
        b.add_widget(btn2)
        return b
    def xplay(self,instance):
        pass
        sound.play()
    def xstop(self,instance):
        pass
        sound.stop()
    def reshaper(self,text):
        x = reshape(text)
        c =get_display(x)
        return c
        
        
    
if __name__=='__main__':
    xmusic().run()
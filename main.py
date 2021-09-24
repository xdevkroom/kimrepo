from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


sound = SoundLoader.load('./club.ogg')
if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    

class xmusic(App):
    def build(self):
        b = BoxLayout(orientation="vertical")
        btn = Button(text="Play",on_press=self.xplay)
        btn2 = Button(text="Stop",on_press=self.xstop)
        b.add_widget(btn)
        b.add_widget(btn2)
        return b
    def xplay(self,instance):
        pass
        sound.play()
    def xstop(self,instance):
        pass
        sound.stop()
        
    
if __name__=='__main__':
    xmusic().run()
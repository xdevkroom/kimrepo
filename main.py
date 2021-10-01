from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import  Button
from kivy.core.window import Window

class xapp(App):
    def build(self):
        x = Window.size[0]
        y= Window.size[1]
        
        box = BoxLayout(pos=(x/2-400,y/2),spacing=10)
        btn =Button(text="Push",size_hint=(None,None),size=(400,150))
        btn2= Button(text="Pull",size_hint=(None,None),size=(400,150))
        box.add_widget(btn)
        box.add_widget(btn2)
        return box
if __name__=="__main__":
    xapp().run()
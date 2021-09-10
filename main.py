from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.toast import toast
import os
class app(App):
   
    def build(self):
        self.info= """((Welcome to WhatsDirct))\nKSA version\ntobuse this app \nEnter phon number \nfor example:\n05XXXXXXXX"""
    
        box = FloatLayout()
        leb = Label(text= self.info,pos=(600,1500),size_hint=(0.1,.1))
        
        button = Button(text="Start WhatsApp Chat",size_hint=(1,.08),pos=(1,800),on_press=self.click)
        
        img = Image(source="back.jpg",allow_stretch=True,size_hint=(2,2),pos=(-700,0))
        
        self.textinput = TextInput(input_type='number',input_filter="int",size_hint=(1,.1),border=(2,2,2,2),font_size="33sp",multiline=False,pos=(1,900))
        
        box.add_widget(img)
        box.add_widget(leb)
        box.add_widget(self.textinput)
        box.add_widget(button)
      
        return  box
    def click(self,instance):
        toast("Starting...")
        number = str(self.textinput.text)
        number1="966"
        os.system(f"am start -a android.intent.action.VIEW -d https://api.whatsapp.com/send?phone={number1}{number} com.whatsapp")
       
        
    
if __name__=="__main__":
    app().run()

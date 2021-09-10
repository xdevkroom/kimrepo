from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.toast import toast
import os
class app(App):
   
    def build(self):
        self.info= '''((Welcome to WhatsDirct))\nto use this app :\nadd phon number\nwith country \ncode and without\nsymbole + or 00\nfor example :\nCanadian number\n16049008887'''
    
        box = FloatLayout()
        leb = Label(text= self.info,pos=(600,1500),size_hint=(0.1,.1))
        
        button = Button(text="Start WhatsApp Chat",size_hint=(1,.08),pos=(1,800))
        
        img = Image(source="back.jpg",allow_stretch=True,size_hint=(2,2),pos=(-700,0))
        
        self.textinput = TextInput(input_type='number',input_filter="int",size_hint=(1,.1),border=(2,2,2,2),font_size="33sp",multiline=False,pos=(1,900))
        
        box.add_widget(img)
        box.add_widget(leb)
        box.add_widget(self.textinput)
        box.add_widget(button)
        button.bind(on_press=self.click)
        
        return  box
    def click(self,instance):
        pass
        toast("Starting...")
        toast(self.textinput.text)
        input_number = str(self.textinput.text)
        number = f"{input_number}"
        os.system(f"am start -a android.intent.action.VIEW -d https://api.whatsapp.com/send?phone={number} com.whatsapp")
        
if __name__=="__main__":
    app().run()

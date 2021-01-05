#pylint:disable=E1101
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import tts,battery
from kivymd.toast import toast
from kivy.network.urlrequest import UrlRequest
#import requests
from jnius import autoclass,cast

url="http://192.168.43.249/LED=ON"
a = str(battery.status)

PythonActivity = autoclass('org.kivy.android.PythonActivity')
activity = PythonActivity.mActivity
Context = autoclass('android.content.Context')

vibrator_service = activity.getSystemService(Context.VIBRATOR_SERVICE)
vibrator = cast("android.os.Vibrator", vibrator_service)

vibration_effect = autoclass("android.os.VibrationEffect")       

# first argument of createOneShot is the time in ms
# second argument is the amplitude (range from 1 to 255), -1 is device standard amplitude

class myapp(App):
    
    tts.speak("hello kivymd you welcome")
    toast(a)
    def build(self):
       
        b1=BoxLayout(orientation='vertical')
        self.textin=TextInput(text="hello",multiline=False)
        self.label = Label(text="test")
        butn1= Button(text="kivy")
        butn2= Button(text="button")
        butn3= Button(text="layout")
        butn4= Button(text="start")
        butn1.bind(on_press=self.ledon)
        butn4.bind(on_press=self.press)
        b1.add_widget(self.textin)
        b1.add_widget(self.label)
        b1.add_widget(butn1)
        b1.add_widget(butn2)
        b1.add_widget(butn3)
        b1.add_widget(butn4)
        
       
        return b1
    def press(self,instance):
        vibrator.vibrate(vibration_effect.createOneShot(int(500),vibration_effect.DEFAULT_AMPLITUDE))
        
        #vibrator.vibrate(vibration_effect.DEFAULT_AMPLITUDE)
        #vibrator.vibrate()
        self.label.text = self.textin.text
        toast(self.textin.text)
    def ledon(self,instance):
        self.b = UrlRequest(url,verify=False)
    
         
        
                

if __name__=='__main__':
     myapp().run()
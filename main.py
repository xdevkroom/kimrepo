from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.toast import toast
from plyer import battery,tts
from jnius import  autoclass,cast

a = str(battery.status)
class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "50"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        btn_flat.bind(on_press = self.myfunc)
        return screen
    def myfunc(self,any):
        tts.speak(a)
        toast(a)
        DemoApp.vibrating(self)
        
    def vibrating(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity
        Context = autoclass('android.content.Context')

        vibrator_service = activity.getSystemService(Context.VIBRATOR_SERVICE)
        vibrator = cast("android.os.Vibrator", vibrator_service)

        vibration_effect = autoclass("android.os.VibrationEffect")
        return  vibrator.vibrate(vibration_effect.createOneShot(int(500),vibration_effect.DEFAULT_AMPLITUDE))
        
  


DemoApp().run()


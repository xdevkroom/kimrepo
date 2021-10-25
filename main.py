from kivymd .app import MDApp
from kivy.uix.image import Image
from kivymd.toast import toast
from kivymd.uix.textfield import TextInput
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.anchorlayout import AnchorLayout
from kivymd .uix.label import Label
from kivymd.uix.button import MDFillRoundFlatButton,MDRaisedButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget
#from kivymd.utils.fitimage import FitImage
#from jnius import autoclass,cast
from arabic_reshaper import reshape as shape
from bidi.algorithm import get_display as ibidi
#import pysqlite3
"""
try:
    import webbrowser
except:
    pass
"""
#db = pysqlite3.connect("kivy.db")
#cr = db.cursor()
#cr.execute("create table if not exists state(id integer , check_state text,ccode text)")
#cr.execute("insert into state(id,check_state,ccode) values(1,'KSA','+966')")
#cr.execute("update state set check_state='' ,ccode='' where id =1")
#db.commit()
#db.close()

telegram="http://t.me/king_kim"
text2="مرحبا بك في تطبيق واتس اب المباشر"
toolbarx= "واتس اب المباشر"
code_number=""
phone_number=""
message=""

ccode =["KSA","SYR","LBN","JOR","EGY","YEM","IRQ","QTR","KWT","LBY","TUN","TUR","SDN","MAR","BHR","OMN","SOM","PSE","MRT","ALG","UK","USA","CAN","AUS","GER"]

icons =["icons/ksa.png","icons/syr.png","icons/lbn.png","icons/jor.png","icons/egy.png","icons/yem.png","icons/irq.png","icons/qtr.png","icons/kwt.png","icons/lby.png","icons/tun.png","icons/tur.png","icons/sdn.png","icons/mar.png","icons/bhr.png","icons/omn.png","icons/som.png","icons/pse.png","icons/mrt.png","icons/alg.png","icons/uk.png","icons/usa.png","icons/can.png","icons/aus.png","icons/ger.png"]
"""
try:
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass("android.content.Intent")
    Uri = autoclass("android.net.Uri")
    comp = autoclass("android.content.ComponentName")

#Create the intent
    intent = Intent()
    intent.setAction(Intent.ACTION_VIEW)
except:
    pass
"""

class Ar_text(TextInput):
    
    str =""
    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        

    def insert_text(self, substring, from_undo=False):
        self.str = self.str+substring
        self.text = ibidi(shape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)
       

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = ibidi(shape(self.str))

class WhatsappDirct(MDApp):
    def build(self):
        self.box = MDScreen()
        #ancher = AnchorLayout(anchor_x="center",anchor_y="top")
        #mdtoolbar= MDToolbar(title=self.arabic("واتس اب المباشر"),type="top")
        #mdtoolbar.ids.label_title.font_name = "font/mohanad.ttf"
        #mdtoolbar.elevation=12
        
        #ancher.add_widget(mdtoolbar)
        #img = FitImage(source="Back.jpg")
        img2= Image(source="blue.png",pos_hint={"center_x":.5,"center_y":.82},size_hint=(.3,.3))
        #self.theme_cls.theme_style="Dark"
        
        leb= Label(text=self.arabic(text2),font_name="font/arial.ttf",pos_hint={"center_x":.5,"center_y":.7},font_size="13sp")
        
        self.txtin1 = TextInput(size_hint=(.4,.05),hint_text=self.arabic("ادخل رقم الهاتف"),pos_hint={"center_x":.75,"center_y":.575},input_type="number",font_name="font/arial.ttf")
        
 
        
        self.txtin2 = TextInput(size_hint=(.25,.05),hint_text=self.arabic("رمز الدولة"),pos_hint={"center_x":.41,"center_y":.575},input_type="number",font_name="font/arial.ttf")
        #self.txtin2.text=self.getdb()
        
        self.txtin3 = Ar_text(size_hint=(.9,.15),hint_text=self.arabic("اكتب رسالة "),pos_hint={"center_x":.5,"center_y":.43},input_type="number",font_name="font/arial.ttf")
        
        btn1= MDFillRoundFlatButton(text=self.arabic(" ابدأ الدردشة"),text_color=(1,1,1,1),pos_hint={"center_x":.5,"center_y":.27},font_name="font/arial.ttf",on_release=lambda c :print("intent_func"))
        
        btn2=MDFillRoundFlatButton(text=self.arabic("حول التطبيق"),font_name="font/arial.ttf",text_color=(0,0,1,2),pos_hint={"center_x":.5,"center_y":.2},on_release=lambda c:print("dialog_show"))
        
       
        btn3= MDFillRoundFlatButton(text=self.arabic("اختر الرمز"),font_name="font/arial.ttf",text_color=(1,1,1,1),size_hint=(.255,.05),pos_hint={"center_x":.140,"center_y":.575},on_release=self.listitems)
       
        #self.box.add_widget(img)
        #self.box.add_widget(ancher)
        self.box.add_widget(img2)
        self.box.add_widget(leb)
        self.box.add_widget(self.txtin1)
        self.box.add_widget(self.txtin2)
        self.box.add_widget(self.txtin3)
        self.box.add_widget(btn1)
        self.box.add_widget(btn2)
        self.box.add_widget(btn3)
        
        return  self.box
    """       
    def intent_func(self,instance):
            code_number = self.txtin2.text
            phone_number=self.txtin1.text
            recive_text=self.txtin3.text
            message=ibidi(recive_text)
            intent.setData(Uri.parse(f"https://api.whatsapp.com/send?phone={code_number}{phone_number}&text={message}"))
            intent.setPackage("com.whatsapp")
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
            x = self.txtin1.text
            toast(x)
            """
            
    def arabic(self,value):
           text = shape(value)
           arabitext = ibidi(text)
           return  arabitext
           
    #def updatedb(self,check_state,ccode):
           #cr.execute(f"update state set check_state='{check_state}' ,ccode='{ccode}' where id =1")
           #db.commit()
           
    def getdb(self):
           pass
           #cr.execute("select ccode from state")
           #getdata= cr.fetchone()[0]
           #return  getdata
           
    def listitems(self,instance):
            self.mdlis=MDList()
            self.mdlis.md_bg_color=self.theme_cls.primary_dark
            self.scrol = ScrollView(size_hint=(.49,.45),pos_hint={"center_x":.28,"center_y":.775})
            for i in range(len(ccode)):
                iconz= IconLeftWidget(icon=icons[i])
                items = OneLineAvatarIconListItem(text=ccode[i])
                items.add_widget(iconz)
                self.mdlis.add_widget(items)
                items.on_release=lambda x=ccode[i]:self.switch(x)
            self.scrol.add_widget(self.mdlis)
            self.box.add_widget(self.scrol)
            
    def dialog_show(self,instance):
        pass
        
        #self.theme_cls.theme_style="Light"
        #titl = self.arabic("حول التطبيق!")
        #msg = self.arabic(""" 
#        مرحبا بك في تطبيق
#  واتس اب المباشر
#        تم بناء هذا
#        التطبيق بلغة بايثون
 #       اطار عمل kivymd
#        يمكنك ارسال تعليق للمطور
#        عبر منصة تلغرام 
        """)
        """
        btn_chat=self.arabic("مراسلة")
        btn_cancel=self.arabic("الغاء")
        self.dialog= MDDialog(title=f"[font=font/arial.ttf]{titl}[/font]",buttons=[
            MDFlatButton(
                text=btn_cancel
            ,font_name="font/arial.ttf",on_release=self.close_dialog),
            MDRaisedButton(
                text=btn_chat
            ,font_name="font/arial.ttf",on_release=lambda c :print("self.web"))],auto_dismiss=False) 
        self.dialog.text=(f"[font=font/arial.ttf]{msg}[/font]")
        
        self.dialog.open()
        
        
        
    def close_dialog(self,instance):
      self.dialog.dismiss(force=False)
      pass
      
    #def web(self,instance):
        #x = webbrowser.open(telegram)
        
    def switch(self,x):
            if x=="KSA":
                toast("تم ضبط مفتاح السعودية ")
                ksa = self.txtin2.text ="+966"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,ksa)
            elif x=="SYR":
                toast("تم ضبط مفتاح سورية")
                syr = self.txtin2.text ="+963"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,syr)
            elif x=="LBN":
                toast("تم ضبط مفتاح لبنان")
                lbn = self.txtin2.text ="+961"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,lbn)
            elif x=="JOR":
                toast("تم ضبط مفتاح الاردن")
                jor = self.txtin2.text ="+962"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,jor)
            elif x=="EGY":
                toast("تم ضبط مفتاح مصر")
                egy = self.txtin2.text ="+20"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,egy)
            elif x=="YEM":
                toast("تم ضبط مفتاح اليمن")
                yem = self.txtin2.text ="+967"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,yem)
            elif x=="IRQ":
                toast("تم ضبط مفتاح العراق")
                irq = self.txtin2.text ="+964"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,irq)
            elif x=="QTR":
                toast("تم ضبط مفتاح قطر")
                qtr = self.txtin2.text ="+974"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,qtr)
            elif x=="KWT":
                toast("تم ضبط مفتاح الكويت")
                kwt =self.txtin2.text ="+965"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,kwt)
            elif x=="LBY":
                toast("تم ضبط مفتاح ليبيا")
                lby=self.txtin2.text ="+218"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,lby)
            elif x=="TUN":
                toast("تم ضبط مفتاح تونس")
                tun =self.txtin2.text ="+216"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,tun)
            elif x=="TUR":
                toast("تم ضبط مفتاح تركيا")
                tur=self.txtin2.text ="+90"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,tur)
            elif x=="SDN":
                toast("تم ضبط مفتاح السودان")
                sdn =self.txtin2.text ="+249"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,sdn)
            elif x=="MAR":
                toast("تم ضبط مفتاح المغرب")
                mar=self.txtin2.text ="+212"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,mar)
            elif x=="BHR":
                toast("تم ضبط مفتاح البحرين")
                bhr=self.txtin2.text ="+973"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,bhr)
            elif x=="OMN":
                toast("تم ضبط مفتاح عمان")
                omn=self.txtin2.text ="+968"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,omn)
            elif x=="SOM":
                toast("تم ضبط مفتاح الصومال")
                som=self.txtin2.text ="+252"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,som)
            elif x=="PSE":
                toast("تم ضبط مفتاح فلسطين")
                pse=self.txtin2.text ="+970"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,pse)
            elif x=="MRT":
                toast("تم ضبط مفتاح موريتانبا")
                mrt=self.txtin2.text ="+222"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,mrt)
            elif x=="ALG":
                toast("تم ضبط مفتاح الجزائر")
                alg=self.txtin2.text ="+213"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,alg)
            elif x=="UK":
                toast("تم ضبط مفتاح بريطانيا")
                uk=self.txtin2.text ="+44"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,uk)
            elif x=="USA":
                toast("تم ضبط مفتاح امريكا")
                usa=self.txtin2.text ="+1"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,usa)
            elif x=="CAN":
                toast("تم ضبط مفتاح كندا")
                can =self.txtin2.text ="+1"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,can)
            elif x=="AUS":
                toast("تم ضبط مفتاح استراليا")
                aus=self.txtin2.text ="+61"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,aus)
            elif x=="GER":
                toast("تم ضبط مفتاح المانيا")
                ger=self.txtin2.text ="+49"
                self.box.remove_widget(self.scrol)
                #self.updatedb(x,ger)
        
                
                       
if __name__=="__main__":
        WhatsappDirct().run()
        #db.close()
        
        
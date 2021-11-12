from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import pyqrcode


qr = """
MDScreen:
    MDCard:
        size_hint: None, None
        size: 300, 450
        orientation: "vertical"
        padding: 20
        spacing: 20
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 15
        radius: 15
        MDLabel:
            id: title
            text: "QR Code Generator"
            font_size: 30
            halign: "center"
        MDTextFieldRound:
            id: link
            hint_text: "Enter Your URL"
            icon_left: "link"
        MDTextFieldRound:
            id:file
            hint_text: "Enter File Name"
            icon_left: "file"
        MDFillRoundFlatIconButton:
            text: "Generate"
            pos_hint: {"center_x": .5}
            on_release: app.gen()
            icon: "file-plus"
        MDFillRoundFlatIconButton:
            text: "Clear"
            pos_hint: {"center_x": .5}
            on_release: app.clfs()
            icon: "delete"
        Image:
            id: qr_image
            source:"D:\KivyMD\KivyMD\QR Code Generator\img.png"
        MDSwitch:
            pos_hint: {"center_x": .5, "center_y": .5}
            on_active: app.dark(*args)

"""


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(qr)
    
    
    def gen(self):
        link = self.root.ids.link.text
        file = self.root.ids.file.text
        if len(link) == 0:
            self.root.ids.title.text = "URL Not Specified!"
            self.root.ids.qr_image.source = "D:\KivyMD\KivyMD\QR Code Generator\img.png"
        elif len(file) == 0:
             self.root.ids.title.text = "File Name Not Specified!"
             self.root.ids.qr_image.source = "D:\KivyMD\KivyMD\QR Code Generator\img.png"
        else:
            link = self.root.ids.link.text
            file = self.root.ids.file.text
            qr = pyqrcode.create(content=link)
            qr.png(f"{file}.png", scale=4)
            self.root.ids.qr_image.source = f"D:\KivyMD\KivyMD\QR Code Generator\{file}.png"
            self.root.ids.title.text = "QR Code Generated!"

    def clfs(self):
        self.root.ids.title.text = "QR Code Generator"
        self.root.ids.link.text = ""
        self.root.ids.file.text = ""
        self.root.ids.qr_image.source =""
        self.root.ids.qr_image.source = "D:\KivyMD\KivyMD\QR Code Generator\img.png"

    
    def dark(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


MainApp().run()
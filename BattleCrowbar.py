from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton


KV = '''
FloatLayout:
    
    MDGridLayout:
        adaptive_height: True
        cols: 3
        pos_hint: {'x': .4,'y':.5}
        
        MDIconButton:
            id: button_left1
            icon: "arrow-left-bold"
            on_release: app.previous1()
            
        
        MDLabel:
            id: kv_label1
            
            size_hint_x: None
            width: 20
            
            
        
        MDIconButton:
            id: button_right1
            icon: "arrow-right-bold"
            on_release: app.next1()
            
    MDGridLayout:
        adaptive_height: True
        cols: 3
        pos_hint: {'x': .4,'y':.3}
        MDIconButton:
            id: button_left2
            icon: "arrow-left-bold"
            on_press: app.previous2()
            
        
        MDLabel:
            id: kv_label2
            size_hint_x: None
            width: 20
            
            
        
        MDIconButton:
            id: button_right2
            icon: "arrow-right-bold"
            on_press: app.next2()
            

'''


class MainApp(MDApp):

    a = 1
    b = 2

    def build(self):
        self.title = "Battle Crowbar"
        self.kv_string = Builder.load_string(KV)

        self.label_text1 = self.kv_string.ids.kv_label1
        self.label_text1.text = str(self.a)

        self.label_text2 = self.kv_string.ids.kv_label2
        self.label_text2.text = str(self.b)

        return self.kv_string

    def next1(self):

        self.a += 1
        self.label_text1.text = str(self.a)

    def previous1(self):

        self.a -= 1
        self.label_text1.text = str(self.a)


    def next2(self):

        self.b += 1
        self.label_text2.text = str(self.b)

    def previous2(self):

        self.b -= 1
        self.label_text2.text = str(self.b)


if __name__ == '__main__':
    MainApp().run()

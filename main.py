from operator import length_hint
from unicodedata import name
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class buttuon(App):
    def build(self):
        main_layout=BoxLayout()

        min= TextInput(text="Min", font_size=33, size_hint=(.1, .1), pos_hint={'center_x':.95, 'center_y':.95})
        max= TextInput(text="Max", font_size=33, size_hint=(.1, .1),pos_hint={'center_x':.95, 'center_y':.95})
        name= TextInput(text="name", font_size=33, size_hint=(.1, .1),pos_hint={'center_x':.95, 'center_y':.95})
        
        alt_layout=BoxLayout()

        alt_layout.add_widget(min)
        alt_layout.add_widget(max)
        alt_layout.add_widget(name)
        main_layout.add_widget(alt_layout)

        return main_layout



    
    
  
if __name__ == '__main__':

    helloKivy = buttuon()
    helloKivy.run()
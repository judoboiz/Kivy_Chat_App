from operator import length_hint
from tkinter import HORIZONTAL
from unicodedata import name
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class buttuon(App):
    def build(self):
        main_layout=BoxLayout(orientation="vertical")

       
        name= TextInput(text="name", font_size=33, size_hint=(.3, .175),pos_hint={'center_x':.975, 'center_y':.935})
        
        alt_layout=BoxLayout(orientation="horizontal")

        alt_layout.add_widget(name)
       
        text= TextInput( font_size=33, size_hint=(.3, .3),pos_hint={'center_x':.05, 'center_y':.05},background_color=[.9,.1,-3,1.7])
        send = Button(text="send", size_hint=(.05, .2),background_color=[1,.1,.1,6])

        alt_layout2=BoxLayout(orientation="horizontal")
        alt_layout2.add_widget(text)
        alt_layout2.add_widget(send)

        main_layout.add_widget(alt_layout)
        main_layout.add_widget(alt_layout2)


        

        return main_layout



    
    
  
if __name__ == '__main__':

    helloKivy = buttuon()
    helloKivy.run()
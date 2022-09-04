from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class FrontPage(BoxLayout):

    def play_sound(slf):
        sound = SoundLoader.load("sound.mp3")
        if sound:
            sound.play()
        else:
            print("Fuck my self")

    def translertor(msg,type):
        if type==True:
            send_msg = ''.join(format(ord(i), '08b')for i in msg)
            return send_msg
        elif type == False:
            end_msg = ""
            for i in range(int(len(msg)/8)):
                recive_msg = chr(int(msg[0+i*8:8+i*8],2))
                end_msg = end_msg + recive_msg
                print(recive_msg)
            return end_msg

class MyApp(App):
    def build():
        return FrontPage()

if __name__ == "__main__":
    MyApp().run()

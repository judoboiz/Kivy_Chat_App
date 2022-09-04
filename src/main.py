from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout

class FrontPage(BoxLayout):

    def play_sound(self):
        sound = SoundLoader.load("sound.mp3")
        if sound:
            sound.play()
        else:
            print("Fuck my self")

    def translertor(self, msg,type):
        if type==True:
            send_msg = ''.join(format(ord(i), '08b')for i in msg)
            return send_msg
        elif type == False:
            recive_msg = ""
            for i in range(0, len(msg), 7):
                temp_data = int(msg[i:i + 7])
                ecimal_data = BinaryToDecimal


    def BinaryToDecimal(binary):
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return (decimal)

class MyApp(App):
    def build(self):
        return FrontPage()

if __name__ == "__main__":
    MyApp().run()
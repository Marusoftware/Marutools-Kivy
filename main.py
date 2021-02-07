import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.label import Label

class Main(App):
    def build(self):
        return Label(text="test")

if __name__ == "__main__":
    Main().run()

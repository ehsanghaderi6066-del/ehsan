from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

def process_text(s: str) -> str:
    return s.strip()[::-1] + " ✅"

class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=12, spacing=8, **kwargs)
        self.input = TextInput(hint_text="متن بنویس…", size_hint_y=None, height=48)
        self.add_widget(self.input)
        btn = Button(text="اجرا", size_hint_y=None, height=48, on_press=self.run_code)
        self.add_widget(btn)
        self.out = Label(text="خروجی اینجاست…")
        self.add_widget(self.out)

    def run_code(self, _):
        self.out.text = process_text(self.input.text)

class MyApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    MyApp().run()

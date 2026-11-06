from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import QLabel
from kivy.uix.textinput import TextInput

class StreamingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.title_label = QLabel(text='تطبيق البث الحي', font_size=24, size_hint=(1, 0.2))
        self.url_input = TextInput(text='rtsp://', hint_text='أدخل رابط البث هنا', multiline=False, size_hint=(1, 0.2))
        self.start_btn = Button(text='بدء البث', size_hint=(1, 0.2), background_color=(0.1, 0.6, 0.1, 1))
        
        layout.add_widget(self.title_label)
        layout.add_widget(self.url_input)
        layout.add_widget(self.start_btn)
        
        return layout

if __name__ == '__main__':
    StreamingApp().run()

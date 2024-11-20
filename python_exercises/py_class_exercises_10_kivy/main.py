import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Define the main layout for the app
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Label to display the counter
        self.label = Label(text="Counter: 0", font_size=40)
        self.add_widget(self.label)

        # Button to increment the counter
        self.button = Button(text="Increment", size_hint=(1, 0.5), font_size=30)
        self.button.bind(on_press=self.increment_counter)
        self.add_widget(self.button)

        self.counter = 0

    # Function to increment the counter
    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"

# Define the main App class
class SimpleKivyApp(App):
    def build(self):
        return MainLayout()

# Run the app
if __name__ == '__main__':
    SimpleKivyApp().run()

## When you run this app, 
# you'll see a window with a counter and a button.
#  Clicking the button increments the counter.
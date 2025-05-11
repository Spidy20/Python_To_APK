from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import math


class CalculatorApp(MDApp):
    def build(self):
        self.operators = ["/", "*", "-", "+", "."]
        self.last_was_operator = None
        self.last_button = None

        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"

        main_layout = MDBoxLayout(orientation="vertical", padding=10, spacing=10)

        self.solution = MDTextField(
            text="",
            halign="right",
            font_size=55,
            readonly=True,
            mode="rectangle",
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["C", "√", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
            ["1/x"]
        ]

        for row in buttons:
            h_layout = MDBoxLayout(spacing=10)
            for label in row:
                button = MDRaisedButton(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    font_size=24,
                    on_release=self.on_button_press
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.solution.text = ""

        elif text == "=":
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"

        elif text == "√":
            try:
                self.solution.text = str(math.sqrt(float(self.solution.text)))
            except:
                self.solution.text = "Error"

        elif text == "%":
            try:
                self.solution.text = str(float(self.solution.text) / 100)
            except:
                self.solution.text = "Error"

        elif text == "+/-":
            try:
                self.solution.text = str(float(self.solution.text) * -1)
            except:
                self.solution.text = "Error"

        elif text == "1/x":
            try:
                val = float(self.solution.text)
                if val != 0:
                    self.solution.text = str(1 / val)
                else:
                    self.solution.text = "Error"
            except:
                self.solution.text = "Error"

        else:
            self.solution.text += text


if __name__ == "__main__":
    CalculatorApp().run()

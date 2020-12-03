from kivymd.app import MDApp
from kivy.lang import Builder

class Test(MDApp):
    def build(self):
        self.title = 'Programming'
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: 'Programming'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
                
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

            Image:
                id: imageView
                source: 'python.png'
        
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'C++'
            icon: 'language-cpp'

            Image:
                id: imageView
                source: 'cp.png'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Kivy'
            icon: 'android'

            Image:
                id: imageView
                source: 'kivy.png'
'''
        )

Test().run()
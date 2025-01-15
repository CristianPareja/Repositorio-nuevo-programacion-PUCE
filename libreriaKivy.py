from libreriaKivy import App


class KivySaludo(App):
    def build(self):
        return label(text="Hola Mundo")
    
KivySaludo().run()
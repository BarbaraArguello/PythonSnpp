from pygame import mixer
class Reproductor:
    #Atributos
    archivo = None
    #Consructor
    def __init__(self,archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)
    def pause(self):
        mixer.music.pause()
        return "La música de ha pausado"
    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    def stop(self):
        mixer.music.stop() 
        return "La música se detuvo"
    def volume(self, v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a {}".format(v)

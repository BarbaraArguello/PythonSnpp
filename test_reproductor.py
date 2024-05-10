from tkinter import *
from tkinter.ttk import *
from Reproductor import *
musica = Reproductor('wefere.mp3')

def play_musica():
    musica.volume(0.1)
    musica.play()
def pause_musica():
        musica.pause()
def stop_musica():
        musica.stop()
def volume_musica():
        musica.volume(1)



master = Tk()
master.geometry('150x350')

label = Label(master,text="Reproductor de música")

label.pack(pady = 10)

btn_play = Button(master,text ="Reproducir", command = play_musica)
btn_play.pack(pady = 10)

btn_pause = Button(master,text ="Pausar",command = pause_musica)
btn_pause.pack(pady = 10)

btn_stop = Button(master,text ="Parar",command = stop_musica)
btn_stop.pack(pady = 10)

btn_volume = Button(master,text ="Volumen >",command = volume_musica)
btn_volume.pack(pady = 10)


mainloop()
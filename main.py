import tkinter
from tkinter  import *
from tkinter import tkk

# cores #
cor0 = "444466" #Preto
cor1 = "feffff" #Branco
cor2 = "6f9fbd" #Azul

fundo_dia = "6cc4cc"
fundo_noite = "484f60"
fundo_tarde = "bfb86b"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('350x350')
janela.configure(bg=fundo)

tkk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

janela.mainloop()
import tkinter as tk
from PIL import Image, ImageDraw

class Tela_Login:
    def __init__(self):
        janela = tk.Tk()
        janela.title('Tela de Login')
        janela.config(padx=0, pady=0)
        janela.state('zoomed')
        
        background = tk.PhotoImage(file='texturas/Tela de Login/Fundo.png')
        
        tk.Label(janela, image=background).pack()

        janela.mainloop()
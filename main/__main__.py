import tkinter as tk
from interface import HelpSystemApp
from gui.tela_login import Tela_Login

def main():
    print('Começo do aplicativo aqui')
    
    tl = Tela_Login()
    tl.mainloop()
    
    #root = tk.Tk()
    #app = HelpSystemApp(root)
    #root.mainloop()
    #hsa = HelpSystemApp(root)
    #hsa.inicializar()
    
    #sys.exit(main())
    
if __name__ == "__main__":
    main()
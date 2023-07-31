import tkinter as tk
from interface import HelpSystemApp

def main():
    print('Começo do aplicativo aqui')
    
    root = tk.Tk()
    app = HelpSystemApp(root)
    root.mainloop()
    
    hsa = HelpSystemApp(root)
    hsa.inicializar()
    #sys.exit(main())
    
if __name__ == "__main__":
    main()
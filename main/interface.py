import tkinter as tk

class HelpSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Help System - Specialisterne")
        self.solicitacoes = []
        
        # Criar widgets
        self.label_titulo = tk.Label(root, text="Sistema de Ajuda")
        self.label_titulo.pack(pady=10)

        self.label_solicitacao = tk.Label(root, text="Crie uma solicitação de ajuda:")
        self.label_solicitacao.pack()

        self.entry_solicitacao = tk.Entry(root, width=50)
        self.entry_solicitacao.pack(pady=5)

        self.botao_solicitar = tk.Button(root, text="Solicitar Ajuda", command=self.solicitar_ajuda)
        self.botao_solicitar.pack()

        self.label_solicitacoes = tk.Label(root, text="Solicitações de ajuda:")
        self.label_solicitacoes.pack(pady=10)

        self.lista_solicitacoes = tk.Listbox(root, width=60)
        self.lista_solicitacoes.pack()

    def solicitar_ajuda(self):
        solicitacao = self.entry_solicitacao.get()
        if solicitacao:
            self.solicitacoes.append(solicitacao)
            self.lista_solicitacoes.insert(tk.END, solicitacao)
            self.entry_solicitacao.delete(0, tk.END)

# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpSystemApp(root)
    root.mainloop()
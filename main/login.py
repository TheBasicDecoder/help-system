import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ajuda - Login")
        self.geometry("600x400")

        # Criar o widget do fundo
        self.fundo_label = tk.Label(self)
        self.fundo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Carregar imagem do fundo
        self.fundo_image = tk.PhotoImage(file="texturas/Tela de Login/Fundo.png")
        self.fundo_label.config(image=self.fundo_image)

        # Criar o widget do logo
        self.logo_label = tk.Label(self)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")

        # Carregar imagem do logo
        self.logo_image = tk.PhotoImage(file="texturas/Tela de Login/logo_ABTech.png")
        self.logo_label.config(image=self.logo_image)

        # Criar os campos de nome de usuário e senha
        self.username_label = tk.Label(self, text="Nome de usuário:")
        self.username_label.place(relx=0.35, rely=0.45, anchor="e")

        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.username_entry.insert(0, "Digite seu usuário")

        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.place(relx=0.35, rely=0.55, anchor="e")

        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")
        self.password_entry.insert(0, "Digite sua senha")


        # Criar o botão de login
        self.login_image = tk.PhotoImage(file="texturas/Tela de Login/login.png")
        self.login_button = tk.Button(self, image=self.login_image, command=self.login, bd=0)
        self.login_button.place(relx=0.5, rely=0.7, anchor="center")

        # Criar o botão de cadastro
        self.cadastro_image = tk.PhotoImage(file="texturas/Tela de Login/cadastro.png")
        self.cadastro_button = tk.Button(self, image=self.cadastro_image, command=self.cadastrar, bd=0)
        self.cadastro_button.place(relx=0.5, rely=0.8, anchor="center")

        # Criar o link de "Esqueci minha senha"
        self.esqueci_senha_label = tk.Label(self, text="Esqueci minha senha", fg="blue", cursor="hand2")
        self.esqueci_senha_label.place(relx=0.5, rely=0.9, anchor="center")
        self.esqueci_senha_label.bind("<Button-1>", lambda e: self.esqueci_senha())

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Aqui adicionar a lógica para verificar o login
        # Por exemplo, verificar se o usuário e senha são válidos
        if username == "seu_usuario" and password == "sua_senha":
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

    def cadastrar(self):
        # Aqui adicionar a lógica para o cadastro de novos usuários
        messagebox.showinfo("Cadastro", "Ainda não implementado.")

    def esqueci_senha(self):
        # adicionar a lógica para lidar com o esquecimento de senha
        messagebox.showinfo("Esqueci minha senha", "Ainda não implementado.")

    def toggle_password(self):
        # Alterna a visibilidade da senha entre visível e escondida
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show="*")
        else:
            self.password_entry.config(show="")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()

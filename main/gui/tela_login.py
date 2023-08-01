import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mysql

cnct = mysql.connect(host="localhost",user="root",port="3306",password=" ",database="inserir nome do database aqui")
# Dados padrão ao criar um database
# Modificar os dados de acordo com o banco de dados usado

c = cnct.cursor()

class Tela_Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ajuda - Login")
        self.geometry("600x400")
        self.state('zoomed')

        # Criar o widget do fundo
        self.fundo_label = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.fundo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Carregar imagem do fundo
        self.fundo_image = tk.PhotoImage(file="texturas/Tela de Login/Fundo.png")
        self.fundo_label.config(image=self.fundo_image)

        # Criar o widget do logo
        self.logo_label = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")

        # Carregar imagem do logo
        self.logo_image = tk.PhotoImage(file="texturas/Tela de Login/logo_ABTech.png")
        self.logo_label.config(image=self.logo_image)

        # Criar os campos de nome de usuário e senha
        self.username_label = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.username_label.place(relx=0.5, rely=0.45, anchor="center")
        
        self.username_imagem = tk.PhotoImage(file="texturas/Tela de Login/campo username.png")
        self.username_label.config(image=self.username_imagem)

        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.username_entry.insert(0, "Digite seu usuário")

        self.password_label = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.password_label.place(relx=0.5, rely=0.60, anchor="center")
        
        self.password_imagem = tk.PhotoImage(file="texturas/Tela de Login/campo senha visivel.png")
        self.password_label.config(image=self.password_imagem)

        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.place(relx=0.5, rely=0.60, anchor="center")
        self.password_entry.insert(0, "Digite sua senha")


        # Criar o botão de login
        self.login_image = tk.PhotoImage(file="texturas/Tela de Login/login.png")
        self.login_button = tk.Button(self, image=self.login_image, command=self.login, bd=0)
        self.login_button.place(relx=0.5, rely=0.75, anchor="center")

        # Criar o botão de cadastro
        self.cadastro_image = tk.PhotoImage(file="texturas/Tela de Login/cadastro.png")
        self.cadastro_button = tk.Button(self, image=self.cadastro_image, command=self.cadastrar, bd=0)
        self.cadastro_button.place(relx=0.5, rely=0.85, anchor="center")

        # Criar o link de "Esqueci minha senha"
        self.esqueci_senha_label = tk.Label(self, text="Esqueci minha senha", fg="blue", cursor="hand2", borderwidth=0, highlightthickness=0)
        self.esqueci_senha_label.place(relx=0.5, rely=0.95, anchor="center")
        self.esqueci_senha_label.bind("<Button-1>", lambda e: self.esqueci_senha())

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        vals = (username,password,)
        select = "SELECT * FROM 'cadastros' WHERE 'email' = %s and 'senha' = %s"
        c.execute(select,vals)
        usuario = c.fetchone()
        if usuario is not None:
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

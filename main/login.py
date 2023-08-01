import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Aqui você pode adicionar a lógica para verificar o login
    # Por exemplo, verificar se o usuário e senha são válidos

    if username == "seu_usuario" and password == "sua_senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")

def cadastrar():
    # Aqui você pode adicionar a lógica para o cadastro de novos usuários
    messagebox.showinfo("Cadastro", "Ainda não implementado.")

def esqueci_senha():
    # Aqui você pode adicionar a lógica para lidar com o esquecimento de senha
    messagebox.showinfo("Esqueci minha senha", "Ainda não implementado.")

# Criando a janela principal
root = tk.Tk()
root.title("Sistema de Ajuda - Login")

# Criando os widgets
username_label = tk.Label(root, text="Nome de usuário:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Senha:")
password_entry = tk.Entry(root, show="*")

login_button = tk.Button(root, text="Login", command=login)
cadastre_button = tk.Button(root, text="Cadastre-se", command=cadastrar)
esqueci_senha_link = tk.Label(root, text="Esqueci minha senha", fg="blue", cursor="hand2")
esqueci_senha_link.bind("<Button-1>", lambda e: esqueci_senha())

# Posicionando os widgets na janela
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
cadastre_button.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
esqueci_senha_link.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Iniciando a execução da interface
root.mainloop()

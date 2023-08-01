class User:
    email = 'email@usuario.com'
    nome = 'Usuário'
    senha = 'usuario123'
    sobre = 'Um usuário comum'
    
    def __init__(usuario, email, nome, senha, sobre):
        usuario.email = email
        usuario.nome = nome
        usuario.senha = senha
        usuario.sobre = sobre
        
    
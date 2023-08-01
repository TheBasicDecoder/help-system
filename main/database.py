import mysql.connector as mysql

cnct = mysql.connect(host="localhost",user="root",port="3306",password=" ",database="inserir nome do database aqui")
# Dados padrão ao criar um database
# Modificar os dados de acordo com o banco de dados usado

c = cnct.cursor()
def getUser() -> 
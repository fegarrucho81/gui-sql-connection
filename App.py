import json
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector


with open('config.json', encoding='utf-8') as f:
    config_data = json.load(f)


user = config_data["user"]
password = config_data["password"]


conn = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="py"
)
cursor = conn.cursor()


def adicionar_cliente():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    email = entry_email.get()
    cpf = entry_cpf.get()

    sql = "INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (%s, %s, %s, %s)"
    val = (nome, sobrenome, email, cpf)
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")

def remover_cliente():
    n_idContato = entry_id.get()
    sql = "DELETE FROM clientes WHERE n_idContato = %s"
    val = (n_idContato,)
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")

def consultar_clientes():
    cursor.execute("SELECT * FROM clientes")
    result = cursor.fetchall()
    
    text_resultado.delete('1.0', tk.END)
    
    for row in result:
        text_resultado.insert(tk.END, f"{row}\n")


root = tk.Tk()
root.title("Gerenciamento de Clientes")

label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_sobrenome = tk.Label(root, text="Sobrenome:")
label_sobrenome.pack()
entry_sobrenome = tk.Entry(root)
entry_sobrenome.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_cpf = tk.Label(root, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(root)
entry_cpf.pack()

btn_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
btn_adicionar.pack()

label_id = tk.Label(root, text="ID do Cliente para Remover:")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

btn_remover = tk.Button(root, text="Remover Cliente", command=remover_cliente)
btn_remover.pack()

btn_consultar = tk.Button(root, text="Consultar Clientes", command=consultar_clientes)
btn_consultar.pack()


label_resultado = tk.Label(root, text="Resultados da Consulta:")
label_resultado.pack()

text_resultado = tk.Text(root, height=10, width=50)
text_resultado.pack()

btn_sair = tk.Button(root, text="Sair", command=root.quit)
btn_sair.pack()

root.mainloop()

cursor.close()
conn.close()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import psycopg2

def insert_data():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    
    if name and age.isdigit() and email:
        try:
            cur.execute("INSERT INTO users (nome, idade, email) VALUES (%s, %s, %s)", (name, int(age), email))
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
        except psycopg2.Error as e:
            messagebox.showerror("Database Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input error", "Please enter valid data")

def fetch_data():
    try:
        cur.execute("SELECT id, nome, idade, email FROM users")
        rows = cur.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for row in rows:
            tree.insert("", tk.END, values=row)
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))

# Configuração da conexão com o banco de dados PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="empresafake",
        user="marvyn",
        password="120313",
        host="localhost"
    )
    cur = conn.cursor()
except Exception as e:
    messagebox.showerror("Error", str(e))
    exit()

    # Configuração da interface gráfica Tkinter
root = tk.Tk()
root.title("Cadastrar e Mostrar Dados")

# Widgets para inserir os dados
tk.Label(root, text="Nome").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Idade").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

tk.Button(root, text="Cadastrar Dados", command=insert_data).grid(row=3, columnspan=2)

# Treeview para mostrar os dados
columns = ("ID", "Nome", "Idade", "Email")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=2, sticky='nsew')

tk.Button(root, text="Mostrar Dados", command=fetch_data).grid(row=5, columnspan=2)

root.mainloop()

cur.close()
conn.close()
import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3

#conexão  com BD
#conexao = sqlite3.connect('produtos.db')
#cursor = conexao.cursor()
#cursor.execute("CREATE TABLE produtos(descricao text, unidade text, qt real, p_custo real, p_venda real)")
#conexao.commit()
#conexao.close()

#função do botão cadastrar
def cadastrar_produto():
    conexao = sqlite3.connect('produtos.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos VALUES(:descricao, :unidade, :qt, :p_custo, :p_venda)",
                   {
                        'descricao':entry_descricao.get(),
                        'unidade':combo_unidade.get(),
                        'qt':entry_qt.get(),
                        'p_custo':entry_preco_custo.get(),
                        'p_venda':entry_preco_venda.get()
                    }
                    )
    conexao.commit()
    conexao.close()
    entry_descricao.delete(0, "end")
    combo_unidade.delete(0, "end")
    entry_qt.delete(0, "end")
    entry_preco_custo.delete(0, "end")
    entry_preco_venda.delete(0, "end")

#Design da janela
lista_und = ["UN", "JG"]

janela = tk.Tk()
janela.title('Cadastro de Produtos')
janela.geometry("410x170")

label_titulo = tk.Label(text='Cadastro de produtos')
label_titulo.grid(row=0, column=0, sticky='nswe', columnspan=4)

label_descricao = tk.Label(text='Descrição:')
label_descricao.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')

entry_descricao = tk.Entry()
entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky='nswe', columnspan=3)

label_unidade = tk.Label(text='Unidade:')
label_unidade.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')

combo_unidade = ttk.Combobox(values=lista_und, width=10)
combo_unidade.grid(row=2, column=1, padx=5, pady=5, sticky='nswe') #nswe

label_qt = tk.Label(text='Quant.:')
label_qt.grid(row=2, column=2, padx=5, pady=5, sticky='nswe')

entry_qt = tk.Entry()
entry_qt.grid(row=2, column=3, padx=5, pady=5, sticky='nswe')

label_preco_custo = tk.Label(text='P.Custo:')
label_preco_custo.grid(row=3, column=0, padx=5, pady=5, sticky='nswe')

entry_preco_custo = tk.Entry()
entry_preco_custo.grid(row=3, column=1, padx=5, pady=5, sticky='nswe')

label_preco_venda = tk.Label(text='P.Venda:')
label_preco_venda.grid(row=3, column=2, padx=5, pady=5, sticky='nswe')

entry_preco_venda = tk.Entry()
entry_preco_venda.grid(row=3, column=3, padx=5, pady=5, sticky='nswe')

btn_cadastrar_produto = tk.Button(text='Cadastrar', command=cadastrar_produto)
btn_cadastrar_produto.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

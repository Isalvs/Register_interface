import tkinter as tk
from tkinter import ttk
import datetime as dt


def createItem():
    description = textField
    unitType = unitTypeEntry
    quant = quantityItensEntry
    creationDate = dt.datetime.now()
    creationDate = creationDate.strftime('%d/%m/%Y %H:%M:%S')
    elementCode = len(codeList) + 1
    codeInString = f'COD-{elementCode}'
    codeList.append((codeInString, description, unitType, quant, creationDate))


window = tk.Tk()

typeList = ['kg', 'g', 'ml', 'l', 'un']
codeList = list()

window.title('Ferramenta de Cadastro de materiais')

labelDescription = tk.Label(text='Descrição do material')
labelDescription.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

textField = tk.Entry()
textField.grid(row=2, column=0, pady=10, padx=10, sticky='nswe', columnspan=4)

labelUnitType = tk.Label(text='Tipo de unidade do material:')
labelUnitType.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

unitTypeEntry = ttk.Combobox(values=typeList)
unitTypeEntry.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

labelQuantityItens = tk.Label(text='Quantidade de entrada: ')
labelQuantityItens.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

quantityItensEntry = tk.Entry()
quantityItensEntry.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

registerButton = tk.Button(text='Cadastrar', command=createItem)
registerButton.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

window.mainloop()


print(codeList)

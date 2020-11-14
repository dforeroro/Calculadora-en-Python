import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

def init_window():
    window=tk.Tk()
    window.title('Calculadora')
    window.geometry("260x240")
    
    fondo_imagen = PhotoImage(file="Calculadori.png")  
    fondo = tk.Label(window, image=fondo_imagen)
    fondo.place(x=0,y=0)
    label = tk.Label(window, text='', font=('Arial bold', 40))
    label.grid(column = 0, row = 0)
  
    entrada1 = tk.Entry(window, width = 10)  
    entrada2 = tk.Entry(window, width = 10)
    entrada1.grid(column = 6, row = 1, columnspan = 2, padx = 5, pady = 5)
    entrada2.grid(column = 6, row = 2, columnspan = 2, padx = 5, pady = 5)
    entrada1.focus()
    entrada2.focus()
  
    label_entrada1 = tk.Label(window, text='Ingrese primer número: ', font=('Bauhaus 93', 10))
    label_entrada1.grid(column = 0, row = 1, columnspan = 6, padx = 5, pady = 5)
  
    label_entrada2 = tk.Label(window, text='Ingrese segundo número: ', font=('Bauhaus 93', 10))
    label_entrada2.grid(column = 0, row = 2, columnspan = 6, padx = 5, pady = 5)

    label_operador = tk.Label(window, text='Escoja un operador', font=('Bauhaus 93', 10))
    label_operador.grid(column = 0, row = 3, columnspan = 6, padx = 5, pady = 5)
  
    combo_operadores = ttk.Combobox(window, width = 8)
    combo_operadores["values"]=['',"     +","     -","     *","     /","     pow"]
    combo_operadores.current(0)
    combo_operadores.grid(column = 6, row = 3, columnspan = 2, padx = 5, pady = 5)

    boton = tk.Button(window, command = lambda:click_calcular(label_resultado,entrada1.get(),entrada2.get(),combo_operadores.get()),text='Calcular',bg="purple",fg="white")
    boton.grid(column = 2, row = 4, columnspan = 2, padx = 5, pady = 5)

    boton_clear = tk.Button(window, command = lambda:click_clear(label_resultado,entrada1,entrada2,combo_operadores),text='Limpiar',bg="purple",fg="white")
    boton_clear.grid(column = 4, row = 4, columnspan = 2, padx = 5, pady = 5)

    boton_cerrar = tk.Button(window, command = lambda:click_cerrar(window),text='Cerrar',bg="purple",fg="white")
    boton_cerrar.grid(column = 6, row = 4, columnspan = 2, padx = 5, pady = 5)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Bauhaus 93', 11))
    label_resultado.grid(column = 0, row = 5, columnspan = 8, padx = 5, pady = 5)
  
    window.mainloop()
    return

def calculadora(num1, num2, operador):
    if operador == "     +":
        resultado = num1 + num2
    elif operador == "     -":
        resultado = num1 - num2
    elif operador == "     *":
        resultado = num1 * num2
    elif operador == "     /":
        if num2 == 0:
            messagebox.showerror(message="No es posible realizar la operación", title="ERROR")
            resultado = ''
        else:
            resultado = round(num1 / num2, 2)
    elif operador == "     pow":
        if (num1 == 0) and (num2 == 0):
            messagebox.showerror(message="No es posible realizar la operación", title="ERROR")
            resultado = ''
        else:
            resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador):
    valor1 =  float(num1)
    valor2 =  float(num2)
    res = calculadora(valor1, valor2, operador)
    label.configure(text='Resultado: ' + str(res))
    return

def click_clear(label, entrada1, entrada2, operador):
    label.configure(text='Resultado: ')
    operador.current(0)
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    entrada1.focus()
    return

def click_cerrar(window):
    window.destroy()

def main():
    init_window()

main()
    
from ctypes import py_object
from logging import root
import tkinter 
import os

def abrir_csp():
    os.system('/home/jostos/Escritorio/IA-UNAL-2022-2/Proyecto_Final_IA/metodo_logico/m_logico.py')




ventana = tkinter.Tk()
fondo = tkinter.PhotoImage(file='menu.png')
label1 = tkinter.Label(ventana, image=fondo)
label1.place(x=0,y=0)
ventana.geometry('500x500')
ventana.title('Nonogram Solver Menu')





boton_csp = tkinter.Button(text='CSP',        
        cursor='hand2',
        relief='flat',
        bg = '#ffffff',
        highlightbackground='white',
        highlightthickness=2,
        command=abrir_csp)
boton_csp.place(x=225, y=280)
ventana.mainloop()


from tkinter import ttk
from tkinter import *

import sqlite3

class Producto:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Productos app')


        #contenedor
        frame = LabelFrame(self.wind, text='Nuevo Producto')
        frame.grid(row = 0, column = 3, columnspan = 3, pady = 20)

        Label(frame, text = 'Nombre Producto').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)


if __name__ == '__main__':
    window = Tk()
    app = Producto(window)
    window.mainloop()
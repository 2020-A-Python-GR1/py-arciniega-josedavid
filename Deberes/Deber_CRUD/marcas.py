from tkinter import ttk
from tkinter import *
import sqlite3

class Marcas:#aqui todos los metodos de las ventanas/ funcionalidad de las ventanas

    db_name = 'database.db'


    def __init__(self, ventana1):
        self.wind = ventana1 # wind almacena mi ventana en una propiedad
        self.wind.title('GESTOR DE MARCAS')

        ## CREAR UN CONTENEDOR FRAME
        frame = LabelFrame(self.wind, text='REGISTRO DE MARCAS')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        ## Ingreso de Nombre de la Marca
        Label(frame, text = 'Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        ## Ingreso de la industria de la Marca
        Label(frame, text='Industria: ').grid(row=2, column=0)
        self.industria = Entry(frame)
        self.industria.grid(row=2, column=1)

        ## Ingreso de colores de la Marca
        Label(frame, text = 'Color1/Color2: ').grid(row=3, column=0)
        self.color = Entry(frame)
        self.color.grid(row=3, column=1)

        ## Ingreso de numero en el Ranking en el mercado de la Marca
        Label(frame, text='N° Ranking: ').grid(row=4, column=0)
        self.ranking = Entry(frame)
        self.ranking.grid(row=4, column=1)

        ## ingreso si la marca tiene SLOGAN
        Label(frame, text = 'Slogan S/N: ').grid(row=5, column=0)
        self.slogan = Entry(frame)
        self.slogan.grid(row= 5, column=1)

        ## Ingreso del nivel de aceptacion de la Marca
        Label(frame, text='% Aceptación: ').grid(row=6, column=0)
        self.aceptacion = Entry(frame)
        self.aceptacion.grid(row=6, column=1)

        ## BOTÓN  AGREGAR REGISTRO
        ttk.Button(frame, text='Ingresar Marca', command = self.ingresar_marca).grid(row=7, columnspan=2, sticky=W+E)

        ## Mensaje de salida
        self.mensaje_salida = Label(text='', fg='green')
        self.mensaje_salida.grid(row=8, column=0, columnspan=2, sticky=W+E)

        # TABLA PARA MOSTRAR DATOS
        self.tree = ttk.Treeview(height=15, columns=6)
        self.tree.grid(row=9, column=0, columnspan=2)
        self.tree["columns"] = ("1", "2", "3", "4", "5")

        self.tree.heading('#0', text='MARCA', anchor=CENTER)
        self.tree.heading('1', text='Industria', anchor=CENTER)
        self.tree.heading('2', text='Color', anchor=CENTER)
        self.tree.heading('3', text='Ranking', anchor=CENTER)
        self.tree.heading('4', text='Slogan', anchor=CENTER)
        self.tree.heading('5', text='% Aceptacion', anchor=CENTER)

        ## BOTON ELIMINAR FILA
        ttk.Button(text='ELIMINAR', command=self.elimnar_marca).grid(row=10, column=0, sticky=W+E)

        ## BOTPON EDITAR FILA
        ttk.Button(text='EDITAR', command=self.editar_marca).grid(row=10, column=1, sticky=W+E)

        # LLENAR TABLA
        self.get_products()

    # EJECUTAR CONSULTA A LA BASE DE DATOS
    def run_query(self,query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        # LIMPIAR DATOS DE TABLA
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # OBTENER DATOS TABLA
        query = 'SELECT * FROM marca ORDER BY nombre DESC'
        db_rows = self.run_query(query) # rows=filas

        # LLENANDO LOS DATOS
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=(row[2], row[3],row[4], row[5], row[6]))

    # Validar Ingreso de datos
    def validation(self):
        return len(self.name.get()) != 0 and\
               len(self.industria.get()) != 0 and \
               len(self.color.get()) != 0 and \
               len(self.ranking.get()) != 0 and \
               len(self.slogan.get()) != 0 and \
               len(self.aceptacion.get()) != 0

    def ingresar_marca(self):
        if self.validation():
            query = 'INSERT INTO marca VALUES(NULL, ?, ?, ?, ?, ?, ?)'
            parameters =(self.name.get(),self.industria.get(),self.color.get(),self.ranking.get(),self.slogan.get(),self.aceptacion.get(),)
            self.run_query(query, parameters)
            self.mensaje_salida['text']='La Marca {} se ha REGISTRADO EXITOSAMENTE'.format(self.name.get())
            self.name.delete(0, END)
            self.industria.delete(0, END)
            self.color.delete(0, END)
            self.ranking.delete(0, END)
            self.slogan.delete(0, END)
            self.aceptacion.delete(0, END)
        else:
            self.mensaje_salida['text'] = 'Ingreso de Datos Incorrecto'
        self.get_products()

    def elimnar_marca(self):
        self.mensaje_salida['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje_salida['text'] = 'Selecciona un Registro'
            return
        self.mensaje_salida['text'] = ''
        nombre = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM marca WHERE nombre = ?'
        self.run_query(query, (nombre, ))
        self.mensaje_salida['text'] = 'La Marca {} ha sido ELIMINADO EXITOSAMENTE'.format(nombre)
        self.get_products()

    # EDITAR MARCA
    def editar_marca(self):
        self.mensaje_salida['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.mensaje_salida['text'] = 'Seleccione una Marca para Editar'
            return
        nombre = self.tree.item(self.tree.selection())['text']
        old_industria = self.tree.item(self.tree.selection())['values'][0]
        old_color = self.tree.item(self.tree.selection())['values'][1]
        old_ranking = self.tree.item(self.tree.selection())['values'][2]
        old_slogan = self.tree.item(self.tree.selection())['values'][3]
        old_aceptacion = self.tree.item(self.tree.selection())['values'][4]

        self.ventana_edicion = Toplevel()
        self.ventana_edicion.title = 'VENTANA DE EDICION'

        # Nombre Actual
        Label(self.ventana_edicion, text ='Nombre:').grid(row = 0, column = 1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value=nombre), state ='readonly').grid(row = 0, column = 2)
        # Nuevo Nombre
        Label(self.ventana_edicion, text ='Nuevo Nombre:').grid(row = 1, column = 1)
        nuevo_nombre = Entry(self.ventana_edicion)
        nuevo_nombre.grid(row = 1, column = 2)

        # Industria Actual
        Label(self.ventana_edicion, text ='Industria:').grid(row = 2, column = 1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value=old_industria), state ='readonly').grid(row = 2, column = 2)
        # Nueva Industria
        Label(self.ventana_edicion, text ='Nueva Industria:').grid(row = 3, column = 1)
        nueva_industria= Entry(self.ventana_edicion)
        nueva_industria.grid(row = 3, column = 2)

        # Color Acutual
        Label(self.ventana_edicion, text ='Color:').grid(row = 4, column = 1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value=old_color), state ='readonly').grid(row = 4, column = 2)
        # Nuevo Color
        Label(self.ventana_edicion, text ='Nuevo Color:').grid(row = 5, column = 1)
        nuevo_color = Entry(self.ventana_edicion)
        nuevo_color.grid(row = 5, column = 2)

        # Ranking Actual
        Label(self.ventana_edicion, text ='Ranking:').grid(row = 6, column = 1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value=old_ranking), state ='readonly').grid(row = 6, column = 2)
        # Nuevo Ranking
        Label(self.ventana_edicion, text ='Nuevo Ranking:').grid(row = 7, column = 1)
        nueva_ranking = Entry(self.ventana_edicion)
        nueva_ranking.grid(row = 7, column = 2)

        # Slogan Actual
        Label(self.ventana_edicion, text ='Slogan, estado:').grid(row = 8, column=1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value=old_slogan), state ='readonly').grid(row = 8, column = 2)
        # Nuevo Slogan
        Label(self.ventana_edicion, text ='Nuevo Estado de Slogan:').grid(row = 9, column = 1)
        nuevo_slogan = Entry(self.ventana_edicion)
        nuevo_slogan.grid(row = 9, column=2)

        # Aceptacion Actual
        Label(self.ventana_edicion, text ='% Aceptación:').grid(row = 10, column = 1)
        Entry(self.ventana_edicion, textvariable = StringVar(self.ventana_edicion, value = old_aceptacion), state ='readonly').grid(row = 10, column = 2)
        # Nueva Aceptacion
        Label(self.ventana_edicion, text ='Nueva Aceptación:').grid(row = 11, column = 1)
        nueva_aceptacion= Entry(self.ventana_edicion)
        nueva_aceptacion.grid(row = 11, column = 2)

        ## BOTON ACTUALIZAR DE LA VENTANA EDICION
        Button(self.ventana_edicion, text ='Actualizar',
               command = lambda: self.editar_registro(nuevo_nombre.get(), nombre,
                                                      nueva_industria.get(), old_industria,
                                                      nuevo_color.get(), old_color,
                                                      nueva_ranking.get(), old_ranking,
                                                      nuevo_slogan.get(), old_slogan,
                                                      nueva_aceptacion.get(), old_aceptacion)).grid(row = 13, column = 2, sticky = W)
        self.ventana_edicion.mainloop()


    def editar_registro(self, nuevo_nombre, nombre, nueva_industria, old_industria,
                        nuevo_color,old_color,nuevo_ranking,old_ranking,
                        nuevo_slogan,old_slogan,nueva_aceptacion,old_aceptacion):
        query = 'UPDATE marca SET nombre = ?, industria = ?,' \
                'color = ?, ranking = ?, slogan = ?, ' \
                'aceptacion = ? WHERE nombre = ? AND industria = ? AND ' \
                'color = ? AND ranking = ? AND slogan = ? AND aceptacion = ?'
        parameters = (nuevo_nombre, nueva_industria, nuevo_color, nuevo_ranking,
                      nuevo_slogan, nueva_aceptacion,nombre, old_industria,
                      old_color,old_ranking, old_slogan,old_aceptacion)
        self.run_query(query, parameters)
        self.ventana_edicion.destroy()
        self.mensaje_salida['text'] = 'Actualización de {}  Exitosa'.format(nombre)
        self.get_products()


if __name__ == '__main__':#comprovacion(if) para la aplicacion principal
    ventana1 = Tk()
    application = Marcas(ventana1)#Instancia la clase Productmy enviar el parametro windows
    ventana1.mainloop()
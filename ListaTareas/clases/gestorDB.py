
import datetime
import sqlite3 as sql
from clases.tarea import Tarea




class GestorDBTareas:
    tareas = [] 
    def __init__(self):
        pass
    
    def createDB(self):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tareas(
                           descripcion TEXT NOT NULL UNIQUE,
                           activo INT NOT NULL,
                           fecha_creacion TEXT NOT NULL,
                           modificacionHora TEXT 
                           )
                    """)
    
    def agregarTarea(self,tarea:Tarea):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO tareas (descripcion,activo,fecha_creacion) VALUES (?,?,?)
            """,(tarea.descripcion, tarea.activo, tarea.horaCreacion))
    
    def verTareas(self):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas;")
            try:

                tareas = cursor.fetchall()
                return tareas   
            except:
                return "lista vacia"
    
    def eliminarTarea(self, decripcion):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tareas WHERE descripcion = ?", (decripcion,))
    
    def actualizarDescripcion(self, descripcionActual,newDescripcion:str):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            horaAcrual =  datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")
            cursor.execute("""UPDATE tareas SET descripcion = ?,
                                                modificacionHora = ?
                            WHERE descripcion = ?""", (newDescripcion,horaAcrual,descripcionActual,))
    
    def actualizarEstado(self, newEstado:bool, descripcion=str):
        with sql.Connection("Tareas") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    UPDATE tareas SET activo = ?
                        WHERE descripcion = ?""",(newEstado,descripcion))














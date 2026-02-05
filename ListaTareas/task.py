
import flet as ft
from clases.gestorTareas import GestorTareas
from clases.tarea import Tarea
from clases.gestorDB import GestorDBTareas
import coloresConstantes




class Task(ft.Container):
    def __init__(self, tarea: Tarea):
        super().__init__(self)
        self.gestor = GestorTareas()
        self.tarea = tarea
        self.gestorDb = GestorDBTareas()
        self.db = self.gestorDb.createDB()
        self.completada = self.tarea.activo
        self.descripcion = ft.Text()
        self.bgcolor = coloresConstantes.COLOR_CARDS_INACTIVO
        self.border_radius = 10
    


        self.btnBorrar = ft.IconButton(ft.Icons.DELETE, 
                                       icon_color=coloresConstantes.COLOR_BOTON_BORRAR, 
                                       visible=False, 
                                       on_click=self.borrarTarea)
        
        self.descripcion = ft.Text(self.tarea.descripcion, style=ft.TextStyle(
            weight=ft.FontWeight.BOLD,
            color=coloresConstantes.TEXTO_COLOR
        ))
        self.on_click = self.hacerCLick

        self.btnEditar = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.hacerVisibleEntrada, icon_color="#2563EB")
        self.entradaEditar = ft.TextField(
            width = 80,
            border_radius = 10,
            visible = False,
            border= ft.InputBorder.NONE,
            autofocus=True,
            on_submit= self.hacerEditar,
            color=coloresConstantes.TEXTO_COLOR
        )



        self.checkbox = ft.Checkbox(
                            value=self.completada,
                            on_change=self.setCompletar,
                            fill_color = coloresConstantes.COLOR_CHECK


                        )

        self.content = ft.Row(
            controls = [
                ft.Row(
                    controls=[
                        self.checkbox,
                        self.descripcion,
                        self.entradaEditar,
                    ]
                ),
                self.btnEditar,
                self.btnBorrar

            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        if self.tarea.activo:
            self.configuracionesColores()

    def setCompletar(self):
        if self.checkbox.value:
            self.tarea.activo = True


            
            self.gestorDb.actualizarEstado(self.tarea.activo, self.descripcion.value)
            self.configuracionesColores()
            
            

        else:
            
            
            self.tarea.activo = False
            self.gestorDb.actualizarEstado(self.tarea.activo, self.descripcion.value)
            self.completada = self.tarea.activo
            self.btnBorrar.visible = False
            self.descripcion.style = ft.TextStyle(
                decoration=ft.TextDecoration.NONE,
                weight=ft.FontWeight.BOLD,
                color=coloresConstantes.TEXTO_COLOR
            )
            self.bgcolor = coloresConstantes.COLOR_CARDS_INACTIVO
            self.tarea.activo = False
            self.btnEditar.visible = True
            


    def hacerCLick(self, e):
        print(self.gestor.tareas.index(self))

    def hacerEditar(self, e):
        if (e.data != ""):
            
            self.gestorDb.actualizarDescripcion(self.descripcion.value,e.data)
            self.descripcion.value = e.data
            self.entradaEditar.visible = False


    def hacerVisibleEntrada(self, e):
        self.entradaEditar.visible = True

    def borrarTarea(self):
        self.gestor.removeTarea(self)
        self.gestorDb.eliminarTarea(self.descripcion.value)


    def agregarTarea(self):
        self.gestor.addTarea(self)
        
        self.gestorDb.agregarTarea(self.tarea)

    def __str__(self):
        return f"Task(tarea: {self.descripcion.value}, activo={self.completada})"
    

    def configuracionesColores(self):
        self.descripcion.style = ft.TextStyle(
            decoration=ft.TextDecoration.LINE_THROUGH,
            weight=ft.FontWeight.BOLD,
            )
        self.bgcolor = coloresConstantes.COLOR_CARD_ACTIVO
        self.tarea.activo = True
        self.btnBorrar.visible = True
        self.entradaEditar.visible = False
        self.btnEditar.visible = False
        self.tarea.activo = True
        self.completada = self.tarea.activo




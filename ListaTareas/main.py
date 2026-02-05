from clases.gestorDB import GestorDBTareas
from clases.gestorTareas import GestorTareas
from clases.tarea import Tarea
import coloresConstantes
from task import Task
import flet as ft




listaTareas = GestorTareas()

def main(page: ft.Page):

    def agregarTarea(e):
        try:
            if entradaTarea.value != "" and len(entradaTarea.value) <= 35:

                new_tarea = Tarea(descripcion=entradaTarea.value,activo=False)
                task = Task(new_tarea)
                
                task.agregarTarea()
                entradaTarea.value = ""
                contenedorTareas.update()
        except Exception as e:
            print(f"{e}")


    def obtenerTareas():
        db = GestorDBTareas()
        tareasDb = []
        try:
            for tareas in db.verTareas():
                descripcion, activo, *demas = tareas
                if activo:
                    newTarea = Tarea(descripcion, True)
                    task = Task(newTarea)
                    tareasDb.append(task)
                else:
                    newTarea = Tarea(descripcion, False)
                    task = Task(newTarea)
                    tareasDb.append(task)
        except:
            print("base de datos vacia")

        return tareasDb

    listaTareas.tareas.extend(obtenerTareas())


    page.window.width = 500
    page.window.height = 500
    page.bgcolor = "#2A2E35"
    page.window.resizable = False



    titulo = ft.Text("Mis tareas")
    titulo.style = ft.TextStyle(size=30, color=coloresConstantes.TEXTO_COLOR,weight=ft.FontWeight.BOLD)

    contenedorTitulo = ft.Container(
        content=ft.Column(
            controls=[
                titulo
            ]
        ),
    )



    entradaTarea = ft.TextField()
    entradaTarea.color = coloresConstantes.TEXTO_COLOR
    # entradaTarea.border = ft.InputBorder.NONE
    entradaTarea.width = 390
    entradaTarea.border_radius = 10
    entradaTarea.border_color = "black"
    entradaTarea.autofocus = True

    btnAgregar = ft.FloatingActionButton(
        bgcolor= coloresConstantes.COLOR_BOTON_ADD,
        icon=ft.Icon(icon=ft.Icons.ADD),
        hover_elevation= 1000.56,
        on_click=agregarTarea
        )
    

    contenedorEntrada = ft.Container(
        content=ft.Row(
            controls=[
                entradaTarea,
                btnAgregar,
            ],

        )
    )

    contenedorTareas = ft.Container(
        content=ft.Column(
            controls=listaTareas.getTareas(),
            scroll=ft.ScrollMode.AUTO
        ),

        width = 490,
        height = 270,
        padding = 12,
        bgcolor=coloresConstantes.COLOR_CONTENDOR_CARDS,
        border_radius=10

    )


    contenedorTitulo.padding = 14
    page.add(ft.Column(
        controls=[
            contenedorTitulo,
            contenedorEntrada,
            contenedorTareas
        ]))

if __name__ == "__main__":
    ft.run(main)


from clases.tarea import Tarea



class GestorTareas:
    tareas = []
    def __init__(self):
        self.totalTareas = len(self.getTareas())

    def addTarea(self, tarea):
        self.tareas.append(tarea)

    def getTareas(self):
        return self.tareas

    def removeTarea(self, tarea):
        self.tareas.remove(tarea)
    
    




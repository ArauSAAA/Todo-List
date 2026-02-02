import datetime



class Tarea:
    def __init__(self,descripcion:str, activo:bool):
        self.descripcion = descripcion
        self.activo = activo
        self.__horaCreacion = datetime.datetime.now().strftime("%d:%m:%Y %H:%M:%S")


    @property
    def horaCreacion(self):
        return self.__horaCreacion
    
    def __str__(self):
        return f"Tarea(descripcion={self.descripcion}, activo={self.activo})"
    

uno = Tarea("Estudiar", False)

if __name__ == "__main__":
    print(uno.horaCreacion)
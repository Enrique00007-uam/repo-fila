"""Desarrolle un programa en Python que simule una Cola_de_atencion de atención en una clínica. El sistema
debe permitir agregar pacientes a la Cola_de_atencion (registro de llegada), atender al siguiente paciente
(eliminar el primero en la Cola_de_atencion) y mostrar en pantalla la lista actual de pacientes en espera. El
docente implementará el programa paso a paso, explicando cada parte del código, mientras los
estudiantes proponen mejoras, prueban con distintos datos y analizan el comportamiento de la
estructura tipo Cola_de_atencion."""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola_de_atencion:
    def __init__(self):
        self.frente = None
        self.final = None
        
#Metodo para insertar pacientes en la cola
    def registro (self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:   
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        print("Paciente insertado:", dato)
    
    #Metodo que atiende y elimina al paciente al frente de la cola

    def atender(self):
        if self.frente is None:
            print("Cola vacia, noy hay pacientes para atender.")
            return
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print("Paciente atendido:", eliminado) 
        return eliminado
    #Metodo que muestra todos los pacietes de la cola

    def mostrar_lista(self):
        if self.frente is None:
            print("Cola vacia, noy hay pacientes para atender.")
        
        else:
            print("Pacientes en la cola:")
            actual = self.frente
            while actual:
                    print(actual.dato, end=", ")
                    actual = actual.siguiente
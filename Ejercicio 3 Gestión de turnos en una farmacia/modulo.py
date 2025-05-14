"""Implemente un sistema de turnos en una farmacia, donde los pacientes son atendidos en el
orden en que llegan. Cada paciente tiene un nombre y un tipo de servicio (compra, consulta,
receta). El sistema debe permitir registrar nuevos pacientes, atender al siguiente en la fila y
mostrar los turnos pendientes."""

#class Nodo:
class Paciente:
    def __init__(self, nombre, tipo_servicio):
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola_de_atencion:
    def __init__(self):
        self.frente = None
        self.final = None
        
#Metodo para insertar pacientes en la cola
    def registro (self, nombre,tipo_servicio ):   
        nuevo_paciente = Paciente(nombre,tipo_servicio) 
        nuevo_nodo = Nodo(nuevo_paciente)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:   
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        print("Paciente insertado:", nombre, "Servicio nesesitado:", tipo_servicio)
    
    #Metodo que atiende y elimina al paciente al frente de la cola

    def atender(self):
        if self.frente is None:
            print("Cola vacia, noy hay pacientes para atender.")
            return
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print("Paciente atendido:", eliminado.nombre, ", Servicio recibido:", eliminado.tipo_servicio) 
        return eliminado
    #Metodo que muestra todos los pacietes de la cola

    def mostrar_lista(self):
        if self.frente is None:
            print("Cola vacia, noy hay pacientes para atender.")
        
        else:
            print("Pacientes en la cola:")
            actual = self.frente
            while actual:
                    print(f"Nombre: {actual.dato.nombre}, servicio: {actual.dato.tipo_servicio}")
                    actual = actual.siguiente
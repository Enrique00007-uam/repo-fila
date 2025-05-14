from modulo import Paciente, Cola_de_atencion

# Crea una instancia de la clase Cola_de_atencion para manejar la cola de pacientes
cola = Cola_de_atencion()

# función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú de Gestión de Turnos ---")
    print("1. Registrar nuevo paciente")
    print("2. Atender siguiente paciente")
    print("3. Mostrar turnos pendientes")
    print("4. Salir")

# Define la función principal
def main():
    # Inicia un bucle para mantener el programa en ejecución hasta que el usuario decida salir
    while True:
        # Muestra el menú de opciones
        mostrar_menu()
        # Solicita al usuario que ingrese una opción
        opcion = input("Seleccione una opción: ")

        # Evalúa la opción ingresada por el usuario
        if opcion == '1':
            #registra un nuevo paciente
            nombre = input("Ingrese el nombre del paciente: ")
            #validacion
            while True:
                tipo_servicio = input("Ingrese el tipo de servicio (compra, consulta, receta): ").lower()
                if tipo_servicio in ["compra", "consulta", "receta"]:
                    break
                else:
                    print("Tipo de servicio no válido. Por favor, ingrese 'compra', 'consulta' o 'receta'.")
            # Llama al método registro para agregar el paciente
            cola.registro(nombre, tipo_servicio)
        elif opcion == '2':
            #atiende y elimina al siguiente paciente
            cola.atender()   
        elif opcion == '3':
            #muestra la lista y los turnos pendientes
            cola.mostrar_lista()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break  # Termina el bucle while
        else:
            # Si la opción no es válida, informa al usuario
            print("Opción no válida. Por favor, intente de nuevo.")


main()


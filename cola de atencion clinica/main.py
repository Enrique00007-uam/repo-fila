from modulo import Cola_de_atencion

# Crea una instancia de la clase Cola_de_atencion
cola = Cola_de_atencion()

# Bucle principal del programa para mostrar el menú y procesar opciones
while True:
    print("\nMenú de Atención Clínica:")
    print("1. Agregar paciente a la cola")
    print("2. Atender próximo paciente")
    print("3. Mostrar cola de pacientes")
    print("4. Salir")

    # Solicita al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Evalúa la opción seleccionada por el usuario
    if opcion == '1':
        #solicita el nombre del paciente 
        #y Llama al método registro de la  cola para agregar al paciente
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        cola.registro(nombre_paciente)
    elif opcion == '2':
        # llama al método atender de la cola
        cola.atender()
    elif opcion == '3':
        #llama al método mostrar_lista de la instancia cola
        cola.mostrar_lista()
    elif opcion == '4':
        #termina el bucle
        print("Saliendo del sistema.")
        break
    else:
        # Si la opción no es válida, informa al usuario
        print("Opción no válida. Por favor, intente de nuevo.")
while True:
    respuesta = input("¿Desea continuar Si/No? ").strip().strip('$')
    
    #verificar si el usuario escribió "No"
    if respuesta.lower() == "no":
        print("Programa finalizado.")
        break
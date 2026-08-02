import random
ids = []
titulos = []
categorias = []
niveles = []
preguntas = []
respuestas = []
observaciones = []
#-----------------------------------------------#
#--|menu_principal_aleatorizador_de_preguntas|--#
#-----------------------------------------------#
while True:
    print("menu principal aleatorizador de preguntas")
    print("1) crear pregunta")
    print("2) editar pregunta")
    print("3) eliminar pregunta")
    print("4) buscar pregunta")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_pregunta|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_pregunta = 1
        else:
            id_pregunta = ids[-1] + 1
        titulo = input("título de la pregunta: ")
        categoria = input("categoría: ")
        nivel = input("nivel de dificultad: ")
        pregunta = input("pregunta: ")
        respuesta = input("respuesta: ")
        observacion = input("observación: ")
        ids.append(id_pregunta)
        titulos.append(titulo)
        categorias.append(categoria)
        niveles.append(nivel)
        preguntas.append(pregunta)
        respuestas.append(respuesta)
        observaciones.append(observacion)
        print("pregunta registrada correctamente.")
        print("id:", id_pregunta)
    #---------------------#
    #--|editar_pregunta|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar pregunta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {preguntas[i]} | {respuestas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {preguntas[posicion]} | {respuestas[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                categorias[posicion] = input("nueva categoría: ")
                niveles[posicion] = input("nuevo nivel de dificultad: ")
                preguntas[posicion] = input("nueva pregunta: ")
                respuestas[posicion] = input("nueva respuesta: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_pregunta|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar pregunta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {preguntas[i]} | {respuestas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {preguntas[posicion]} | {respuestas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    categorias.pop(posicion)
                    niveles.pop(posicion)
                    preguntas.pop(posicion)
                    respuestas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_pregunta|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar pregunta")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {preguntas[posicion]} | {respuestas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            facil = 0
            media = 0
            dificil = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {preguntas[i]} | {respuestas[i]} | {observaciones[i]}")
                if niveles[i].lower() == "fácil" or niveles[i].lower() == "facil":
                    facil += 1
                elif niveles[i].lower() == "media":
                    media += 1
                elif niveles[i].lower() == "difícil" or niveles[i].lower() == "dificil":
                    dificil += 1
            print("estadísticas aleatorizador de preguntas")
            print("cantidad de preguntas:", len(ids))
            print("preguntas fáciles:", facil)
            print("preguntas medias:", media)
            print("preguntas difíciles:", dificil)
            posicion = random.randint(0, len(ids) - 1)
            print("pregunta seleccionada aleatoriamente")
            print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {preguntas[posicion]} | {respuestas[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de preguntas.")
        break
    else:
        print("opción no válida.")
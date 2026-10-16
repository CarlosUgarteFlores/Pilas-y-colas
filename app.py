# app_consola.py
import logica


def ejecutar_menu():
    while True:
        print("\n" + "="*35)
        print("   GESTOR DE SOLICITUDES (CLI)")
        print("="*35)
        print("1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Consultar siguiente turno (Reto 1)")
        print("5. Buscar solicitud por ID (Reto 2)")
        print("6. Cancelar solicitud (Reto 3)")
        print("7. Deshacer varias atenciones (Reto 4)")
        print("8. Ver estadísticas (Reto 5)")
        print("9. Mostrar estado completo")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            res = logica.registrar_solicitud(cliente, asunto)
            if isinstance(res, dict) and "error" in res:
                print("Error:", res["error"])
            elif res:
                print(f"Registrada con éxito [ID #{res['id']}]")
            else:
                print("Error: Datos inválidos.")

        elif opcion == "2":
            atendida = logica.atender_siguiente()
            print("Atendida:", atendida if atendida else "No hay solicitudes pendientes.")

        elif opcion == "3":
            restaurada = logica.deshacer_ultima_atencion()
            print("Restaurada a la cola:", restaurada if restaurada else "No hay historial para deshacer.")

        elif opcion == "4":
            siguiente = logica.consultar_siguiente()
            print("Próximo turno:", siguiente if siguiente else "Cola vacía.")

        elif opcion == "5":
            try:
                sol_id = int(input("Ingrese ID a buscar: "))
                item, estado = logica.buscar_por_id(sol_id)
                if item:
                    print(f"Encontrado: {item} | Estado actual: {estado}")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == "6":
            try:
                sol_id = int(input("Ingrese ID de la solicitud a cancelar: "))
                cancelada = logica.cancelar_solicitud(sol_id)
                if cancelada:
                    print("Solicitud cancelada:", cancelada)
                else:
                    print("ID no encontrado en la cola de pendientes.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")

        elif opcion == "7":
            try:
                cant = int(input("¿Cuántas atenciones desea deshacer?: "))
                total = logica.deshacer_varias_atenciones(cant)
                print(f"Se restauraron {total} solicitudes.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")

        elif opcion == "8":
            stats = logica.obtener_estadisticas()
            print("\n--- Estadísticas ---")
            print(f"Pendientes: {stats['total_pendientes']}")
            print(f"Atendidas:  {stats['total_atendidas']}")
            print(f"Total:      {stats['total_procesadas']}")

        elif opcion == "9":
            logica.mostrar_estado()

        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar_menu()
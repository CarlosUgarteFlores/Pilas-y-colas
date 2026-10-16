
cola_pendientes = []
pila_historial = []
siguiente_id = 1


def mostrar_estado():
    print("\nPendientes (FIFO):", cola_pendientes)
    print("Historial (LIFO):", pila_historial)


def registrar_solicitud(cliente: str, asunto: str):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None


    for item in cola_pendientes:
        if item["cliente"].lower() == cliente.strip().lower() and item["asunto"].lower() == asunto.strip().lower():
            return {"error": "Solicitud duplicada ya se encuentra en cola pendientes."}

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
        "estado": "pendiente"
    }
    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud


def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud


def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud


def consultar_siguiente():
    if not cola_pendientes:
        return None
    return cola_pendientes[0]


# Reto 2: Buscar una solicitud por ID
def buscar_por_id(id_solicitud: int):
    for item in cola_pendientes:
        if item["id"] == id_solicitud:
            return item, "pendiente"
    for item in pila_historial:
        if item["id"] == id_solicitud:
            return item, "atendida"
    return None, None


def cancelar_solicitud(id_solicitud: int):
    for idx, item in enumerate(cola_pendientes):
        if item["id"] == id_solicitud:
            return cola_pendientes.pop(idx)
    return None



def deshacer_varias_atenciones(cantidad: int) -> int:
    if cantidad <= 0:
        return 0
    
    restauradas = 0
    while restauradas < cantidad and pila_historial:
        deshacer_ultima_atencion()
        restauradas += 1
    return restauradas



def obtener_estadisticas():
    return {
        "total_pendientes": len(cola_pendientes),
        "total_atendidas": len(pila_historial),
        "total_procesadas": len(cola_pendientes) + len(pila_historial)
    }
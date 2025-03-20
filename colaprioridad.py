import heapq

cola_prioridad = []

heapq.heappush(cola_prioridad, (1, "Pepe"))
heapq.heappush(cola_prioridad, (2, "Paco"))
heapq.heappush(cola_prioridad, (3, "Juan"))
heapq.heappush(cola_prioridad, (4, "Maria"))
heapq.heappush(cola_prioridad, (5, "Luis"))

while cola_prioridad:
    prioridad,paciente = heapq.heappop(cola_prioridad)
    print(f'Atendiendo al paciente {paciente} con prioridad {prioridad}')
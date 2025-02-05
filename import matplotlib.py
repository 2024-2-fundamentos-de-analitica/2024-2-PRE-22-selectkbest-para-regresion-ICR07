import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.DiGraph()

# Nodo principal
G.add_node("Selección y Gestión de Proveedores")

# Subtemas principales
subtemas = [
    "Planificación y Requisitos",
    "Identificación de Proveedores",
    "Preparar y Emitir RFP",
    "Evaluar Propuestas y Seleccionar Proveedor",
    "Acuerdo Formal",
    "Gestión del Proveedor",
    "Aceptación del Software",
    "Implementación"
]

# Agregar subtemas al nodo principal
for sub in subtemas:
    G.add_edge("Selección y Gestión de Proveedores", sub)

# Detalles para cada subtema
detalles = {
    "Planificación y Requisitos": ["Definir requisitos", "Decidir subcontratación", "Formar equipo de evaluación"],
    "Identificación de Proveedores": ["Relaciones previas", "Investigación", "Recomendaciones", "Lista corta de proveedores"],
    "Preparar y Emitir RFP": ["Definir criterios", "Emitir solicitud", "Evaluar respuestas"],
    "Evaluar Propuestas y Seleccionar Proveedor": ["Análisis detallado", "Presentaciones", "Verificación de referencias"],
    "Acuerdo Formal": ["Contrato legal", "Declaración de trabajo", "Acuerdo de nivel de servicio", "Escrow"],
    "Gestión del Proveedor": ["Monitoreo", "Gestión de riesgos", "Revisión de progreso"],
    "Aceptación del Software": ["Pruebas de aceptación", "Corrección de defectos", "Validación final"],
    "Implementación": ["Despliegue", "Capacitación", "Mantenimiento"]
}

# Agregar detalles a cada subtema
for subtema, items in detalles.items():
    for item in items:
        G.add_edge(subtema, item)

# Dibujar el mapa mental
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=9, font_weight="bold", arrows=True)
plt.title("Mapa Mental: Selección y Gestión de Proveedores")
plt.show()

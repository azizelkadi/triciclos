import sys
from pyspark import SparkContext

# Procesa cada línea del archivo y crea una arista ordenada lexicográficamente
def process_edge(line):
    edge = line.strip().split(',')
    n1, n2 = edge[0].strip(), edge[1].strip()
    return (n1, n2) if n1 < n2 else (n2, n1)

# Genera posibles triángulos a partir de un nodo y sus vecinos
def generate_possible_triangles(node_neighbors):
    node, neighbors = node_neighbors
    return [((node, n1), n2) for n1 in neighbors for n2 in neighbors if n1 < n2]

# Encuentra todos los 3-ciclos en el conjunto de datos utilizando un enfoque basado en RDD
def find_triangles(edges_rdd):
    # Genera posibles triángulos utilizando un enfoque de "nodo-vecinos"
    possible_triangles = edges_rdd.flatMap(lambda edge: [(edge[0], edge[1]), (edge[1], edge[0])]) \
                                   .groupByKey() \
                                   .flatMap(generate_possible_triangles)
    
    # Filtra aquellos que son triángulos válidos
    valid_edges = edges_rdd.map(lambda edge: (edge, 1))
    triangles_rdd = possible_triangles.join(valid_edges) \
                                      .map(lambda node_edge_edge: (node_edge_edge[0][0], node_edge_edge[0][1], node_edge_edge[1][0])) \
                                      .distinct()

    return triangles_rdd

# Función main
def main(sc, files):
    # Leer los archivos y procesar las aristas
    edges_rdd = sc.textFile(','.join(files)).map(process_edge).distinct()

    # Encontrar los 3-ciclos
    triangles_rdd = find_triangles(edges_rdd)

    # Imprimir resultados
    triangles = triangles_rdd.collect()
    print("-" * 50)
    print(f"Cantidad de 3-ciclos encontrados: {len(triangles)}")
    print("Lista de 3-ciclos encontrados:")
    for triangle in triangles:
        print(triangle)
    print("-" * 50)

if __name__ == "__main__":
    # Comprobamos si se han introducido los argumentos necesarios
    if len(sys.argv) < 2:
        print("python3 2_multifichero.py <grafo_1/n> <grafo_2/n> ... <grafo_n/n>")
    # Ejecutamos el proceso
    else:
        files = sys.argv[1:]
        with SparkContext() as sc:
            sc.setLogLevel("ERROR")
            main(sc, files)

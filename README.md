# Triciclos en un grafo

Este proyecto se centra en encontrar 3-ciclos en grafos utilizando el módulo PySpark de Apache Spark. Spark permite paralelizar procesos y mejorar el rendimiento al procesar grandes conjuntos de datos. El objetivo del proyecto es practicar y familiarizarse con PySpark y sus funciones en la resolución de problemas reales, como el análisis de grafos.

## Instrucciones de uso

### 1 - Triciclos en un grafo

Archivo: `1_triciclos.py`

Procesa un único grafo y encuentra los 3-ciclos en él. Para ejecutar este archivo, se debe utilizar la siguiente línea de comando:

```
python3 1_triciclos.py <grafo>
```

<grafo>: Ruta del archivo de texto que contiene las aristas del grafo.

### 2 - Triciclos en múltiples grafos concatenados

Archivo: `2_multifichero.py`

Procesa múltiples grafos dados concatenándolos y encuentra los 3-ciclos en el grafo resultante. Para ejecutar este archivo, se debe utilizar la siguiente línea de comando:

```
python3 2_multifichero.py <grafo_1/n> <grafo_2/n> ... <grafo_n/n>
```

<grafo_1/n>, <grafo_2/n>, ..., <grafo_n/n>: Rutas de los archivos de texto que contienen las aristas de los grafos.

### 3 - Triciclos en múltiples grafos de forma individual

Archivo: `3_triciclo_local.py`

Procesa múltiples grafos de forma individual y encuentra los 3-ciclos en cada grafo. Para ejecutar este archivo, se debe utilizar la siguiente línea de comando:

```
python3 3_triciclo_local.py <grafo_1/n> <grafo_2/n> ... <grafo_n/n>
```
  
<grafo_1/n>, <grafo_2/n>, ..., <grafo_n/n>: Rutas de los archivos de texto que contienen las aristas de los grafos.
  
  
## Formato de archivos de entrada

Los archivos de texto de entrada que contienen las aristas de los grafos deben seguir el siguiente formato:


```
nodo1, nodo2
nodo3, nodo4
nodo2, nodo3
```

Cada línea representa una arista entre dos nodos, separados por una coma y un espacio. No hay restricciones en el orden de las aristas.

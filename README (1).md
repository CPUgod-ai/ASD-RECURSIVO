# Taller — Conjuntos PRIMEROS, SIGUIENTES y PREDICCIÓN

## Introduccion

En este taller se construye un programa en Python que recibe una gramática libre de contexto y calcula automáticamente los conjuntos de **PRIMEROS**, **SIGUIENTES** y **PREDICCIÓN** de todos sus no terminales y reglas de producción.

El programa está organizado en cuatro archivos separados: uno con la lógica principal de los algoritmos, dos con la definición de cada gramática y uno como punto de entrada.

---

## Estructura del proyecto

Todos los archivos tienen que estar en la misma carpeta. Si no están juntos, el programa no va a encontrar los módulos que importa y va a fallar.

```
conjuntos_gramatica/
├── main.py          <- punto de entrada, desde acá se corre todo
├── grammar.py       <- clase Gramatica con los tres algoritmos
├── gramatica1.py    <- definición y producciones de la Gramática 1
└── gramatica2.py    <- definición y producciones de la Gramática 2
```

> `main.py` importa `construir_gramatica1` y `construir_gramatica2` directamente desde sus archivos. Si se mueve uno sin el otro va a aparecer un `ModuleNotFoundError`.

---

## Requisitos

No se necesitan librerías externas. Solo se necesita tener instalado **Python 3.10 o superior** (por las anotaciones de tipo en los métodos).

Para verificar la versión instalada:

```bash
python --version
```

---

## Como ejecutar el taller

### Windows

Abrir la terminal y navegar hasta la carpeta del proyecto:

```bash
cd C:\Users\tu_usuario\Documents\conjuntos_gramatica
```

Correr el programa:

```bash
python main.py
```




### Linux

Abrir la terminal y navegar hasta la carpeta del proyecto:

```bash
cd ~/Documentos/conjuntos_gramatica
```

Correr el programa:

```bash
python3 main.py
```



### MacOS

Abrir la terminal y navegar hasta la carpeta del proyecto:

```bash
cd ~/Documents/conjuntos_gramatica
```

Correr el programa:

```bash
python3 main.py
```



> En los tres sistemas el programa imprime los resultados directamente en consola. No crea carpetas ni archivos adicionales.

---

## Que hace cada archivo

### `grammar.py`
Es el núcleo del taller. Contiene la clase `Gramatica` con los tres algoritmos implementados como métodos:

- **`calcular_primeros()`**: recorre las producciones por punto fijo. Para cada no terminal expande sus reglas y acumula los primeros de cada secuencia. Si todos los símbolos de una producción pueden derivar ε, añade ε al resultado.
- **`calcular_siguientes()`**: también trabaja por punto fijo. Para cada aparición de un no terminal en el lado derecho de una regla, añade PRIMEROS de lo que le sigue; si ese resto puede derivar ε, propaga SIGUIENTES de la cabeza de la regla.
- **`calcular_prediccion()`**: para cada regla `A → α` toma PRIMEROS(α); si ε está en PRIMEROS(α), añade también SIGUIENTES(A).

### `gramatica1.py`
Define la Gramática 1 con sus terminales, no terminales y producciones. Puede ejecutarse solo con `python gramatica1.py` para ver únicamente sus resultados.

### `gramatica2.py`
Define la Gramática 2 con sus terminales, no terminales y producciones. Puede ejecutarse solo con `python gramatica2.py` para ver únicamente sus resultados.

### `main.py`
Punto de entrada del taller. Importa ambas gramáticas, llama a `imprimir_resultados()` en cada una y muestra todo en consola.

---

## Gramaticas utilizadas

### Gramática 1

```
S  →  A uno B C  |  S dos
A  →  B C D  |  A tres  |  ε
B  →  D cuatro C tres  |  ε
C  →  cinco D B  |  ε
D  →  seis  |  ε
```

### Gramática 2

```
S  →  A B uno
A  →  dos B  |  ε
B  →  C D  |  tres  |  ε
C  →  cuatro A B  |  cinco
D  →  seis  |  ε
```

---

## Salida en consola

Cuando se corre `main.py` la consola muestra algo así:


<img width="817" height="648" alt="image" src="https://github.com/user-attachments/assets/29ddffdc-ae10-4fad-838c-3fcfd1e0af81" />

<img width="592" height="347" alt="image" src="https://github.com/user-attachments/assets/dcea50f7-66dd-4ca4-aee6-498fd5bd1618" />

---

## Resultados

### Gramática 1 — PRIMEROS

<img width="552" height="165" alt="image" src="https://github.com/user-attachments/assets/3ba2fb52-8579-4e22-a97a-cf81a813bc3c" />


### Gramática 1 — SIGUIENTES

<img width="511" height="147" alt="image" src="https://github.com/user-attachments/assets/bb9809ce-43a0-4c7f-a3de-3e98ecb20049" />

### Gramática 1 — PREDICIONES
<img width="568" height="288" alt="image" src="https://github.com/user-attachments/assets/62fe225b-db7b-4830-b473-e6204ece6530" />

### Gramática 2 — PRIMEROS

<img width="482" height="152" alt="image" src="https://github.com/user-attachments/assets/a13c26d4-8e34-4eed-a773-cc9771744648" />


### Gramática 2 — SIGUIENTES

<img width="497" height="143" alt="image" src="https://github.com/user-attachments/assets/394a2477-640b-44ee-94b6-19d3b6c3eb4c" />

### Gramática 2 — PREDICCIONES
<img width="553" height="253" alt="image" src="https://github.com/user-attachments/assets/8b431898-9aa5-48bf-b8f7-291ddffc6fdf" />

---

## Analisis

Los conjuntos calculados confirman que los algoritmos respetan correctamente las reglas de la teoría de compiladores.

En la Gramática 1, el hecho de que `A`, `B`, `C` y `D` puedan derivar ε hace que sus conjuntos PRIMEROS incluyan épsilon y obliga a propagar SIGUIENTES en múltiples niveles. Por ejemplo, PRIMEROS(S) no incluye ε porque aunque A puede desaparecer, después viene el terminal `uno` que siempre aparece.

En la Gramática 2, la cadena `S → A B uno` combina dos no terminales que pueden derivar ε antes del terminal fijo `uno`, lo que hace que PRIMEROS(S) incluya `uno` directamente. Esto se refleja en los conjuntos de PREDICCIÓN donde varias reglas comparten tokens, lo que indica que esta gramática no es LL(1) sin transformaciones adicionales.

---

## Conclusion

Este taller permitió aplicar de forma práctica los algoritmos de PRIMEROS, SIGUIENTES y PREDICCIÓN sobre dos gramáticas con distintos niveles de complejidad. El diseño en archivos separados facilita agregar nuevas gramáticas sin modificar la lógica central: basta con crear un nuevo archivo siguiendo el patrón de `gramatica1.py` e importarlo en `main.py`.

Lo más importante del ejercicio es entender que estos conjuntos no son un fin en sí mismos, sino la base para construir tablas de análisis sintáctico LL(1) que los compiladores usan para decidir qué regla aplicar en cada paso del parseo.

---

## Tecnologias usadas

- [`Python 3.10+`](https://www.python.org/) — lenguaje de implementación
- Sin dependencias externas — solo la librería estándar de Python

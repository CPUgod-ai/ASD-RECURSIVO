EPSILON = 'ε'  # Símbolo que representa la cadena vacía
FIN = '$'       # Marca el fin de la entrada en los conjuntos SIGUIENTES


class Gramatica:

    def __init__(self, nombre, terminales, no_terminales, producciones, inicio):
        self.nombre = nombre
        self.terminales = terminales          
        self.no_terminales = no_terminales    
        self.producciones = producciones      
        self.inicio = inicio                 
        self.primeros = {}                   
        self.siguientes = {}                  
        self.prediccion = {}                  

    def primeros_de_secuencia(self, secuencia):
        resultado = set()
        # Recorre cada símbolo de la secuencia acumulando sus primeros
        for simbolo in secuencia:
            if simbolo == EPSILON:
                resultado.add(EPSILON)
                break
            primeros_simbolo = self.primero_de(simbolo)
            resultado |= (primeros_simbolo - {EPSILON})  # Agrega primeros sin incluir ε
            if EPSILON not in primeros_simbolo:           # Si no deriva ε, la secuencia se detiene aquí
                break
        else:
            resultado.add(EPSILON)  # Todos los símbolos derivan ε, entonces la secuencia también
        return resultado

    def primero_de(self, simbolo):
        if simbolo in self.terminales or simbolo == EPSILON:
            return {simbolo}                  # Los terminales son su propio primer
        if simbolo not in self.primeros:
            self.primeros[simbolo] = set()    # Inicializa vacío para cortar posibles ciclos
            # Recorre cada producción del símbolo y acumula sus primeros
            for prod in self.producciones.get(simbolo, []):
                self.primeros[simbolo] |= self.primeros_de_secuencia(prod)
        return self.primeros[simbolo]

    def calcular_primeros(self):
        # Inicializa todos los conjuntos PRIMEROS como vacíos
        for nt in self.no_terminales:
            self.primeros[nt] = set()
        hubo_cambio = True
        while hubo_cambio:                    # Punto fijo: repite hasta que no haya cambios
            hubo_cambio = False
            # Recorre cada no terminal para recalcular su conjunto PRIMEROS
            for nt in self.no_terminales:
                anterior = set(self.primeros[nt])
                # Recorre cada producción del no terminal y acumula sus primeros
                for prod in self.producciones[nt]:
                    self.primeros[nt] |= self.primeros_de_secuencia(prod)
                if self.primeros[nt] != anterior:
                    hubo_cambio = True        # Hubo cambio, se necesita otra iteración

    def calcular_siguientes(self):
        self.calcular_primeros()              # PRIMEROS debe estar listo antes de calcular SIGUIENTES
        # Inicializa todos los conjuntos SIGUIENTES como vacíos
        for nt in self.no_terminales:
            self.siguientes[nt] = set()
        self.siguientes[self.inicio].add(FIN) # Regla 1: el símbolo inicial siempre contiene $
        hubo_cambio = True
        while hubo_cambio:                    # Punto fijo: repite hasta que no haya cambios
            hubo_cambio = False
            # Recorre cada no terminal junto con sus producciones
            for nt, prods in self.producciones.items():
                # Recorre cada producción del no terminal actual
                for prod in prods:
                    # Recorre cada símbolo de la producción buscando no terminales
                    for i, simbolo in enumerate(prod):
                        if simbolo not in self.no_terminales:
                            continue
                        beta = prod[i + 1:]   # β es la cadena que sigue al símbolo actual
                        primeros_beta = self.primeros_de_secuencia(beta) if beta else {EPSILON}
                        anterior = set(self.siguientes[simbolo])
                        self.siguientes[simbolo] |= (primeros_beta - {EPSILON})  # Regla 2
                        if EPSILON in primeros_beta:
                            self.siguientes[simbolo] |= self.siguientes[nt]      # Regla 3: β deriva ε, propaga SIGUIENTES de la cabeza
                        if self.siguientes[simbolo] != anterior:
                            hubo_cambio = True

    def calcular_prediccion(self):
        self.calcular_siguientes()            # SIGUIENTES debe estar listo antes de calcular PREDICCIÓN
        # Recorre cada no terminal junto con sus producciones
        for nt, prods in self.producciones.items():
            # Recorre cada producción con su índice para construir la clave del diccionario
            for indice, prod in enumerate(prods):
                primeros_prod = self.primeros_de_secuencia(prod)  # PRIMEROS de la producción completa
                pred = primeros_prod - {EPSILON}
                if EPSILON in primeros_prod:
                    pred |= self.siguientes[nt]   # Si la producción deriva ε, se añaden SIGUIENTES del NT
                self.prediccion[(nt, indice)] = pred

    @staticmethod
    def prod_a_texto(prod):
        return ' '.join(prod)  # Convierte la lista de símbolos en una cadena legible

    def imprimir_resultados(self):
        self.calcular_prediccion()            # Dispara la cadena: PRIMEROS → SIGUIENTES → PREDICCIÓN

        print("=" * 60)
        print(f"  {self.nombre}")
        print("=" * 60)

        print("\n Producciones:")
        # Recorre cada no terminal e imprime todas sus producciones
        for nt, prods in self.producciones.items():
            for prod in prods:
                print(f"   {nt} → {self.prod_a_texto(prod)}")

        print("\n PRIMEROS:")
        # Recorre los no terminales en orden alfabético e imprime sus conjuntos PRIMEROS
        for nt in sorted(self.no_terminales):
            tokens = ", ".join(sorted(self.primeros[nt]))
            print(f"   PRIMEROS({nt}) = {{ {tokens} }}")

        print("\n SIGUIENTES:")
        # Recorre los no terminales en orden alfabético e imprime sus conjuntos SIGUIENTES
        for nt in sorted(self.no_terminales):
            tokens = ", ".join(sorted(self.siguientes[nt]))
            print(f"   SIGUIENTES({nt}) = {{ {tokens} }}")

        print("\n PREDICCIÓN:")
        # Recorre cada producción e imprime su conjunto de PREDICCIÓN
        for nt, prods in self.producciones.items():
            for indice, prod in enumerate(prods):
                tokens = ", ".join(sorted(self.prediccion[(nt, indice)]))
                print(f"   PRED({nt} → {self.prod_a_texto(prod)}) = {{ {tokens} }}")

        print()
from grammar import Gramatica, EPSILON


def construir_gramatica1():
    terminales = {'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis'}
    no_terminales = {'S', 'A', 'B', 'C', 'D'}
    producciones = {
        'S': [
            ['A', 'uno', 'B', 'C'],   # S → A uno B C
            ['S', 'dos'],              # S → S dos
        ],
        'A': [
            ['B', 'C', 'D'],           # A → B C D
            ['A', 'tres'],             # A → A tres
            [EPSILON],                 # A → ε
        ],
        'B': [
            ['D', 'cuatro', 'C', 'tres'],  # B → D cuatro C tres
            [EPSILON],                     # B → ε
        ],
        'C': [
            ['cinco', 'D', 'B'],      # C → cinco D B
            [EPSILON],                # C → ε
        ],
        'D': [
            ['seis'],                 # D → seis
            [EPSILON],                # D → ε
        ],
    }
    return Gramatica("GRAMÁTICA 1", terminales, no_terminales, producciones, 'S')


if __name__ == '__main__':
    construir_gramatica1().imprimir_resultados()

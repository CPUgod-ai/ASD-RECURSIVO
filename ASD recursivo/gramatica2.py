from grammar import Gramatica, EPSILON


def construir_gramatica2():
    terminales = {'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis'}
    no_terminales = {'S', 'A', 'B', 'C', 'D'}
    producciones = {
        'S': [
            ['A', 'B', 'uno'],        # S → A B uno
        ],
        'A': [
            ['dos', 'B'],             # A → dos B
            [EPSILON],                # A → ε
        ],
        'B': [
            ['C', 'D'],               # B → C D
            ['tres'],                 # B → tres
            [EPSILON],                # B → ε
        ],
        'C': [
            ['cuatro', 'A', 'B'],     # C → cuatro A B
            ['cinco'],                # C → cinco
        ],
        'D': [
            ['seis'],                 # D → seis
            [EPSILON],                # D → ε
        ],
    }
    return Gramatica("GRAMÁTICA 2", terminales, no_terminales, producciones, 'S')


if __name__ == '__main__':
    construir_gramatica2().imprimir_resultados()

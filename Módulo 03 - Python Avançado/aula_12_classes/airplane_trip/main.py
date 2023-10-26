"""
Crie uma classe que representa uma viagem de avião, onde temos como atributos os aeroportos de origem e de destino.
Caso queiramos somar uma viagem de A para B com uma de B para C, o resultado precisa ser uma viagem de A para C.
"""

class Viagem:
    """
    This is the Viagem class that takes two attributes called _origem and _destino and counts the created instances.
    """
    __slots__ = ['_origem', '_destino']   # This setting prohibits new attributes from being created.

    _total_viagens = 0  # This is an attribute of the class that counts how many instances were created in a way that represents the number of trips.

    def __init__(self, origem: str, destino: str) -> None:  # This function is the constructor of instances
        self._origem = origem
        self._destino = destino
        Viagem._total_viagens += 1
    
    @property                       # This decorator defines the origem() or destino() methods as properties.
    def origem(self) -> str:        # This method returns the _origem attribute of a Viagem instance
        return self._origem

    @property
    def destino(self) -> str:    # This method returns the _destino attribute of a Viagem instance
        return self._destino
    
    def __add__(self, airport: "Viagem") -> "Viagem":
        return Viagem(self._origem, airport._destino)

    def __str__(self) -> None:   # This method returns the realized trip.
        return 'Você viajou da cidade {0} para a cidade {1}.\n'.format(self._origem, self._destino)

    @staticmethod                       # Defines a static method.
    def get_total_viagens() -> int:     # Returns the number of realized trips.
        return Viagem._total_viagens

def main() -> None:
    """
    This function is the main function that only configures some instances of the Viagem class.
    """
    print("Informe o nome de 3 cidades que você gostaria de viajar em sequência:\n")
    
    cidades = []
    for cidade in range(3):
        cidades.append(input(f"{cidade+1}ª cidade: "))
    
    viagem_A_B = Viagem(cidades[0], cidades[1])
    viagem_B_C = Viagem(cidades[1], cidades[2])
    viagem_A_C = viagem_A_B + viagem_B_C

    print()
    for viagem in (viagem_A_B, viagem_B_C, viagem_A_C):
        print(viagem)

    print('\nNo total foram realizadas {} viagens.'.format(Viagem.get_total_viagens()))

if __name__ == '__main__':
    main()

"""
SAÍDA:

Informe o nome de 3 cidades que você gostaria de viajar em sequência:

1ª cidade: Caruaru
2ª cidade: Recife
3ª cidade: Balneário Camboriú

Você viajou da cidade Caruaru para a cidade Recife.

Você viajou da cidade Recife para a cidade Balneário Camboriú.

Você viajou da cidade Caruaru para a cidade Balneário Camboriú.


No total foram realizadas 3 viagens.
"""
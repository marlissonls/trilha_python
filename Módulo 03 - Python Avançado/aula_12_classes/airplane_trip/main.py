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
    def destino(self) -> str:       # This method returns the _destino attribute of a Viagem instance
        return self._destino
    
    def viagemOrigemDestino(self) -> None:   # This method shows the realized trip.
        print('\nVocê viajou do {0} para o {1}.'.format(self._origem, self._destino))

    @staticmethod                       # Defines a static method.
    def get_total_viagens() -> int:     # Returns the number of realized trips.
        return Viagem._total_viagens

def main() -> None:
    """
    This function is the main function that only configures some instances of the Viagem class.
    """
    viagem_A_B = Viagem('Aeroporto A', 'Aeroporto B')
    viagem_B_C = Viagem('Aeroporto B', 'Aeroporto C')
    viagem_A_C = Viagem(viagem_A_B.origem, viagem_B_C.destino)

    viagem_A_B.viagemOrigemDestino()
    viagem_B_C.viagemOrigemDestino()
    viagem_A_C.viagemOrigemDestino()
    print('\nNo total foram realizadas {} viagens.'.format(Viagem.get_total_viagens()))

if __name__ == '__main__':
    main()
class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def __vazia(self):
        return len(self.items) == 0

    def topo(self):
        return self.items[-1]


def torre_hanoi(discos, origem: Pilha, destino: Pilha, auxiliar: Pilha) -> None:
    if discos == 1:
        destino.empilhar(origem.desempilhar())
    else:
        torre_hanoi(discos-1, origem, auxiliar, destino)
        destino.empilhar(origem.desempilhar())
        torre_hanoi(discos-1, auxiliar, destino, origem)


torre_origem = Pilha()
torre_destino = Pilha()
torre_auxiliar = Pilha()

discos = 5  # número de discos

# empilhar discos na torre origem, do maior para o menor
for i in range(discos, 0, -1):
    torre_origem.empilhar(i)

# chamar a função para resolver a Torre de Hanoi
torre_hanoi(discos, torre_origem, torre_destino, torre_auxiliar)

# exibir a torre destino após a resolução do problema
while not torre_destino.__vazia():
    print(torre_destino.desempilhar())
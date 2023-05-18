def contar_palavras(texto):
    # Remover pontuação e converter para minúsculas
    texto = texto.lower()
    texto = texto.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    # Dividir o texto em palavras
    palavras = texto.split()

    # Criar a hashtable para armazenar as palavras e suas contagens
    hashtable = {}

    # Contar as palavras
    for palavra in palavras:
        if palavra in hashtable:
            hashtable[palavra] += 1
        else:
            hashtable[palavra] = 1

    return hashtable

# Exemplo de uso
print("\nEste é um contador de palavras de um texto qualquer!")
texto = input("\nDigite um texto: ")
resultado = contar_palavras(texto)
print("\n", resultado)

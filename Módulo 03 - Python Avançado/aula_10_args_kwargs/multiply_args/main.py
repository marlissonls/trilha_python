"""
Crie um programa em python que receba via input n números e faça a multiplicação entre eles e imprima na tela.
Pode receber a quantidade ilimitada de números mas deve-se usar o *args em uma função onde vai receber esses valores e irá realizar a multiplicação. 
Exemplo: 
Se rodar o programa e receber : 5, 4, 5 o resultado será 100. 
Se rodar o programa e receber : 10, 2, 4, 3 o resultado será 240.
"""

def multiply_args(*params: float, product: float = 1) -> float:
    """
    This function takes an unknown number of arguments of type float and returns their product.
    """
    for n in params:
        product *= n
    return product

if __name__ == '__main__':
    product = multiply_args(10, 2, 4, 3)
    print(product)
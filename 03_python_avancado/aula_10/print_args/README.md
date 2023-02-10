Crie uma função chamada que tenha a estrutura para receber 2 argumentos fixos e N argumentos nomeados e no final imprima todos os argumentos passados para essa função: 
Exemplo de passagem de argumentos que a função receberá sem precisar ter nenhuma mudança: 
Chamada da função: teste_Kargs(Carro’, 100, nome=’jose’, chave=’teste’) 
Saída: 
    arg1=carro 
    arg2=100 
    nome=jose 
    chave=teste 
Outros exemplos de chamadas de função que deverão funcionar sem alterar a função: 
teste_Kargs(Carro’, 100, nome=’jose’, chave=’teste’,outrachave=’brasil’, oo=’python’) 
Saída: 
    arg1=carro 
    arg2=100 
    nome=jose 
    chave=teste 
    outrachave = brasil 
    oo = python 
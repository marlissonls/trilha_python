"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário (se nota maior que 7 aprovado se não reprovado). 
No final, mostre o conteúdo gravado no dicionário.

ATENÇÃO:
Acima é o que foi pedido, mas implementei para mais de um aluno e fiz validação das informações
"""

import string

def classLength() -> int:
    """
    This function asks for the number of students in the class and returns it.
    """
    while True:
        try:
            alunos = int(input('\nInforme o número de alunos: '))
            if alunos >= 1:
                break
            else:
                print('Informe uma quantidade de alunos igual ou superior a 1!')
        except ValueError:
            print('VALOR INVÁLIDO!\nA quantidade de alunos deve ser um número inteiro igual ou superior a 1!')
    return alunos

def nameValidation() -> str:
    """
    This function asks for a student's name and returns it.
    """
    name = '!'
    while not name.isalpha():
        try:
            name = input('Nome: ')
            invalidChar = set(string.punctuation)
            isInvalid = any(char.isdigit() or char in invalidChar for char in name)
            if isInvalid:
                raise ValueError
            else:
                break
        except ValueError:
            print('O nome não pode conter números ou caracteres especiais!')
    return name

def averageValidation() -> float:
    """
    This function asks for the student's final average and returns it.
    """
    while True:
        try:
            average = float(input('Média: ').replace(',','.'))
            if average <= 10 and average >= 0:
                break
            else:
                print('Informe uma média entre 0.0 e 10.0!')
        except ValueError:
            print('A média tem que ser um número inteiro ou decimal!')
    return average

def checkCondition(average: int) -> str:
    """
    This function receives the average of the student and returns its condition
    """
    if average >= 7:
        return 'aprovado(a)'
    else:
        return 'reprovado(a)'

def fillFinalExamForm(numAlunos: int) -> list:
    """
    This function asks for the names and average of the students and returns a list of student information dictionaries
    """
    turma = []
    for aluno in range(numAlunos):
        print('Escreva o nome e a média do ' + str(aluno + 1) + 'º aluno(a): ')

        name = nameValidation()
        average = averageValidation()
        condition = checkCondition(average)
                
        turma.append({
            'nome': name,
            'media': average,
            'situacao': condition
        })
    return turma

if __name__ == '__main__':
    numAlunos = classLength()
    finalExamResult = fillFinalExamForm(numAlunos)

    for aluno in finalExamResult:
        print(aluno)

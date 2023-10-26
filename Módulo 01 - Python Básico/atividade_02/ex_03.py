# Exercício 002-3: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')
if len(letra) > 1:
  print('Você digitou mais de uma letra...')
else:
  if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
    print('A letra que você digitou é uma consoante')
  else:
    print('A letra que você digitou é uma vogal')
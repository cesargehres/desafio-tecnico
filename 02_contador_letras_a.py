print('=== Contador de Letras "A" ===\n')
texto = str(input('Digite o texto:\n'))

texto = texto.upper() #coloca todas as letras em maiúsculo
quant_a = texto.count('A') #conta quantidade de letras A


if quant_a == 0:
    print('A letra "A" não aparece no texto.')

elif quant_a == 1:
    print(f'A letra "A" aparece no texto {quant_a} vez.')

else:
    print(f'A letra "A" aparece no texto {quant_a} vezes.')

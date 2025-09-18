n1 = float (input ("digite sua nota b1: "))
n2 = float (input ("digite sua nota b2: "))
media = (n1 + n2) / 2 

if media >= 7:  
    print(f'Aluno Aprovado {media}') 
else:
    print(f'Aluno Reprovado {media}')
    exame = float (input('Qual sua nota do Exame? '))

    mediafinal = media + exame
    mediafinal = min(mediafinal, 10)

    if mediafinal >= 10:
        print(f'Média + Exame APROVADO {mediafinal}')
    else:
        print (f'Média + Exame REPROVADO {mediafinal}')










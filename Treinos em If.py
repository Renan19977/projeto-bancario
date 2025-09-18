maior_idade = 18
idade_especial = 17

idade = int (input('Digite sua Idade: '))

if idade >= maior_idade:
    print ('Você pode tirar CNH')
elif idade == idade_especial: 
    print ('Voce ja pode ir antecipando suas aulas teoricas')
else:
    print ('Ainda não atinguiu a maioridade!')
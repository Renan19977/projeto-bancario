opcao = -1

while opcao != 0:
    opcao = int(input('[1] sacar\n[2] Extrato\n[0] Sair:'))
    
    if opcao == 1:
        print('sacando...')
    elif opcao == 2:
        print ('Extrato')
    elif opcao == 1 or 2:
        print ('Opcão invalida!')
else:
    print ('Obrigado')
    
  
        
    for numero in range (100):
        
       if numero % 2 ==1 :
           continue
        
       print(numero, end=" ")
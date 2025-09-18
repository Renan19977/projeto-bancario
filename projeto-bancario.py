menu = """

[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0 
limite_saques = 3


while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("Deposito")
        valor = float(input("Digite um valor: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print ("Deposito realizado com sucesso!")
        else:
            print ("Valor Invalido")
        
        
        
        
        
        
    elif opcao == "2":
        print("saque")
        valor_saque = float(input("Digite o Valor do saque:"))
        if valor_saque <= 0:
            print ("Operação falhou")
        elif numeros_saques >= limite_saques:
            print ("Numero maximo de saques excedido.")
        elif valor_saque > saldo:
            print ("Saldo Insufiente.")
        elif valor_saque > limite:
            print ("Valor de Limite Excedido")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque}\n"
            numeros_saques += 1
            print("Saque Realizado")
            
            
            
            
                    
        
    elif opcao == "3":
        print("Extrato")
        print ("---------EXTRATO--------")
        if not extrato:
            print("Não há transações")
        else:
            print(extrato)
            print(f"SALDO: {saldo:.2f}") 
            
            
            
            
            
    elif opcao == "0":
        break
    
    else:
        print("Operação Inválida!")
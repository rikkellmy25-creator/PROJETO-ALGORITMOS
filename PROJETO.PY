print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())

op=1

adms=[]
cliente=[]

while op!=0:
    print("MENU")
    print("01-CADASTRAR")
    print("02-LOGIN")
    print("03-SAIR")

    menu=int(input("Digite a opção desejada: "))

    if menu==1:
        print("01-ADM")
        print("02-CLIENTE")
        perm=int(input("Digite a opção desejada: "))
        if perm==1:
            usuario=input("DIGITE O SEU USUÁRIO: ")
            senha=(input("DIGITE SUA SENHA: "))
            adms.append([usuario,senha])
        elif perm==2:
            usuario=input("DIGITE O SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            cliente.append([usuario, senha])
    if menu==2:
        print("-"*50)
        print("LOGIN")
        print("01-ADM")
        print("02-CLIENTE")
        perm_login=input("DIGITE A OPÇÃO DESEJADA: ")
        if perm_login==1:
            login=True
            for i
            while perm==1:
                print("-"*50)
                ("MENU ADM")
                print("01-GERENCIAR REBANHO")
                print("02-GERENCIAR PRODUÇÃO") 
                print("03-GERENCIAR ESTOQUE")
                print("04-VALORES DOS PRODUTOS")
                print("05-GERENCIAR VALIDADE")
                print("06-REMOVER PRODUTOS")
                
            

    
            


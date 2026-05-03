print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())

op=1

adm=[]
cliente=[]
rebanho=[]
estoque=[]

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
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA: ")
            cadastrado=False
            for i in adm:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    adm.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!" )
        if perm==2:
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA: ")
            cadastrado=False
            for i in cliente:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    cliente.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!" )
    if menu==2:
        print("="*50)
        print("LOGIN")
        print("01-ADM")
        print("02-CLIENTE")
        print("="*50)
        perm_login=int(input("DIGITE A OPÇÃO DESEJADA: "))
        if perm_login==1:
            login=False
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in adm:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    login=True
            if login:
                opadm=0
                while opadm>=0:
                        print(f"SEJA BEM VINDO {usuario}!")
                        print("="*30)
                        print("MENU ADM")
                        print("01-GERENCIAR REBANHO")
                        print("02-GERENCIAR PRODUÇÃO") 
                        print("03-GERENCIAR ESTOQUE")
                        print("04-VALORES DOS PRODUTOS")
                        print("05-GERENCIAR VALIDADE")
                        print("06-REMOVER PRODUTOS")

                        menuadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        if menuadm==1:
                            print("="*30)
                            print("01-ADICIONAR ANIMAL")
                            print("02-REMOVER ANIMAL")
                            print("03-EDITAR ANIMAL")
                            print("04-LISTAR ANIMAIS DO REBANHO")
                            print("05-SAIR")
                            opadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if opadm==1:
                                print("ADICIONAR ANIMAL")
                                id_animal= len(rebanho)+1
                                tipo=input("TIPO DO ANIMAL:").upper()
                                peso=input("PESO DO ANIMAL(KG):").upper()
                                gestaçao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
                                rebanho.append({"IDENTIFICAÇÃO DO ANIMAL":id_animal,"TIPO:":tipo,"PESO(KG)":peso,"GESTAÇÃO:":gestaçao})
                                print(F"ANIMAL ADICIONADO COM SUCESSO!")
                                print(f"ID:{id_animal}, TIPO:{tipo}, PESO:{peso},GESTANTE:{gestaçao}")
                            elif opadm==2:
                                print("REMOVER REBANHO")
                                print(rebanho)
                                print("R")
                                existe=False
                                remv=int((input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO:")))
                                for i in rebanho:
                                       if i["IDENTIFICAÇÃO DO ANIMAL"]==remv:
                                            rebanho.remove(i)
                                            existe=True
                                            
                                if not existe:
                                     print("ANIMAL NÃO ENCONTRADO!")
                            elif opadm==3:
                                print("="*30)
                                print("EDITAR ANIMAL")
                                print(rebanho)
                                id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR:"))
                                for i in rebanho:
                                     
                                     if i["IDENTIFICAÇÃO DO ANIMAL"]==id_atualizar:
                                          i["PESO(KG)"]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
                                          i["GESTAÇÃO"]=(input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): "))
                                          print(F"ATUALIZAÇÃO BEM SUCEDIDADE{rebanho}")
                            elif opadm==4:
                                 print("="*30)
                                 print("RELATORIO DO REBANHO")
                                 print("EXISTEM",len(rebanho),"ANIMAIS NO REBANHO")
                                                                     
                            
                            
                                       

                            
                            

                            





            if not login:
                    print("USUARIO OU SENHA INVALIDO! ")
            
                
            

    
            


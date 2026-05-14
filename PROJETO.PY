print("-"*50)
print("Sistema de Gestão Agropecuária (Fazenda Sertão)".upper())

op=1

adm=[]
cliente=[]
rebanho=[]
estoqueadm=[]
estoquecliente=[]
financeiro=[]
vacina=[]
retiradas=[]
carac_especiais= "!@#$%&*()-_=+[]{}|;:,.<>?/"

while op!=0:
    print("="*15, "MENU" ,"="*15)
    print("01-CADASTRAR")
    print("02-LOGIN")
    print("="*36)
    print()
    menu=int(input("Digite a opção desejada: "))
    print()

    if menu==1:
        print("="*15, "MENU", "="*15)
        print("01-ADM")
        print("02-CLIENTE")
        print("03-VOLTAR")
        print("="*36)
        print()
        cadastrar=int(input("Digite a opção desejada: "))
        print()
        if cadastrar==1:
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
            cadastrado=False
            maiuscula_user=False
            maiuscula_senha=False
            senha_espec=False
            user_espec=False
            for i in usuario:
                 if i.isupper():
                      maiuscula_user=True
                 continue
            if len(usuario)<5:
                 print()
                 print("USUARIO INVALIDO, MÍNIMO 5 DÍGITOS")
                 print()
                 continue
            for i in senha:
                if i.isupper():
                      maiuscula_senha=True
                if i in carac_especiais:
                     senha_espec=True
            if len(senha)<8 or not maiuscula_senha or not senha_espec:
                 print()
                 print("SENHA INVALIDA!!")
                 print()
                 continue
                     
            
            for i in adm:
                if i[0]==usuario and i[1] == senha:
                    print()
                    print("USUARIO JÁ CADASTRADO")
                    print()
                    cadastrado=True
                    continue
            if not cadastrado:
                    adm.append([usuario,senha])
                    print()
                    print("USUARIO CADASTRADO COM SUCESSO!" )
                    print()
        elif cadastrar==2:
            print()
            usuario=input("DIGITE O USUARIO: ")
            senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
            print()
            cadastrado=False
            maiuscula_user=False
            maiuscula_senha=False
            senha_espec=False
            user_espec=False
            for i in usuario:
                 if i.isupper():
                      maiuscula_user=True
                 continue
            if len(usuario)<5:
                 print()
                 print("USUARIO INVALIDO, MÍNIMO 5 DÍGITOS")
                 print()
                 continue
            for i in senha:
                if i.isupper():
                      maiuscula_senha=True
                if i in carac_especiais:
                     senha_espec=True
            if len(senha)<8 or not maiuscula_senha or not senha_espec:
                 print("SENHA INVALIDA")
                 continue
            for i in cliente:
                if i[0]==usuario and i[1] == senha:
                    print("USUARIO JÁ CADASTRADO")
                    cadastrado=True
                    continue
            if not cadastrado:
                    cliente.append([usuario,senha])
                    print("USUARIO CADASTRADO COM SUCESSO!") 
        elif cadastrar==3:
             continue
            
    if menu==2:
        print("="*30)
        print("LOGIN")
        print("="*30)
        print("01-ADM")
        print("02-CLIENTE")
        print("03-VOLTAR")
        print("="*30)
        perm_login=int(input("DIGITE A OPÇÃO DESEJADA: "))
        if perm_login==3:
            continue
        elif perm_login==1:
            loginadm=False
            loginusuario=False
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in adm:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    loginadm=True
        if perm_login==2:
            loginusuario=False
            loginadm=False
            usuario=input("DIGITE SEU USUÁRIO: ")
            senha=input("DIGITE SUA SENHA: ")
            for i in cliente:
                if i[0]==usuario and i[1]==senha:
                    print("LOGIN REALIZADO COM SUCESSO! ")
                    loginusuario=True
        if loginadm==True:
                opadm=0
                while opadm>=0:
                        print()
                        print(f"SEJA BEM VINDO {usuario}!")
                        print("="*30)
                        print("MENU ADM")
                        print("01-GERENCIAR REBANHO")
                        print("02-GERENCIAR PRODUÇÃO/ESTOQUE") 
                        print("03-FINANCEIRO")
                        print("04-RETIRADAS")
                        print("05-RELATÓRIOS")
                        print("05-SAIR")
                        print()
                        menuadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                        print()
                        if menuadm==5:
                            break
                        elif menuadm==1: #opção 1 do menu
                            print("="*30)
                            print("01-ADICIONAR ANIMAL")
                            print("02-REMOVER ANIMAL")
                            print("03-EDITAR ANIMAL")
                            print("04-LISTAR ANIMAIS DO REBANHO")
                            print("05-VACINAS")
                            print("06-VOLTAR")
                            print()
                            opadm=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            print()
                            if opadm==1:
                                print("ADICIONAR ANIMAL")
                                id_animal= len(rebanho)+1
                                tipo=input("TIPO DO ANIMAL:").upper()
                                peso=input("PESO DO ANIMAL(KG):")
                                gestaçao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
                                rebanho.append([id_animal,tipo,peso,gestaçao])
                                print()
                                print(F"ANIMAL ADICIONADO COM SUCESSO!")
                                print(f"ID:{id_animal}, TIPO:{tipo}, PESO:{peso},GESTANTE:{gestaçao}")
                                print()
                            elif opadm==2:
                                print("REMOVER REBANHO")
                                print(rebanho)
                                existe=False
                                print()
                                remv=int((input("QUAL ANIMAL VOCÊ QUER REMOVER? DIGITE O NÚMERO DE INDENTIFICAÇÃO:")))
                                print()
                                for i in rebanho:
                                       if i[0]==remv:
                                            rebanho.remove(i)
                                            existe=True
                                            print()
                                            print("ANIMAL REMOVIDO COM SUCESSO!")
                                            print()
                                            
                                if not existe:
                                     print()
                                     print("ANIMAL NÃO ENCONTRADO!")
                                     print()
                            elif opadm==3:
                                print("="*30)
                                print("EDITAR ANIMAL")
                                print(rebanho)
                                print()
                                id_atualizar=int(input("DIGITE QUAL A IDENTIFICAÇÃO DO ANIMAL QUE VOCÊ QUER ATUALIZAR:"))
                                print()
                                for i in rebanho:
                                     if i[0]==id_atualizar:
                                          i[2]=int(input("DIGITE O PESO ATUALIZADO DO ANIMAL: "))
                                          i[3]=(input("DIGITE SE AINDA ESTÁ PRENHA O ANIMAL (SIM) OU (NÃO): "))
                                          print(F"ATUALIZAÇÃO BEM SUCEDIDADE{rebanho}")
                            elif opadm==4:
                                 print()
                                 print("="*30)
                                 print("RELATORIO DO REBANHO")
                                 print("EXISTEM",len(rebanho),"ANIMAIS NO REBANHO")
                                 print()
                            elif opadm==5:
                                print()
                                print("="*10,"VACINAS","="*10)
                                print("01-REGISTRAR VACINA")
                                print("02-PROXIMAS VACINAS")
                                print("03-LISTAR VACINAS")
                                print("04-Voltar")
                                print()
                                op_vacinas=int(input("DIGITE A OPÇÃO DESEJADA: "))
                                print()
                                if op_vacinas==1:
                                    print("VACINAS")
                                    print(rebanho)
                                    reg_vacinas=int(input("DIGITE O ID DO ANIMAL PARA REGISTRAR A VACINA:"))
                                    for i in rebanho:
                                        if i[1]==reg_vacinas:
                                            id_animal=i[1]
                                            animal=input("DIGITE O TIPO DO ANIMAL:")
                                            vacina_nome=input("DIGITE O NOME DA VACINA:")
                                            data=input("DIGITE A DATA DA VACINA(AA/MM/YY): ")
                                            prox_vacina=input("DIGITE A DATA DA PROXIMA VACINA(AA/MM/YY):")
                                        vacina.append([id_animal,animal, vacina_nome, data, prox_vacina])
                                        print(({"ID",id_animal,"ANIMAL:",animal,"VACINA:",vacina_nome,"DATA",data,"PROXIMAS VACINAS:",prox_vacina}))
                                elif op_vacinas==2:
                                    print("PROXIMAS VACINAS A SEREM APLICADAS")
                                    print()
                                    for i in vacina:
                                        if i[4]:
                                            print(F"AS PROXÍMAS VACINAS SÃO{i}")
                                elif op_vacinas==3:
                                    print("VACINAS JÁ APLICADAS")
                                    for i in vacina:
                                         if i[2]:
                                              print(i[1])
                                              print(i[2])
                                              print(i[3])
                                              print(i[4])
                                elif op_vacinas==4:
                                     continue
                            elif opadm==6:
                                 continue
                        elif menuadm==2:
                                print("="*15,"GESTÃO PRODUÇÃO", "="*15)
                                print("01-ADICIONAR AO ESTOQUE")
                                print("02-REMOVER DO ESTOQUE")
                                print("03-ATUALIZAR QUANTIDADE DE ITENS")
                                print("04-LISTAR ESTOQUE")
                                print("05-ADICIONAR PRODUÇÃO DIÁRIA")
                                print("05-VOLTAR")
                                print()
                                opadm=int(input("DIGITE A OPÇÃO DESEJADA:"))
                                print()
                                if opadm==1:
                                    id_produto=len(estoqueadm)+1
                                    produto=input("DIGITE O PRODUTO A SER ADICIONADO:  ")
                                    quantidade=int(input("DIGITE A QUANTIDADE DE ITENS: "))
                                    peso=int(input("DIGITE O PESO(KG): "))
                                    valor=int(input("DIGITE O VALOR DO PRODUTO(R$): "))
                                    validade=(input("DIGITE A VALIDADE DO PRODUTO(AA/MM/YY): "))
                                    estoqueadm.append({"ID":id_produto, "PRODUTO:":produto, "QUANTIDADE:":quantidade,"PESO(KG):":peso,"VALOR(R$):":valor,"VALIDADE(AA/MM/YY):":validade})
                                    print("Produto adicionado com sucesso:",{"ID":id_produto, "PRODUTO:":produto, "QUANTIDADE:":quantidade,"PESO(KG):":peso,"VALOR(R$):":valor,"VALIDADE(AA/MM/YY):":validade})
                                elif opadm==2:
                                    print("="*15,"REMOÇÃO DE PRODUTO","="*15)
                                    print(estoqueadm)
                                    existe=False
                                    remv_produto=int(input("DIGITE O PRODUTO QUE VOCÊ QUER REMOVER(ID):"))
                                    for i in estoqueadm:
                                        if i["ID"]==remv_produto:
                                            estoqueadm.remove(i)
                                            print("PRODUTO REMOVIDO COM SUCESSO!")
                                            existe=True
                                        if not existe:
                                            print("PRODUTO NÃO ENCONTRADO!")
                                elif opadm==3:
                                     print("="*15,"ATUALIZAR PRODUTO", "="*15)
                                     print(estoqueadm)
                                     update_estoque=int(input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR(ID): "))
                                     for i in estoqueadm:
                                        if i["ID"]==update_estoque:
                                             i["ID"]=int(input("DIGITE O ID ATUALIZADO: "))
                                             i["PRODUTO"]=input("DIGITE QUAL O PRODUTO VOCÊ QUER ATUALIZAR:")
                                             i["QUANTIDADE"]=int(input("DIGITE A QUANTIDADE ATUALIZADA DO PRODUTO: "))
                                             i["PESO"]=int(input("DIGITE O PESO DO PRODUTO ATUALIZADO(KG): "))
                                             i["VALOR"]=int(input("DIGITE O VALOR DO PRODUTO ATUALIZADO(R$): "))
                                             i["VALIDADE"]=input("DIGITE A VALIDADE ATUALIZADA DO PRODUTO(AA/MM/YY):")
                                elif opadm==4:
                                     print("="*15,"ESTOQUE","="*15)
                                     print(("O ESTOQUE ATUAL É:",{F"ID":id_produto, f"PRODUTO:":produto, f"QUANTIDADE:":quantidade,f"PESO:":peso,f"VALOR:":valor}))
                                elif opadm==5:
                                     print("="*10,"PRODUÇÃO DIÁRIA",)
                                     prod_diaria=input("DIGITE O ID DO PRODUTO PRODUZIDO:")
                                     print(estoqueadm)
                                     for i in estoqueadm:
                                          if i["ID"]==prod_diaria:
                                            i["QUANTIDADE"]=int(input(f"QUAL FOI A PRODUÇÃO DIÁRIA DO {produto}? "))
                                for i in estoqueadm:
                                    if i["QUANTIDADE"]<5:
                                        print(f"ALERTA!!!!!! O {i["PRODUTO"]} ESTÁ COM ESTOQUE BAIXO!")
                        elif menuadm==3:
                                print("MENU FINANCEIRO")
                                print("01-REGISTRAR ENTRADA")
                                print("02-REGISTRAR SAIDA")
                                print("03-VER SALDO")
                                print("04-FILTRAR POR TIPO(ENTRADA/SAIDA)")
                                print("05-VER TOTAL DE ENTRADAS")
                                print("06-VER TOTAL DE SAIDAS")
                                print("07-VOLTAR")
                                op_fin=int(input("DIGITE A OPÇÃO DESEJADA: "))

                                if op_fin==1:
                                    print("REGISTRAR ENTRADA")
                                    valor=int(input("VALOR(R$):"))
                                    desc=input("DESCRIÇÃO:")
                                    tipo="ENTRADA"
                                    financeiro.append({"VALOR:":valor,"DESCRIÇÃO:":desc,"ENTRADA:":tipo})
                                    print(F"VALOR:{valor}",f"DESCRIÇÃO:{desc}", "ADICIONADOS COM SUCESSO")
                                elif op_fin==2:
                                    print("REGISTRAR SAIDA")
                                    valor=int(input("VALOR(R$):"))
                                    desc=input("DESCRIÇÃO:")
                                    tipo="SAIDA"
                                    financeiro.append({"VALOR:":valor,"DESCRIÇÃO:":desc,"SAIDA":tipo})
                                    print(F"VALOR:{valor}",f"DESCRIÇÃO:{desc}", "ADICIONADOS COM SUCESSO")
                                elif op_fin==3:
                                    print("SALDO")
                                    saldo=0
                                    for item in financeiro:
                                        if item["ENTRADA"]:
                                            saldo+=valor["ENTRADA"]
                                        elif item["SAIDA"]=="SAIDA":
                                            saldo-=valor["SAIDA"]
                                    print(F"O SALDO ATUAL É {saldo}")
                                if op_fin==4:
                                    print("FILTRO POR TIPO(ENTRADA/SAIDA)")
                                    tipo=input("DIGITE QUAL O FILTRO(ENTRADA/SAIDA): ")

                                    for i in financeiro:
                                        if i["tipo"]==tipo:
                                            print(tipo)
                                if op_fin==5:
                                    total=0
                                    for i in financeiro:
                                        if i["tipo"]=="entrada":
                                            total+=i["valor"]
                                    print("TOTAL DE ENTRADAS:", total)
                                if op_fin==6:
                                    total=0
                                    for i in financeiro:
                                        if i["tipo"]=="saida":
                                            total+=i["valor"]
                                    print("TOTAL DE SAIDAS:", total)
                                if op_fin==7:
                                    continue
                        elif menuadm==4:
                            print("=====RETIRADAS=====")
                            print("01-AGENDAR RETIRADA")
                            print("02-CONFIRMAR RETIRADA")
                            print("03-RETIRADAS PENDENTES")
                            print("04-RETIRADAS FEITAS")
                            print("05-VOLTAR")
                            op_retirada=int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if op_retirada==1:
                                data=input("DIGITE A DATA DA RETIRADA(AA/MM/YY): ")
                                tipo_retirada=input("DIGITE O TIPO DA RETIRADA(ANIMAL/PRODUTO): ")
                                hora=input("DIGITE A HORA DA RETIRADA(HH:MM:SS):")
                                id_retirada=int(input("DIGITE O ID DO PRODUTO/ANIMAL À SER EFETUADO A RETIRADA:"))
                                status="PENDENTE"
                                retiradas.append({"DATA:":data,"TIPO:":tipo_retirada,"HORA:":hora, "ID":id_retirada,"STATUS":status})
                                print(F"RETIRADA AGENDADA COM SUCESSO PARA {data}, às {hora}")
                            elif op_retirada==2:
                                if retiradas(len<0):
                                    print("NENHUMA RETIRADA AGENDADA")
                                elif retiradas(len>=1):
                                    for i in retiradas:
                                        i["STATUS"]=="pendente"
                                        print(f"ID:{i["ID:"]}| TIPO:{i["TIPO:"]}|HORA:{i["HORA:"]}|DATA:{i["DATA:"]}")
                                id_confretirada=int(input("DIGITE O ID DA RETIRADA A SER CONFIRMADA:"))
                                existe=False
                                for i in retiradas:
                                    if i["ID"]==id_confretirada:
                                        i["STATUS"]=="CONCLUIDA"
                                        print("RETIRADA FEITA COM SUCESSO!")
                                        existe=True
                                        break
                                    if not existe:
                                        print("RETIRADA NÃO ENCONTRADA!")
                                        continue
                            elif op_retirada==3:
                                pendente=[]
                                for i in retiradas:
                                    if i["STATUS"]=="PENDENTE":
                                        pendente.append(i)
                                    print(f"AS RETIRADAS PENDENTE SÃO {pendente}")
                            elif op_retirada==4:
                                concluidas=[]
                                for i in retiradas:
                                    if i["STATUS:"]=="CONCLUIDA":
                                        concluidas.append(i)
                                        print("-"*30)
                                        print(f"AS RETIRADAS CONCLUIDAS SÃO {concluidas}")
                                        print("-"*30)
                            elif op_retirada==5:
                                continue

                        elif menuadm==5:
                            print("-"*30)
                            print("RELATORIOS")
                            print("-"*30)
                            print("01-RELATÓRIO REBANHO")
                            print("02-RELATÓRIO DO ESTOQUE")
                            print("03-RELATÓRIO FINANCEIRO")
                            print("04-RELÁTORIO RETIRADAS")
                            print("05-RELATÓRIOS VACINAS")
                            print("06-VOLTAR")
                            print("-"*30)
                            op_relatorio=int(input("DIGITE A OPÇÃO DESEJADA:"))
                            if op_relatorio==1:
                                print("-"*30)
                                print("RELATÓRIO REBANHO")
                                print("-"*30)
                                print(f"O TOTAL DE ANIMAIS É:{len(rebanho)}")
                                for i in rebanho:
                                    print(i)
                            elif op_relatorio==2:
                                print("-"*30)
                                print("RELATÓRIO ESTOQUE")
                                print("-"*30)
                                print(f"O TOTAL DE ANIMAIS É:{len(estoqueadm)}")
                                for i in estoqueadm:
                                    print(i)
                            elif op_relatorio==3:
                                print("-"*30)
                                print("RELATÓRIO FINANCEIRO")
                                print("-"*30)
                                total_saida=0
                                total_entrada=0
                                for i in financeiro:
                                    if i["ENTRADA"]:
                                        total_saida+=i["VALOR"]
                                    if i["SAIDA"]:
                                        total_saida+=i["VALOR"]
                                saldo=(total_entrada-total_saida)
                                print(F"TOTAL DE ENTRADAS: {total_entrada}")
                                print(f"TOTAL DE SAIDAS: {total_saida}")
                                print(F"O SALDO ATUAL É: {saldo}")
                            elif op_relatorio==4:
                                print("-"*30)
                                print("RELATÓRIO DE RETIRADA")
                                print("-"*30)

                                pendente=[]
                                for i in retiradas:
                                    if i["STATUS"]=="PENDENTE":
                                        pendente.append(i)
                                    print(f"AS RETIRADAS PENDENTE SÃO {pendente}")
                                concluidas=[]
                                for i in retiradas:
                                    if i["STATUS:"]=="CONCLUIDA":
                                        concluidas.append(i)
                                        print("-"*30)
                                        print(f"AS RETIRADAS CONCLUIDAS SÃO {concluidas}")
                                        print("-"*30)
                                print(F"RETIRADAS CONCLUIDAS: {len(concluidas)}")
                                print(F"RETIRADAS PENDENTES: {len(pendente)}")
                            elif op_relatorio==5:
                                print("-"*30)
                                print("RELATÓRIO VACINA")
                                print("-"*30)
                                print(f"O TOTAL DE VACINAS APLICADAS É:{len(vacina)}")
                                for i in vacina:
                                    print(i)
                            elif op_relatorio==6:
                                continue

        elif loginusuario==True:
                op_user=0
                while op_user>=0:
                    print("="*30)
                    print(F"SEJA BEM VINDO {usuario}")
                    print("="*30)
                    print("MENU")
                    print("01-EFETUAR COMPRA")
                    print("02-AGENDAR RETIRADA")
                    print()

                    menu_user=int(input("DIGITE A OPÇÃO DESEJADA: "))                    
                    continue
                                 
                                 

                            #TENHO QUE FAZER AGENDAMENTO DE RETIRADA, o menu do cliente, e ainda da uma melhorada na parte de relatorio


                                     
                                          



                                     
                                        

                                


                                      


                                      
                                                                     
                            
                            
                                       

                            
                            

                            





        elif not loginadm:
                print("USUARIO OU SENHA INVALIDO! ")
                continue
        elif not loginusuario:
                print("USUARIO OU SENHA INVALIDO! ")
                continue

            
                
            

    
            


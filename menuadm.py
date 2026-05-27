def adicionaranimal(rebanho):
    print("ADICIONAR ANIMAL")
    id_animal= len(rebanho)+1
    tipo=input("TIPO DO ANIMAL:").upper()
    peso=int(input("PESO DO ANIMAL(KG):"))
    gestaçao=input("O ANIMAL É GESTANTE? (SIM) OU (NÃO)").upper()
    valor=int(input("QUAL O VALOR? (R$) "))
    quantidade=int(input("QUAL A QUANTIDADE DE ANIMAIS? "))
    rebanho.append({"ID": id_animal, "TIPO": tipo, "PESO": peso, "GESTAÇÃO": gestaçao, "VALOR": valor, "QUANTIDADE": quantidade})
    print()
    print(F"ANIMAL ADICIONADO COM SUCESSO!")
    print(f"ID:{id_animal}, TIPO:{tipo}, PESO:{peso},GESTANTE:{gestaçao}, VALOR:{valor}, QUANTIDADE:{quantidade}")
    print()
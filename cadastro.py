def cadastro_adm(adm):
    usuario=input("DIGITE O USUARIO: ")
    senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
    cadastrado=False      
    for i in adm:
        if i.get("usuario") == usuario:
            print("USUARIO JÁ CADASTRADO")
            print()
            cadastrado=True
            return
    if not cadastrado:
        adm.append({"usuario": usuario, "senha": senha})
        print()
        print("USUARIO CADASTRADO COM SUCESSO!" )
        print()
        return adm

def cadastro_cliente(cliente):
    usuario=input("DIGITE O USUARIO: ")
    senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
    cadastrado=False      
    for i in cliente:
        if i.get("usuario") == usuario:
            print("USUARIO JÁ CADASTRADO")
            print()
            cadastrado=True
            return
    if not cadastrado:
        cliente.append({"usuario": usuario, "senha": senha})
        print()
        print("USUARIO CADASTRADO COM SUCESSO!" )
        print()
        return clientea
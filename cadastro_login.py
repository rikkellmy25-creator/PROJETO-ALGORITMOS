def cadastro(adm):
    usuario=input("DIGITE O USUARIO: ").upper()
    senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
    cadastrado=False      
    for i in adm:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            print("USUARIO JÁ CADASTRADO")
            print()
            cadastrado=True
            continue
    if not cadastrado:
        adm.append({"usuario": usuario, "senha": senha})
        print()
        print("USUARIO CADASTRADO COM SUCESSO!" )
        print()
        return adm

def cadastro(cliente):
    usuario=input("DIGITE O USUARIO: ").upper()
    senha= input("DIGITE A SUA SENHA(8 DÍGITOS, 1 LETRA MAISCULA E 01 CARACTERE ESPECIAL): ")
    cadastrado=False      
    for i in cliente:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            print("USUARIO JÁ CADASTRADO")
            print()
            cadastrado=True
            continue
    if not cadastrado:
        cliente.append({"usuario": usuario, "senha": senha})
        print()
        print("USUARIO CADASTRADO COM SUCESSO!" )
        print()
        return cliente

def login(adm):
    usuario=input("DIGITE SEU USUÁRIO: ")
    senha=input("DIGITE SUA SENHA: ")
    for i in adm:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            print("LOGIN REALIZADO COM SUCESSO! ")
            loginadm=True
    if not loginadm:
        print("USUÁRIO OU SENHA INCORRETOS! TENTE NOVAMENTE.")


def login(cliente):
    usuario=input("DIGITE SEU USUÁRIO: ")
    senha=input("DIGITE SUA SENHA: ")
    logincliente=False
    for i in cliente:
        if i.get("usuario") == usuario and i.get("senha") == senha:
            print("LOGIN REALIZADO COM SUCESSO! ")
            logincliente=True
    if not logincliente:
        print("USUÁRIO OU SENHA INCORRETOS! TENTE NOVAMENTE.")
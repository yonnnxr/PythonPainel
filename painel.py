while True:
    contn = "Carlos"
    senhan = 1234
    usuario = 'Carlos'
    Senha = 1234
    print("Deseja Entrar ou Criar Uma conta?")
    print("1. Entrar")
    print("2. Criar conta")
    info = int(input("Qual a opção desejada? "))
    if info == 2:
        contn = str(input("Insira o usuario novo: "))
        senhan = int(input("Insira a senha nova: "))
    if info == 1:
        usuario = contn
        Senha = senhan
        usu = str(input("Informe o usuario: "))
        senha1 = int(input("informe a senha: "))
        if usu == usuario and senha1 == Senha:
            while True:
                print(" ")
                print(f"Bem vindo, {usu}")
                print("O que deseja fazer hoje?")
                print("1. Calcular porcentagem")
                print("2. Calcular raiz quadrada")
                print("3. Inverter string")
                print("4. Redefinir sua senha")
                print("5. Redefinir seu usuario")
                print("6. Sair")
                opc = int(input("Digite o numero da opção desejada: "))
                if opc == 1:
                    a = int(input("Digite o numero: "))
                    b = int(input("Insira quantos porcento dele quer saber: "))
                    tot = (a * b) / 100
                    print(tot)
                if opc == 2:
                    c = int(input("Digite o numero: "))
                    tot = c ** 0.5
                    print(tot)
                if opc == 3:
                    frase = str(input('Insira a Frase: '))
                    tamanho = len(frase)
                    for i in range(1, tamanho + 1):
                        fraseinv = frase[-i]
                        print(fraseinv, end='')
                if opc == 4:
                    i = int(input("Digite a antiga senha: "))
                    if i == Senha:
                        senha1 = int(input("insira a nova senha: "))
                        Senha = senha1
                    else:
                        print("tente novamente mais tarde")
                if opc == 5:
                    joo = str(input("Digite o antigo usuario: "))
                    if joo == usuario:
                        senha1 = str(input("insira o novo usuario: "))
                        usuario = senha1
                    else:
                        print("tente novamente mais tarde")
                if opc == 6:
                    print("Obrigado")



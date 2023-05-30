from os import system
from getpass import getpass


system('cls')

def menu():
    print("Bem vindo")
    print("Escolha uma opção")
    print("[1] Cadastrar um usuario")
    print("[2] Fazer Login")
    print("[Qualquer outra tecla.] Sair do aplicativo")
    opcoes = int(input("Opção selecionada: "))
    return(opcoes)

def _login():
    login = input("usuario: ")
    senha = getpass(prompt='Senha: ')
    return(login, senha)

def b_usuario(Login, senha):
    usuario1 = []  
    try: 
        with open('usuarios.txt', 'r+',) as aqui:
            for line in aqui:
                line = line.strip(',')
                usuario1.append(line.split())
            for usuario1 in usuario1:
                nome = usuario1[0]
                password = usuario1[1]           
                if login == nome and password == senha:
                    return True
    except FileNotFoundError:
        return False
    
while(True):
    estrutura = menu()
    system('cls')
    if estrutura == 1:
        login, senha = _login()
        if login == senha:
            print("Seu login não pode ser igual a senha.") 
        user = b_usuario(login, senha)
        if user == True:
            print("O usuario já existe!!!!")
        else: 
            with open('usuarios.txt', 'a+',) as aqui:
                aqui.writelines(f'{login} {senha}\n')  
            print("Cadastro concluido")
            exit
    elif estrutura == 2:
        login, senha = _login()
        user = b_usuario(login, senha)
        if user == True:
            print("Login realizado com successo")
            exit
        else:
            print("usuario ou senha errado!!")
    else:
        print("Ty, for use")
        break
     


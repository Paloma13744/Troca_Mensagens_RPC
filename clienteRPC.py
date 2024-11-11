import rpyc

conn = rpyc.connect("localhost", 18861)
proxy = conn.root

def ingressar_no_sistema(nome):
    return proxy.ingressar_no_sistema(nome)

def entrar_na_sala(identificacao):
    return proxy.entrar_na_sala(identificacao)

def sair_da_sala(identificacao):
    return proxy.sair_da_sala(identificacao)

def enviar_mensagem_publica(mensagem):
    return proxy.enviar_mensagem_publica(mensagem)

def listar_mensagens_publicas():
    return proxy.listar_mensagens_publicas()

def enviar_mensagem_privada(identificacao_remetente, identificacao_destinatario, mensagem):
    return proxy.enviar_mensagem_privada(identificacao_remetente, identificacao_destinatario, mensagem)

def listar_mensagens_privadas(identificacao):
    return proxy.listar_mensagens_privadas(identificacao)

def listar_usuarios():
    return proxy.listar_usuarios()

def menu_principal(identificacao):
    while True:
        print("\n ______*** Menu de Sala de bate-papo *** _______")
        print("1. Enviar Mensagem Pública")
        print("2. Mostrar Mensagens Públicas")
        print("3. Enviar Mensagem Privada")
        print("4. Mostrar Mensagens Privadas")
        print("5. Listar Usuários")
        print("6. Sair da Sala")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mensagem = input("Digite sua mensagem pública: ")
            print(enviar_mensagem_publica(mensagem))
        elif escolha == "2":
            mensagens = listar_mensagens_publicas()
            for msg in mensagens:
                print(msg)
        elif escolha == "3":
            destinatario = input("Digite a identificação do destinatário: ")
            mensagem = input("Digite sua mensagem privada: ")
            print(enviar_mensagem_privada(identificacao, destinatario, mensagem))
        elif escolha == "4":
            mensagens = listar_mensagens_privadas(identificacao)
            for msg in mensagens:
                print(msg)
        elif escolha == "5":
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif escolha == "6":
            print(sair_da_sala(identificacao))
            break
        elif escolha == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    identificacao = ingressar_no_sistema(nome)
    print(f"Sua identificação é: {identificacao}")
    print(entrar_na_sala(identificacao))
    menu_principal(identificacao)

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:18861/")

def ingressar_no_sistema(nome):
    return proxy.ingressar_no_sistema(nome)

def entrar_na_sala(identificacao):
    return proxy.entrar_na_sala(identificacao)

def sair_da_sala(identificacao):
    return proxy.sair_da_sala(identificacao)

def enviar_mensagem(identificacao, mensagem):
    return proxy.enviar_mensagem(identificacao, mensagem)

def listar_mensagens():
    return proxy.listar_mensagens()

def enviar_mensagem_usuario(identificacao_remetente, identificacao_destinatario, mensagem):
    return proxy.enviar_mensagem_usuario(identificacao_remetente, identificacao_destinatario, mensagem)

def listar_usuarios():
    return proxy.listar_usuarios()

def menu_principal(identificacao):
    while True:
        print("\n--- Menu ---")
        print("1. Enviar Mensagem")
        print("2. Listar Mensagens")
        print("3. Enviar Mensagem para Usuário")
        print("4. Listar Usuários")
        print("5. Sair da Sala")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mensagem = input("Digite sua mensagem: ")
            print(enviar_mensagem(identificacao, mensagem))
        elif escolha == "2":
            mensagens = listar_mensagens()
            for msg in mensagens:
                print(msg)
        elif escolha == "3":
            destinatario = input("Digite a identificação do destinatário: ")
            mensagem = input("Digite sua mensagem: ")
            print(enviar_mensagem_usuario(identificacao, destinatario, mensagem))
        elif escolha == "4":
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif escolha == "5":
            print(sair_da_sala(identificacao))
            break
        elif escolha == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    identificacao = ingressar_no_sistema(nome)
    print(f"Sua identificação é: {identificacao}")
    print(entrar_na_sala(identificacao))
    menu_principal(identificacao)

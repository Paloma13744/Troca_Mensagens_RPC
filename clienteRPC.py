import rpyc

class ChatClient:
    def __init__(self):
        self.conn = rpyc.connect("localhost", 18861)  # Conecta ao servidor , chama os serviços da aplicação
        self.identificacao = None
        self.sala_atual = None

    def ingressar_no_sistema(self, nome):  # Função para inciar no sistema
        self.identificacao = self.conn.root.ingressar_no_sistema(nome)
        print(f"Usuário registrado(a) como: {self.identificacao}")

    def escolher_sala(self):
        while True:
            sala = input("Escolha uma sala:(sala1, sala2 ou sala3): ")
            if sala in ["sala1", "sala2", "sala3"]:
                self.sala_atual = sala
                resultado = self.conn.root.entrar_na_sala(self.identificacao, sala)
                print(resultado)
                break
            else:
                print("Sala inválida. Escolha entre sala1, sala2 ou sala3.")

    def sair_da_sala(self): # Função para sair da sala e também do diciionário de usuários (remove)
        if self.sala_atual:
            resultado = self.conn.root.sair_da_sala(self.identificacao, self.sala_atual)
            print(resultado)
            self.sala_atual = None   
        else:
            print("Você não está em nenhuma sala.")

    def enviar_mensagem_publica(self, mensagem):
        if self.sala_atual:
            resultado = self.conn.root.enviar_mensagem_publica(self.identificacao, self.sala_atual, mensagem)
            print(resultado)
        else:
            print("Você deve escolher uma sala antes de enviar uma mensagem.")

    def listar_mensagens_publicas(self):
        if self.sala_atual:
            mensagens = self.conn.root.listar_mensagens_publicas(self.sala_atual)
            print("Mensagens Públicas:")
            for msg in mensagens:
                print(msg)
        else:
            print("Você deve escolher uma sala para ver as mensagens públicas.")

    def enviar_mensagem_privada(self, destinatario, mensagem):
        if self.sala_atual:
            resultado = self.conn.root.enviar_mensagem_privada(self.identificacao, destinatario, self.sala_atual, mensagem)
            print(f"Enviado para {destinatario} na {self.sala_atual}: {mensagem}")
            print(resultado)
        else:
            print("Você deve escolher uma sala antes de enviar uma mensagem privada.")

    def listar_mensagens_privadas(self):
        if self.sala_atual:
            mensagens = self.conn.root.listar_mensagens_privadas(self.identificacao, self.sala_atual)
            print("Mensagens Privadas:")
            for msg in mensagens:
                print(msg)
        else:
            print("Você deve escolher uma sala para ver as mensagens privadas.")

    def listar_usuarios(self):
        if self.sala_atual:
            usuarios = self.conn.root.listar_usuarios(self.sala_atual)
            print("Usuários na sala:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("Você deve escolher uma sala para ver os usuários.")
            
            
    def listar_identificacoes_usuarios(self):
        """Lista as identificações dos usuários na sala atual."""
        if self.sala_atual:
            identificacoes = self.conn.root.listar_identificacoes_usuarios(self.sala_atual)
            print("Identificações dos usuários na sala:")
            for id in identificacoes:
                print(id)
        else:
            print("Você deve escolher uma sala para ver as identificações dos usuários.")


    def menu(self): # Função para inciar o menu
        nome = input("Digite seu nome: ")
        self.ingressar_no_sistema(nome)
        self.escolher_sala()

        while True:
            print("\nMenu:")
            print("1 - Enviar mensagem pública")
            print("2 - Mostrar mensagens públicas")
            print("3 - Enviar mensagem privada")
            print("4 - Mostrar mensagens privadas")
            print("5 - Mostrar usuários na sala")
            print("6 - Sair ")
            opcao = input("Escolha uma opção:")

            if opcao == "1":
                mensagem = input("Digite a mensagem: ")
                self.enviar_mensagem_publica(mensagem)  # -> Envia mensagem publicamente para todos os que estão na mesma sala
            elif opcao == "2":
                self.listar_mensagens_publicas()  # -> Mostra todas as mensagens dos usuários que estão na mesma sala
            elif opcao == "3": 
                self.listar_identificacoes_usuarios()  
                destinatario = input("Digite o identificador do destinatário: ")
                mensagem = input("Digite a mensagem: ")
                self.enviar_mensagem_privada(destinatario, mensagem)  # -> Envia mensagem para um usuário específico (na mesma sala)
            elif opcao == "4":
                self.listar_mensagens_privadas()  # -> Mostra as mensagens para um usuário específico (na mesma sala)
            elif opcao == "5":
                self.listar_usuarios()    # -> Lista os usuários que estão na mesma sala
            elif opcao == "6":
                self.sair_da_sala()    # -> Sai da sala e também do dicionário de usuários 
                break                 # Sai do sistema de bate-papo
            else:
                print("Opção inválida. Tente as opções: 1,2,3,4,5 ou 6")

if __name__ == "__main__":   # Inicia a main dos usuários
    cliente = ChatClient() 
    cliente.menu()

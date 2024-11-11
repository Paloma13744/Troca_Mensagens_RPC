import rpyc

class ChatClient:
    def __init__(self):
        self.conn = rpyc.connect("localhost", 18861)  # Conecta ao servidor
        self.identificacao = None
        self.sala_atual = None

    def ingressar_no_sistema(self, nome):
        self.identificacao = self.conn.root.ingressar_no_sistema(nome)
        print(f"Você foi registrado como: {self.identificacao}")

    def escolher_sala(self):
        while True:
            sala = input("Escolha uma sala (sala1, sala2, sala3): ")
            if sala in ["sala1", "sala2", "sala3"]:
                self.sala_atual = sala
                resultado = self.conn.root.entrar_na_sala(self.identificacao, sala)
                print(resultado)
                break
            else:
                print("Sala inválida. Escolha entre sala1, sala2 ou sala3.")

    def sair_da_sala(self):
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


    def menu(self):
        nome = input("Digite seu nome: ")
        self.ingressar_no_sistema(nome)
        self.escolher_sala()

        while True:
            print("\nMenu:")
            print("1 - Enviar mensagem pública")
            print("2 - Listar mensagens públicas")
            print("3 - Enviar mensagem privada")
            print("4 - Listar mensagens privadas")
            print("5 - Listar usuários na sala")
            print("6 - Sair da sala")
            print("7 - Sair do sistema")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                mensagem = input("Digite a mensagem pública: ")
                self.enviar_mensagem_publica(mensagem)
            elif opcao == "2":
                self.listar_mensagens_publicas()
            elif opcao == "3": 
                self.listar_identificacoes_usuarios()  
                destinatario = input("Digite o identificador do destinatário: ")
                mensagem = input("Digite a mensagem privada: ")
                self.enviar_mensagem_privada(destinatario, mensagem)
            elif opcao == "4":
                self.listar_mensagens_privadas()
            elif opcao == "5":
                self.listar_usuarios()
            elif opcao == "6":
                self.sair_da_sala()
                self.escolher_sala()
            elif opcao == "7":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    cliente = ChatClient()
    cliente.menu()

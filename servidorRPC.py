import xmlrpc.server
import threading

class ChatServer:
    def __init__(self):
        self.usuarios = {}
        self.mensagens = []
        self.numero_usuario = 1
        self.lock = threading.Lock()

    def ingressar_no_sistema(self, nome):
        with self.lock:
            identificacao = f"{nome}{self.numero_usuario}"
            self.usuarios[identificacao] = nome
            self.numero_usuario += 1
            print(f"Usuário registrado: {identificacao}")
            return identificacao

    def entrar_na_sala(self, identificacao):
        with self.lock:
            if identificacao in self.usuarios:
                print(f"Usuário {identificacao} entrou na sala.")
                return f"Usuário {self.usuarios[identificacao]} entrou na sala."
            print(f"Tentativa de entrada falhou. Usuário {identificacao} não encontrado.")
            return "Usuário não encontrado."

    def sair_da_sala(self, identificacao):
        with self.lock:
            if identificacao in self.usuarios:
                usuario = self.usuarios.pop(identificacao)
                print(f"Usuário {identificacao} saiu da sala.")
                return f"Usuário {usuario} saiu da sala."
            print(f"Tentativa de saída falhou. Usuário {identificacao} não encontrado.")
            return "Usuário não encontrado."

    def enviar_mensagem(self, identificacao, mensagem):
        with self.lock:
            if identificacao in self.usuarios:
                self.mensagens.append(f"{self.usuarios[identificacao]}: {mensagem}")
                return "Mensagem enviada."
            return "Usuário não encontrado."

    def listar_mensagens(self):
        with self.lock:
            return self.mensagens

    def enviar_mensagem_usuario(self, identificacao_remetente, identificacao_destinatario, mensagem):
        with self.lock:
            if identificacao_remetente in self.usuarios and identificacao_destinatario in self.usuarios:
                mensagem_privada = f"Privado de {self.usuarios[identificacao_remetente]} para {self.usuarios[identificacao_destinatario]}: {mensagem}"
                return mensagem_privada
            return "Usuário não encontrado."

    def listar_usuarios(self):
        with self.lock:
            return list(self.usuarios.values())

def run_server():
    server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 18861))
    server.register_instance(ChatServer())
    print("Servidor RPC iniciado na porta 18861...")
    server.serve_forever()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

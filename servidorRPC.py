import rpyc
from rpyc.utils.server import ThreadedServer
import threading

class ChatService(rpyc.Service):
    def __init__(self):
        self.usuarios = {}
        self.mensagens_publicas = []
        self.mensagens_privadas = []
        self.numero_usuario = 1
        self.lock = threading.Lock()

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_ingressar_no_sistema(self, nome):
        with self.lock:
            identificacao = f"{nome}{self.numero_usuario}"
            self.usuarios[identificacao] = nome
            self.numero_usuario += 1
            print(f"Usuário registrado: {identificacao}")
            return identificacao

    def exposed_entrar_na_sala(self, identificacao):
        with self.lock:
            if identificacao in self.usuarios:
                print(f"Usuário {identificacao} entrou na sala.")
                return f"Usuário {self.usuarios[identificacao]} entrou na sala."
            print(f"Tentativa de entrada falhou. Usuário {identificacao} não encontrado.")
            return "Usuário não encontrado."

    def exposed_sair_da_sala(self, identificacao):
        with self.lock:
            if identificacao in self.usuarios:
                usuario = self.usuarios.pop(identificacao)
                print(f"Usuário {identificacao} saiu da sala.")
                return f"Usuário {usuario} saiu da sala."
            print(f"Tentativa de saída falhou. Usuário {identificacao} não encontrado.")
            return "Usuário não encontrado."

    def exposed_enviar_mensagem_publica(self, mensagem): # Envia mensagem para todos publicamente
        with self.lock:
            self.mensagens_publicas.append(mensagem)
            print(f"Mensagem pública enviada: {mensagem}")
            return "Mensagem pública enviada."

    def exposed_listar_mensagens_publicas(self):  # Lista todas as mensagens do sistema
        with self.lock:
            return self.mensagens_publicas

   
    def exposed_enviar_mensagem_privada(self, identificacao_remetente, identificacao_destinatario, mensagem):
        with self.lock:
            if identificacao_remetente in self.usuarios and identificacao_destinatario in self.usuarios:
                mensagem_privada = {
                    "De": self.usuarios[identificacao_remetente],
                    "Para": self.usuarios[identificacao_destinatario],
                    "Mensagem": mensagem
                }
                self.mensagens_privadas.append(mensagem_privada)
                print(f"Mensagem privada enviada: {mensagem_privada}")
                return "Mensagem privada enviada."
            return "Usuário não encontrado."
        
    def exposed_listar_mensagens_privadas(self, identificacao_destinatario):
        with self.lock:
            # Filtrar apenas as mensagens onde o destinatário é o identificador requisitante
            mensagens_para_destinatario = [
                f"Mensagem de {msg['de']} para você: {msg['mensagem']}"
                for msg in self.mensagens_privadas
                if msg["Para"] == self.usuarios.get(identificacao_destinatario)
            ]
            return mensagens_para_destinatario


    def exposed_listar_usuarios(self):
        with self.lock:
            return list(self.usuarios.values())

    def exposed_listar_identificacoes_usuarios(self):
        with self.lock:
            return list(self.usuarios.keys())  

        

if __name__ == "__main__":
    server = ThreadedServer(ChatService(), port=18861)
    print("Servidor RPC iniciado na porta 18861...")
    server.start()
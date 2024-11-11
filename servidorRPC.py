import rpyc
from rpyc.utils.server import ThreadedServer
import threading

class ChatService(rpyc.Service):
    def __init__(self):
        # Dicionário que contém as salas de bate-papo, cada uma com seus usuários e mensagens
        self.salas = {
            "sala1": {"usuarios": {}, "mensagens_publicas": [], "mensagens_privadas": []},
            "sala2": {"usuarios": {}, "mensagens_publicas": [], "mensagens_privadas": []},
            "sala3": {"usuarios": {}, "mensagens_publicas": [], "mensagens_privadas": []}
        }
        self.numero_usuario = 1
        self.lock = threading.Lock()

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_ingressar_no_sistema(self, nome):
        with self.lock:
            identificacao = f"{nome}{self.numero_usuario}"
            self.numero_usuario += 1
            print(f"Usuário registrado: {identificacao}")
            return identificacao

    def exposed_entrar_na_sala(self, identificacao, nome_sala):
        with self.lock:
            if nome_sala in self.salas:
                self.salas[nome_sala]["usuarios"][identificacao] = identificacao
                print(f"Usuário {identificacao} entrou na {nome_sala}.")
                return f"Usuário {identificacao} entrou na {nome_sala}."
            else:
                return "Sala não encontrada."

    def exposed_sair_da_sala(self, identificacao, nome_sala):
        with self.lock:
            if nome_sala in self.salas and identificacao in self.salas[nome_sala]["usuarios"]:
                self.salas[nome_sala]["usuarios"].pop(identificacao)
                print(f"Usuário {identificacao} saiu da {nome_sala}.")
                return f"Usuário {identificacao} saiu da {nome_sala}."
            else:
                return "Sala ou usuário não encontrado."

    def exposed_enviar_mensagem_publica(self, identificacao, nome_sala, mensagem):
        with self.lock:
            if nome_sala in self.salas and identificacao in self.salas[nome_sala]["usuarios"]:
                self.salas[nome_sala]["mensagens_publicas"].append(f"{identificacao}: {mensagem}")
                print(f"Mensagem pública na {nome_sala}: {mensagem}")
                return "Mensagem pública enviada."
            else:
                return "Usuário não está na sala especificada."

    def exposed_listar_mensagens_publicas(self, nome_sala):
        with self.lock:
            if nome_sala in self.salas:
                return self.salas[nome_sala]["mensagens_publicas"]
            else:
                return "Sala não encontrada."

    def exposed_enviar_mensagem_privada(self, identificacao_remetente, identificacao_destinatario, nome_sala, mensagem):
        with self.lock:
            if (
                nome_sala in self.salas and
                identificacao_remetente in self.salas[nome_sala]["usuarios"] and
                identificacao_destinatario in self.salas[nome_sala]["usuarios"]
            ):
                mensagem_privada = {
                    "De": identificacao_remetente,
                    "Para": identificacao_destinatario,
                    "Mensagem": mensagem
                }
                self.salas[nome_sala]["mensagens_privadas"].append(mensagem_privada)
                print(f"Mensagem privada na {nome_sala}: {mensagem_privada}")
                return "Mensagem privada enviada."
            else:
                return "Usuário(s) não encontrado(s) na sala especificada."

    def exposed_listar_mensagens_privadas(self, identificacao_destinatario, nome_sala):
        with self.lock:
            if nome_sala in self.salas:
                mensagens_para_destinatario = [
                    f"Mensagem de {msg['De']} para você: {msg['Mensagem']}"
                    for msg in self.salas[nome_sala]["mensagens_privadas"]
                    if msg["Para"] == identificacao_destinatario
                ]
                return mensagens_para_destinatario
            else:
                return "Sala não encontrada."

    def exposed_listar_usuarios(self, nome_sala):
        with self.lock:
            if nome_sala in self.salas:
                return list(self.salas[nome_sala]["usuarios"].values())
            else:
                return "Sala não encontrada."
            
  
    
    def exposed_listar_identificacoes_usuarios(self, nome_sala):
            """Lista as identificações dos usuários de uma sala específica."""
            with self.lock:
                if nome_sala in self.salas:
                    return list(self.salas[nome_sala]["usuarios"].keys())
                else:
                    return "Sala não encontrada."
    

    
if __name__ == "__main__":
    server = ThreadedServer(ChatService(), port=18861)
    print("Servidor RPC iniciado na porta 18861...")
    server.start()

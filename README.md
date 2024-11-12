# Servidor de Chat RPC com Python

Este projeto é um sistema de chat básico que utiliza chamadas de procedimento remoto (RPC) para permitir que vários clientes se conectem a um servidor e participem de salas de chat. Os usuários podem enviar mensagens públicas para todos na sala ou mensagens privadas para um usuário específico. O servidor utiliza `threading` para permitir que múltiplos clientes acessem simultaneamente as salas e mensagens.

## Funcionalidades

- **Registro de usuários**: Cada usuário recebe uma identificação única no sistema para evitar confusão, mesmo que usem nomes iguais.
- **Salas de chat**: Três salas de chat (`sala1`, `sala2`, `sala3`) estão disponíveis para os usuários ingressarem e saírem.
- **Mensagens públicas**: Envie uma mensagem para todos os usuários em uma sala específica.
- **Mensagens privadas**: Envie mensagens privadas para um usuário específico dentro de uma sala.
- **Listagem de mensagens**: Permite listar mensagens públicas e privadas recebidas por um usuário específico. 
- **Listagem de usuários**: Permite listar todos os usuários presentes em uma sala específica.

## Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white) **Python**: Linguagem principal para a implementação.
- ![RPyC](https://img.shields.io/badge/RPyC-v5.0.1-blueviolet?logo=python&logoColor=white) **RPyC**: Framework para implementar RPC (chamadas de procedimento remoto) em Python.
- ![Threading](https://img.shields.io/badge/Threading-Concurrent-orange?logo=python&logoColor=white) **Threading**: Para suportar o atendimento simultâneo de múltiplos clientes no servidor.

## Pré-requisitos

- **Python 3.x** instalado.
- **RPyC** instalado. Para instalar, use o seguinte comando:

  ```bash
  pip install rpyc

## Estrutura do Código

### `ChatService`

A classe `ChatService` implementa as funções principais do servidor de chat, incluindo métodos expostos aos clientes:

- **Ingressar no sistema** (`exposed_ingressar_no_sistema`)
- **Entrar em uma sala** (`exposed_entrar_na_sala`)
- **Sair de uma sala** (`exposed_sair_da_sala`)
- **Enviar mensagem pública** (`exposed_enviar_mensagem_publica`)
- **Listar mensagens públicas** (`exposed_listar_mensagens_publicas`)
- **Enviar mensagem privada** (`exposed_enviar_mensagem_privada`)
- **Listar mensagens privadas** (`exposed_listar_mensagens_privadas`)
- **Listar usuários em uma sala** (`exposed_listar_usuarios`)

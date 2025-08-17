# 📘 MikuPy v1 – Documentação

## 1️⃣ Introdução
**MikuPy** é uma linguagem simplificada para criar bots do Discord usando Python.  
- Arquivo principal: `main.mpy`  
- Linguagem simplificada: `command <nome>:` e `reply "<mensagem>"`  
- Não é necessário escrever código completo em `discord.py`.  
- Suporte a variáveis como `{user_name}` para respostas dinâmicas.  

---

## 2️⃣ Instalação

1. Baixe os arquivos do site:  
   - `mikupy.py`  
   - `main.mpy` (exemplo)  
   - `requirements.txt`  

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Certifique-se de ter Python 3.10+ instalado.

---

## 3️⃣ Estrutura do `.mpy`

### Bot e Token

```mpy
bot "NomeDoBot" prefixo="!"
token="SEU_TOKEN_DO_BOT"
```

* `bot "<nome>"` → Nome do bot (opcional, usado só para referência).  
* `prefixo="!"` → Prefixo de comandos (opcional, padrão é `!`).  
* `token="<token>"` → Token do bot do Discord (obrigatório).  

---

### Comandos

```mpy
command ola:
    reply "Olá, mundo!"

command ping:
    reply "Pong!"

command user:
    reply "{user_name} Olá"
```

* `command <nome>:` → Cria um comando que pode ser chamado pelo prefixo.  
* `reply "<mensagem>"` → Mensagem que será enviada quando o comando for usado.  
* Variáveis suportadas:

  * `{user_name}` → Nome do usuário que executou o comando  

> Exemplo: Se o usuário `Hallow` usar `!user`, o bot responde: `Hallow Olá`.

---

## 4️⃣ Rodando o bot

### Opção 1: Passando o arquivo `.mpy` como argumento

```bash
python mikupy.py main.mpy
```

### Opção 2: Executando diretamente no diretório com `main.mpy`

```bash
python mikupy.py
```

> O script procura automaticamente por `main.mpy` no mesmo diretório.

---

## 5️⃣ Dicas e boas práticas

* Sempre use **token de bot válido** do Discord Developer Portal.  
* Não compartilhe seu token publicamente.  
* Use `{user_name}` nas respostas para mensagens personalizadas.  
* Para novos comandos, siga sempre o padrão:

```mpy
command nome:
    reply "mensagem"
```

* Prefira manter **token em linha própria**, separado do `bot` e `prefixo`.  

## ⚙️ Funcionalidades, Atualizações e Roadmap do MikuPy

- Atualmente não é necessário adicionar comentários no código `.mpy`.
- Suporte limitado a **comandos de resposta simples**; lógica condicional e estruturas de controle ainda não implementadas.
- Planejado suporte a **variáveis dinâmicas** para personalização de mensagens, por exemplo:  
  - `{user_name}` → nome do usuário  
  - `{user_mention}` → menção do usuário  
  - `{guild_name}` → nome do servidor  
  - `{channel_name}` → nome do canal  
  - `{bot_name}` → nome do bot  
  - `{member_count}` → quantidade de membros no servidor  
  - `{role_name}` → nome de uma role específica  

- Futuras implementações incluirão **estruturas de controle** como:  
  - Condicionais (`if/else`)  
  - Laços de repetição (`for`, `while`)  
  - Funções customizadas pelo usuário

- Futuramente será implementado suporte a **Slash Commands** do Discord, permitindo:  
  - Registro automático de comandos `/nome` no servidor  
  - Suporte a **argumentos e opções** para comandos  
  - Integração com variáveis dinâmicas e respostas personalizadas


## ⚠️ Aviso

Atualmente ainda estou aprendendo **Programação Orientada a Objetos (POO)**, que será usada na evolução do projeto (DSL MikuPy).  

- O código atual da versão 1 ainda não faz uso extensivo de POO.  
- Algumas implementações futuras podem mudar à medida que eu aprendo e aplico novos conceitos.  
- Portanto, esta versão deve ser vista como **experimental** e em contínuo desenvolvimento.

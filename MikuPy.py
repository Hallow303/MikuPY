import sys
import os
import re
import discord
from discord.ext import commands

# Misericodia, sem esses comentariso fica tudo mais dificil de entender
# sksksk preciso apreder a fazer comentarios melhores
# e aprende POO e discord.py ainda mais sksksks


def parse_mpy(file):
    with open(file, "r", encoding="utf-8") as f:
        code = f.read()

    # Token em linha própria
    token_match = re.search(r'token\s*=\s*"(.*)"', code)
    token = token_match.group(1).strip() if token_match else None

    # Bot name (opcional, não usado mas pode ser lido se quiser)
    bot_name_match = re.search(r'bot\s+"(.*)"', code)
    bot_name = bot_name_match.group(1).strip() if bot_name_match else "MeuBot"

    # Prefixo opcional
    prefix_match = re.search(r'prefixo\s*=\s*"(.*)"', code)
    prefix = prefix_match.group(1).strip() if prefix_match else "!"

    # Comandos
    commands_list = re.findall(r'command\s+(\w+):\s+reply\s+"(.*)"', code)

    return token, prefix, commands_list

def build_bot(token, prefix, commands_list):
    # Intents obrigatórios
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=prefix, intents=intents)

    for name, reply in commands_list:
        def make_cmd(msg):
            async def cmd(ctx):
                await ctx.send(msg.replace("{user_name}", ctx.author.name))
            return cmd
        bot.command(name=name)(make_cmd(reply))

    bot.run(token)

if __name__ == "__main__":
    # Pega arquivo .mpy automaticamente se nenhum argumento
    if len(sys.argv) < 2:
        default_file = os.path.join(os.getcwd(), "main.mpy")
        if not os.path.exists(default_file):
            print("Uso: python mikupy.py main.mpy")
            sys.exit(1)
        sys.argv.append(default_file)  # Adiciona main.mpy aos argumentos

    token, prefix, commands_list = parse_mpy(sys.argv[1])

    if not token:
        print("Token não encontrado no arquivo .mpy")
        sys.exit(1)

    print(f"Token lido: '{token}'")  # Para debug
    build_bot(token, prefix, commands_list)

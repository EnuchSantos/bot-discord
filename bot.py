import discord
import datetime
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot('!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')
    # current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif "sexo" in message.content:
        await message.channel.send(f'Precebo que o senhor {message.author.name}, mencionou a palavra "SEXO", '
                                   f'devo preparar o vinho e as camisinhas para a festa?')
    elif "beta" in message.content and "enuch" in message.content:
        await message.channel.send(f'{message.author.name}, Não chame meu mestre de beta, ou sofrerá as consequências!')
        await message.delete()

    await bot.process_commands(message)


@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = f"Olá! como você está hoje, {name}?"
    await ctx.send(response)


@bot.command(name='segredo')
async def secret(ctx):
    try:
        await ctx.author.send("Nunuch mandou dizer que comerá seu cu amanhã")
    except:
        await ctx.send("Não posso te contar o segredo! habilite receber mensagens de qualquer pessoas (Opções > privacidade)")


@bot.command(name='comandos')
async def comandos(ctx):
    await ctx.send("Comandos do bot:\n!oi\n!segredo\n!comandos")


@tasks.loop(minutes=1)
async def current_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(1093236684226826364)
    await channel.send(f"Data atual: {now}")


bot.run('MTEwMzY4NjQ2NTEzODk5OTI5Ng.GNm67b.waYEv6vH3BHrfhb21S0ZJnB6gBIiUGpqJwJR3E')

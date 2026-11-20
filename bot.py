import discord
import random 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def saludo(ctx):
    await ctx.send("Hola bienvenido a mi canal de discord!")

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

@bot.command()
async def password(ctx,num:int):
    await ctx.send(f"Tu contraseña es: {gen_pass(num)}")
@bot.command()
async def meme1(ctx):
    with open("imagenes/mm1.jpeg" , "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def suma(ctx, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"El resultado de la suma es: {resultado}")  
@bot.command()
async def botar(ctx):
    await ctx.send("Los lugares a los que puedes ir a botar tu basura son:")
    await ctx.send("1. Cerca de la calle 12 hay un contedor.")
    bot.run ("")

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
     print("Bot Active")

@bot.command() #here @bot.command this is required if you are making commands
async def hello(ctx): #there are commands and variables here and I must say ctx is required
     await ctx.send("Hello My Name Is Denizbrobro Bot")
     print("!hello Used.")

@bot.command() #here @bot.command this is required if you are making commands
async def say(ctx, *, message): #Here you see a new variable, the function of this variable is capital and asterisk
     await ctx.send(message) #the reason for the star here If there was no star, it would only send 1 word, but because it was a star, it sent them all
     print("!say used.")

@bot.command()
async def bye(ctx): #Here I Taught You How to Delete Messages
     await ctx.message.delete()
     await ctx.send("Good bye")
     print("!bye used.")

bot.run("Your Token Here")

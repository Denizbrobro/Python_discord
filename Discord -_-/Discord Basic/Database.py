import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='é', intents=discord.Intents.all())

@bot.event
async def on_ready():
     print("Bot Active")


@bot.event
async def on_message(message: discord.Message):
     print("Channel » ",message.channel,"|||",message.author," » ",message.content)
     print(" ")


@bot.event
async def on_member_join(member: discord.Member):
     print("Logged in to Any Server » ",member.name," Login")
     print(" ")

@bot.event
async def on_member_remove(member: discord.Member):
     print("To Any Server » ",member.name," Signed Out")
     print(" ")

@bot.event
async def on_guild_channel_create(channel: discord.TextChannel):
     print("A Channel Has Been Created On Any Server » ",channel.name,"|")
     print(" ")

@bot.event
async def on_guild_channel_delete(channel: discord.TextChannel):
     print("On Any Server » ",channel.name,"| A Channel Has Been Deleted.")
     print(" ")


bot.run("Your Token Here")

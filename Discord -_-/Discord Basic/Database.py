import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='é', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Aktif")


@bot.event
async def on_message(message: discord.Message):
    print("Kanal » ",message.channel,"|||",message.author," » ",message.content)
    print("                                                                    ")


@bot.event
async def on_member_join(member: discord.Member):
    print("Herhangi Bir Sunucuya » ",member.name," Giriş Yaptı")
    print("                                                    ")

@bot.event
async def on_member_remove(member: discord.Member):
    print("Herhangi Bir Sunucuya » ",member.name," Çıkış Yaptı")
    print("                                                    ")

@bot.event
async def on_guild_channel_create(channel: discord.TextChannel):
    print("Herhangi Bir Sunucuda » ",channel.name,"| Diye Bir Kanal Oluşturuldu.")
    print("                                                    ")

@bot.event
async def on_guild_channel_delete(channel: discord.TextChannel):
    print("Herhangi Bir Sunucuda » ",channel.name,"| Diye Bir Kanal Silindi.")
    print("                                                    ")


bot.run("Your Token Here")
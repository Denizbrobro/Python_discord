import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Aktif")

@bot.command() #burası @bot.command eğer komut yapıyorsanız bu gerekli
async def hello(ctx): #burada komut ve değişkenler var ve söylemeliyim ctx gerekli
    await ctx.send("Hello My Name İs Denizbrobro Bot")
    print("!hello Kullanıldı.")

@bot.command() #burası @bot.command eğer komut yapıyorsanız bu gerekli
async def say(ctx, *, message): #Burada yeni bir değişken görüyorsunuz bu değişkenin görevi büyük ve yıldız
    await ctx.send(message) #burada yıldızın olma sebebi eğer yıldız olmasaydı sadece 1 kelimeyi göndericekti fakat yıldız olduğu için hepsini gönderdi
    print("!say kullanıldı.")

@bot.command()
async def bye(ctx): #Burada size Mesaj Silmeyi Öğrettim
    await ctx.message.delete()
    await ctx.send("Good bye")
    print("!bye kullanıldı.")

bot.run("Your Token Here")
import discord

client = discord.Client(intents=discord.Intents.default())

TOKEN = "token"

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("코딩 하는 중"))
    
@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send("안농", reference = message)
        
client.run(TOKEN)
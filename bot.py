import discord # 디스코드의 패키지를 import함
import random
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
bot=discord.Client(intents=intents)

TOKEN = "TOKEN" # 봇을 실행시킬 토큰 값을 불러와줌

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("포링뽀리뽀링"))

@bot.event
async def on_message(message):    
    if message.content == "!안녕":
        await message.channel.send("안농", reference = message) # !안녕을 치면 봇이 '안농'을 반환 
        
    if message.content == "!잘가":
        await message.channel.send("바잉", reference = message) # !잘가를 치면 봇이 '바잉'을 반환
        
    if message.content == "!주원":
        await message.channel.send("바보", reference = message) # !주원을 치면 봇이 '바보'를 반환

@bot.event
async def on_message(message):  
    message_content = message.content # 메세지 내용을 message_content라는 변수에 담고
    bad = message_content.find("씨발") # 메세지 내용 중 씨발이란 단어가 있다면 0 이상을 반환
    print(bad)
    if bad >= 0:
        await message.channel.send("착하고 고운말을 쓰도록 하세요") #씨발이란 단어가 있으면 "" 안에 있는 것을 반환 
        await message.delete() # 그 메세지를 삭제 시켜줌
    await bot.process_commands(message) #다음 명령어도 인식할 수 있게 하는 코드  *중요*
    
bot.run(TOKEN) # 봇을 실행시키기 위한 코드
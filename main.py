from ctypes import sizeof
from re import I
import discord 
from discord.ext import commands
from random import randint, choice
from discord import FFmpegPCMAudio
import nacl
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import datetime

intents = discord.Intents.all()
client = commands.Bot(command_prefix="bussy ", intents=intents)

language = ["en"]

Bois = {
    'Midas':346197400781586443,
    'Juul':409649079879204865,
    'Storm':420967235419635723,
    'Sten':459045285440651278,
    'Thijs':887348339794911293,
    'Tijn':420967235419635723
}

correctLanguages = ["af","ar","bg","bn","bs","ca","cs","cy","da","de","el","en","eo","es","et","fi","fr","gu","hi","hr","hu","hy","id","is","it","ja","jw","km","kn","ko","la","lv","mk","ml","mr","my","ne","nl","no","pl","pt","ro","ru","si","sk","sq","sr","su","sv","sw","ta","te","th","tl","tr","uk","ur","vi","zh-CN","zh-TW","zh"]

@client.event
async def on_ready():
    print("ready")

@client.command() # Piemel grote 
async def piemelgrote(ctx):
    piemel = randint(5,20)
    startpiemel = ["8"]
    for i in range(piemel):
        startpiemel.append("=")

    startpiemel.append("D")
    piemel = ''.join([str(elem) for elem in startpiemel])
    await ctx.send(piemel)

@client.command() # Bot joined de call en laat een natte scheet
async def scheetje(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('wet_fart.wav')
    player = voice.play(source)
    time.sleep(2)
    await voice.disconnect()

@client.event # Join geluidjes voor de bois
async def on_voice_state_update(member, before, after):
    if member.id == Bois["Sten"]:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('wet_fart.wav')
                player = voice.play(source)
                time.sleep(2)
                await voice.disconnect()
    if member.id == Bois["Storm"]:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('clown.wav')
                player = voice.play(source)
                time.sleep(10)
                await voice.disconnect()
    if member.id == 211169389259653120:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('amongus.wav')
                player = voice.play(source)
                time.sleep(4)
                await voice.disconnect()
    if member.id == Bois["Midas"]:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('bussin.wav')
                player = voice.play(source)
                time.sleep(10)
                await voice.disconnect()
    if member.id == Bois["Thijs"]:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('thijs.wav')
                player = voice.play(source)
                time.sleep(2)
                await voice.disconnect() 
    if member.id == Bois["Juul"]:
        if before.channel == None:
            if after.channel != None:
                channel = after.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('juul.wav')
                player = voice.play(source)
                time.sleep(2)
                await voice.disconnect() 

@client.event # Geluidjes of berichtjes voor typen
async def on_message(message):
    if message.author.id == Bois["Tijn"]:
        await message.channel.send("boeie")
    if message.author.id == Bois["Storm"]:
        if message.author.voice != None:
            channel = message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('horn.wav')
            player = voice.play(source)
            time.sleep(1)
            await voice.disconnect()
    
    await client.process_commands(message)

@client.event # Sten 
async def on_typing(channel, user, when):
    if user.id == Bois["Sten"]:
        await channel.send("boeie sten")

@client.command() # Random kick
async def kick(ctx):
    if ctx.author.voice != None:
        if ctx.author.permissions_in(ctx.author.voice.channel).move_members:
            if ctx.author.id == Bois["Thijs"]:
                member = Bois["Thijs"]
                await member.move_to(None)
            else:
                channel = ctx.author.voice.channel
                members = channel.members
                member = choice(members)
                await member.move_to(None)

@client.command() # TTS
async def tts(ctx, *, args=""):
    if len(args) < 200 and len(args) > 0:
        gTTS(text=args, lang=language[-1], slow=False).save("temp.mp3")
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("temp.mp3")
        player = voice.play(source)
        audio = MP3("temp.mp3")
        time.sleep(audio.info.length + 3)
        await voice.disconnect()

@client.command() # TTS language change
async def ttslan(ctx, *, args=""):
    isCorrect = False
    for codes in correctLanguages:
        if codes == args:
            isCorrect = True
            break
    if isCorrect:
        language.append(args)
    else:
        await ctx.send("Neem een correcte taal op")

# command that will get the current time
@client.command()
async def time(ctx):
    await ctx.send(datetime.datetime.now().strftime("%H:%M:%S"))

# command to google something
@client.command()
async def google(ctx, *, args=""):
    if len(args) < 200 and len(args) > 0:
        await ctx.send(f"https://www.google.com/search?q={args}")

# command to get current date
@client.command()
async def date(ctx):
    await ctx.send(datetime.datetime.now().strftime("%d-%m-%Y"))
    
if __name__ == "__main__":
    client.run("Your Bot token")


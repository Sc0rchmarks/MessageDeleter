import discord, os, re, read; from dotenv import load_dotenv; from asyncio import sleep;
load_dotenv()
token = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#!'): 
        
        try:
            test = read.resolveTime('#![0-9]*[d|m|s|h|D|M|S|H]', message.content)
            await message.add_reaction("✅")
            await sleep(test)
            await message.delete()
        except:
            await message.reply("The time you entered is invalid, the proper syntax is #![time to wait][d|h||m|s]")

        

client.run(token)



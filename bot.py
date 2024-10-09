import os
import discord

# 環境変数からDiscordのトークンを取得
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        await message.channel.send('hay')

client.run(TOKEN)
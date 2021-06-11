import os.path
import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Account in use: {0.user}'.format(client))
    time.sleep(1)
    print('type .scr in any channel to begin scraping dms')

@client.event
async def on_message(message):

    if(message.content == ".scr"):
        channels = client.private_channels
        for channel in channels:
            if isinstance(channel, discord.DMChannel):
                   file = open(f"{message.channel.id}.txt", "w+", encoding="utf-8")
                   async for message in channel.history(limit=9999):
                       file.write(f"{message.created_at} {message.author.name}#{message.author.discriminator}: {message.content} \r\n")





client.run('TOKEN GOES HERE', bot=False)

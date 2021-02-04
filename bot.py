import requests
import discord
import asyncio
from discord.ext import commands

oldStatus = False
server = 'copperminty.aternos.me'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def start(ctx):
    # Starts the bot
    if ctx.message.channel.name == 'owner-minecraft':
        await run(ctx)

async def run(ctx):
    global oldStatus
    while True:
        print('Checking...')
        response = await getStatus()
        currentStatus = response[0]
        if currentStatus != oldStatus:
            embed1=discord.Embed(title='Minecraft Server Status: {}'.format(currentStatus.upper()) , color=0x01f9f5)
            if currentStatus == 'true':
                embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/759223940236312647/806360046858010634/0-4640_image-royalty-free-clipart-check-mark-green-check.png')
                embed1.add_field(name='Number of Online Players', value='{}/{}'.format(response[1],response[2]), inline=False)
            else:
                embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/759223940236312647/806360274420236308/4844_x_to_doubt.png')
            await ctx.send(embed=embed1)
            oldStatus = currentStatus
        await asyncio.sleep(5)

async def getStatus():
    r = requests.get('https://eu.mc-api.net/v3/server/status-http/{}'.format(server))
    return r.text.split(',')

client.run("ODA2NzE5NDUzNTI5Mzc0NzIx.YBtiCQ.DJ2NQ0rhkKMQLAmI2ovuPBJn8Fk")

import os

import discord as d

from rip import gravestone_png

client = d.Client()

@client.event
async def on_message(msg):
    if msg.content.startswith("!rip"):
        query = msg.content[len('!rip '):]
        await client.send_file(msg.channel, gravestone_png(query), filename="rip.png")

def start_discord():
    client.run(os.environ.get('DISCORD_TOKEN'))

if __name__ == '__main__':
    start_discord()

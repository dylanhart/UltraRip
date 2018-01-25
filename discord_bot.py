import os

import discord as d

from rip import base_url

client = d.Client()

@client.event
async def on_message(msg):
    if msg.content.startswith("!rip"):
        query = msg.content[len('!rip '):]
        img_url = '{}/gen_img.png?{}'.format(base_url, query)
        embed = d.Embed().set_image(url=img_url)
        await client.send_message(msg.channel, embed=embed)

def start_discord():
    client.run(os.environ.get('DISCORD_TOKEN'))

if __name__ == '__main__':
    start_discord()

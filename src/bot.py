import os

import discord
from discord.ext.commands import Bot


BOT_PREFIX = ('?', '!')

p2_bot = Bot(command_prefix=BOT_PREFIX)
client = discord.Client()

@client.event
async def on_member_join(member):
  server = member.server
  fmt = 'Welcome {0.mention} to {1.name}!'
  await client.sent_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    msg = 'Hello {0.author.mention}'.format(message)
    await client.send_message(message.channel, msg)

@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}')

client.run(os.environ.get('DISCORD_TOKEN'))

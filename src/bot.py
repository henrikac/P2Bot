import os

import discord
from discord.ext.commands import Bot


BOT_PREFIX = ('?', '!')

p2_bot = Bot(command_prefix=BOT_PREFIX)
client = discord.Client()

@client.event
async def on_member_join(member):
  channel = member.server.get_channel(os.environ.get('DISCORD_CHANNEL'))
  fmt = 'Welcome {0.mention} to {1.name}!'
  await client.sent_message(channel, fmt.format(member, channel))

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

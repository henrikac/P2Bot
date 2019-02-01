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
async def on_ready():
  print(f'Logged in as {client.user.name}')

client.run(os.environ.get('DISCORD_TOKEN'))

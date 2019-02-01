import os

import discord


client = discord.Client()

@client.event
async def on_member_join(member):
  server = member.server
  fmt = 'Welcome {0.mention} to {1.name}!'
  await client.sent_message(server, fmt.format(member, server))

@client.event
async def on_ready():
  print(f'Welcome back {client.user.name}')

client.run(os.environ.get('DISCORD_TOKEN'))

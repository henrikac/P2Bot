import os
import random

import discord
from discord.ext.commands import Bot


BOT_PREFIX = ('?', '!')

p2_bot = Bot(command_prefix=BOT_PREFIX)

@p2_bot.event
async def on_member_join(member):
  channel = member.server.get_channel(os.environ.get('DISCORD_CHANNEL'))
  fmt = 'Welcome {0.mention} to {1.name}!'
  await p2_bot.sent_message(channel, fmt.format(member, channel))

@p2_bot.event
async def on_message(message):
  if message.author == p2_bot.user:
    return

  if message.content.startswith('!hello'):
    GREETINGS = [
      'Hello',
      'Hello there',
      'Hi',
      'How are you doing?',
      'Yo!',
      'Whazzup?'
    ]

    msg = '{0} {1.author.mention}'.format(random.choice(GREETINGS), message)
    await p2_bot.send_message(message.channel, msg)

@p2_bot.event
async def on_ready():
  print(f'Logged in as {client.user.name}')

p2_bot.run(os.environ.get('DISCORD_TOKEN'))

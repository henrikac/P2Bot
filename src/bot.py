import os
import random

import discord
from discord.ext.commands import Bot, CommandNotFound

import settings

DISCORD_CHANNEL = None
DISCORD_TOKEN = None

if 'DISCORD_CHANNEL' in os.environ:
  DISCORD_CHANNEL = os.environ.get('DISCORD_CHANNEL')
  DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
else:
  DISCORD_CHANNEL = settings.DISCORD_CHANNEL
  DISCORD_TOKEN = settings.DISCORD_TOKEN

BOT_PREFIX = ('?', '!', '.')

p2_bot = Bot(command_prefix=BOT_PREFIX)

# ===== EVENTS ===== #

@p2_bot.event
async def on_member_join(member):
  guild = p2_bot.get_guild(DISCORD_CHANNEL)
  msg = f'Welcome {member.mention} to {guild.name}!'
  await p2_bot.send(msg)

@p2_bot.event
async def on_ready():
  print(f'Logged in as {p2_bot.user.name}')

@p2_bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.author.send(f'Unknown command: {ctx.command}')  # sends private msg to the author
    return

# ====== COMMANDS ===== #

@p2_bot.command(name='hello', description='Get a random greeting', brief='Get a random greeting')
async def hello(ctx):
    print('Message entered')
    GREETINGS = [
      'Hello',
      'Hello there',
      'Hi',
      'How are you doing?',
      'Yo!',
      'Whazzup?'
    ]

    msg = f'{random.choice(GREETINGS)} {ctx.author.mention}'
    await ctx.send(msg)

@p2_bot.command(name='ping', description='ping pong', brief='ping pong', pass_context=True)
async def ping(ctx):
  await ctx.send(':ping_pong: pong!! xD')

@p2_bot.command(name='king', description='surprise *evil laugh', brief='surprise *evil laugh*')
async def king(ctx):
  guild = p2_bot.get_guild(DISCORD_CHANNEL)
  await ctx.send(':crown: All hail King Henrik! :crown:')


p2_bot.run(DISCORD_TOKEN)

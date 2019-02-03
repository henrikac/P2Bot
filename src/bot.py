from datetime import datetime
import os
import random

import discord
from discord.ext import commands

# ===== SETUP ===== #

DISCORD_CHANNEL = None
DISCORD_TOKEN = None

if 'DISCORD_CHANNEL' in os.environ:
  DISCORD_CHANNEL = os.environ.get('DISCORD_CHANNEL')
  DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
else:
  import settings

  DISCORD_CHANNEL = settings.DISCORD_CHANNEL
  DISCORD_TOKEN = settings.DISCORD_TOKEN

BOT_PREFIX = ('?', '!', '.')

bot = commands.Bot(command_prefix=BOT_PREFIX)

# ===== EVENTS ===== #

@bot.event
async def on_member_join(member):
  guild = bot.get_guild(DISCORD_CHANNEL)
  msg = f'Welcome {member.mention} to {guild.name}!'
  await bot.send(msg)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.author.send(f'Unknown command: {ctx.command}')  # sends private msg to the author
    return

# ====== COMMANDS ===== #

@bot.command(name='hello', description='Get a random greeting', brief='Get a random greeting')
async def hello(ctx):
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

@bot.command(name='ping', description='ping pong', brief='ping pong', pass_context=True)
async def ping(ctx):
  await ctx.send(':ping_pong: pong!! xD')

@bot.command(name='king', description='surprise *evil laugh', brief='surprise *evil laugh*')
async def king(ctx):
  await ctx.send(':crown: All hail King Henrik! :crown:')

@bot.command(name='watson', description='get my attention', brief='get my attention')
async def watson(ctx):
  RESPONSES = [
    'You rang?',
    'What can I do for you?',
    'At your service',
    'Yeeees..?',
    'Can a hard working bot not get 2 minutes of rest?'
  ]

  msg = f'{random.choice(RESPONSES)} {ctx.author.mention}'
  await ctx.send(msg)

@bot.command(name='flip', description='flip a coin', brief='flip a coin')
async def flip(ctx):
  random.seed(datetime.now())
  result = None
  coin_val = random.randint(0, 1)

  if coin_val == 1:
    result = 'heads'
  else:
    result = 'tails'

  await ctx.send(result)


bot.run(DISCORD_TOKEN)


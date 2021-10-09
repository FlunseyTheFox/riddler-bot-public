import os
import nextcord as discord
import tweepy
import random
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.voice_client import VoiceClient
from discord.ext.commands import command,has_permissions


#|=================================================================|
#| Please give credit to me as the dev, modifying is OK            |
#| Please don't redistribute                                       |
#| Modify for use if needed                                        |
#| Bot no longer maintained                                        |
#| Bot uses code from my main bot, this is just an experiment i did|
#|=================================================================|

prefix = '?' # Commands prefix

discord_run_token = 'key' # Discord Key

client = commands.Bot(command_prefix = prefix) # Defines "Client" / DO NOT CHANGE

client.remove_command("help") # Removes help command to add custom one later.

activitystatus = 'for ?help' # Playing status message

riddle = random.choice(open('riddles').readlines()) # Defines "Riddle"

feedbackchannel = 'ID' # ID For Bot Feedback Channel

@client.event
async def on_ready():
    print("Online")
    # Changes Playing Status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activitystatus))

@client.command(pass_context = True)
async def ping(ctx):
    await ctx.send(f"You are weaker than I could ever imagine {ctx.message.author.name}.")

@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    embed.set_author(name="Commands")
    embed.add_field(name="Riddle", value="Gives an riddle",  inline=True)
    if feedbackchannel != 'ID':
        embed.add_field(name="Feedback", value="Send feedback to the bot developer",  inline=False)
    embed.add_field(name="Ping", value="Pong",  inline=True)
    embed.add_field(name="Help", value="Displays This Message",  inline=True)
    embed.add_field(name="About", value="Bot information",  inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def about(ctx):
    # Please don't remove source code like or credit to me!
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    embed.set_author(name="About")
    embed.add_field(name="Bot", value="Riddler Based Off [The Riddler](https://en.wikipedia.org/wiki/Riddler)",  inline=True)
    embed.add_field(name="Developer", value="ProtogenDev#2569",  inline=False)
    embed.add_field(name="Discord", value="Code: j48rF5d [Join](https://discord.gg/j48rF5d)")
    embed.add_field(name="Version", value="1 (Beta)",  inline=True)
    embed.add_field(name="Source Code", value="https://github.com/FlunseyTheFox/riddler-bot-public",  inline=False)
    embed.add_field(name="Riddle Sources", value="Riddles are from various Batman media and other sources. Including but not limited too shows, Batman Arkham games.",  inline=True)
    await ctx.send(embed=embed)

@client.command()
async def riddle(ctx):
    riddle = random.choice(open('riddles').readlines())
    if "Racetrack" in riddle:
        rtimages = random.choice(open('raceimages').readlines())
        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.set_author(name="Riddle")
        embed.set_image(url=rtimages)
        embed.add_field(name="Riddle me this...", value="Racetrack",  inline=True)
        await ctx.send(embed=embed)
        return
        


    embed = discord.Embed(
        color = discord.Color.green()
    )
#    embed.set_author(name="Riddle me this...")
    embed.set_image(url="")
    embed.add_field(name="Riddle", value=riddle,  inline=True)
#    embed.add_field(name="Answer", value="||"+"Coming Soon"+"||")
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def feedback(ctx, *args):
    if feedbackchannel == 'ID':
        return await ctx.send("Feedback is not setup!")
    output = ''
    for word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    embed.set_author(name="New Feedback")
    embed.add_field(name="Sender", value=ctx.message.author.mention)
    embed.add_field(name="Name", value=ctx.message.author.name)
    embed.add_field(name="User ID", value=ctx.message.author.id)
    embed.add_field(name="Feedback", value=output)
    channel = client.get_channel(feedbackchannel) # feedbackchannel
    await channel.send(embed=embed)
    await ctx.send(":white_check_mark: Your feedback has been sent to my developer!")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Riddle me this: Who is human and does not have access to that? Answer: YOU!")
        return
    if isinstance(error, CommandNotFound):
        return
    raise error

if discord_run_token == 'key':
    print("Please add token!")
else:
    client.run(discord_run_token)
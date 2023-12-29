import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
# event: something happens that triggers the bot so it can respond to it.

# gives the bot limited access to what they listen to/recieve
intents = discord.Intents.default()

# allows the bot to access the contents of user messages
intents.message_content = True 
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

# async function is when we don't need to wait for the current execution to be done before we move on to the next.
@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')  # verification

'''
@client.event
# a function that sends a message on the channel
async def on_message(message):
    # return right away if the current author is the bot so its not an infinite loop where it keeps sending messages
    if message.author == client.user:
        return
    # if the message sent includes this word, it triggers the bot to respond back
    if message.content.startswith('$Send Daily Assignments'):
        await message.channel.send('These are the assignments due today: ')
'''

@bot.command()
    # ctx stands for 'Context as the first one'
    # inside of Embed, I pass the arguments i want in my embed like title, link, description, etc
async def embed(ctx):
    embed=discord.Embed(title="Daily Assignments", url="https://csufullerton.instructure.com/calendar#view_name=month&view_start=2023-12-19", 
                        description=f'This a list of assignments due {datetime.datetime.now().strftime("%x")}', color=10181046)
    embed.add_field(name="Number of assignments", value="3", inline=True)
    embed.add_field(name="Insert Cat Picture", value="here is a fun cat pic to lighten your day", inline=True)
    embed.add_field(name="Course name 1 ", value="assignment details + link", inline=False)
    embed.add_field(name="Course name 2 ", value="assignment details + link", inline=False)
    embed.add_field(name="Course name 3 ", value="assignment details + link", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)

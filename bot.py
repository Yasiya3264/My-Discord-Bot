import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!send"):
        msg = message.content.split(" ", 1)[1]
        await message.delete()
        await message.channel.send(msg)

# Replace this value with your server ID and channel ID
GUILD_ID = '1183117936408404148'
CHANNEL_ID = '1188706807770787842'

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(CHANNEL_ID))
    
    # Create an embedded message
    embed = discord.Embed(
        title="New Member Joined!",
        description=f"Welcome {member.mention} to the server! \n\n **Play on our Minecraft Serve** : ```66.206.27.170:50501```",
        color=discord.Color.green()
    )

    # Set timestamp in the footer
    embed.set_footer(text=f"{bot.user} || New user notification || MatriX Minecraft Server")

    # Set thumbnail to the member's avatar
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1183401724698951681/dd1af5c577d45c8d5a2299756f5f2b2f.png")

    # Send the embedded message to the specified channel
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(CHANNEL_ID))
    
    # Create an embedded message
    embed = discord.Embed(
        title="Member Left",
        description=f"Goodbye {member.mention}!",
        color=discord.Color.red()
    )

    # Set timestamp in the footer
    embed.set_footer(text=f"{bot.user} || User leave notification || MatriX Minecraft Server")

    # Set thumbnail to the member's avatar
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1183401724698951681/dd1af5c577d45c8d5a2299756f5f2b2f.png")

    # Send the embedded message to the specified channel
    await channel.send(embed=embed)

SERVER_ID = '1183117936408404148'

@tasks.loop(seconds=10)  # Update every 10 seconds, you can adjust this as needed
async def update_status():
    server = bot.get_guild(int(SERVER_ID))

    if server:
        member_count = server.member_count
        activity = discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} members!")
        await bot.change_presence(activity=activity)

bot.run("MTE4MzQ0NTA4NzE1MDE1Nzg2NA.G35LNx.jHeLUs-AACYbUzkpZhIxYb9gEIySNlRJ36s-BI")

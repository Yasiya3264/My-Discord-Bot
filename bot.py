import discord
from discord.ext import commands
from discord.ext import tasks
import ping3
import socket
import time

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Use the bot.event decorator to wait until the bot is ready before adding the cog
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await clear_channel_messages()
    await check_minecraft_status.start()

# SEND COMMAND FOR ADMINS & OTHER CUSTOM COMMANDS
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!send"):
        msg = message.content.split(" ", 1)[1]
        await message.delete()
        await message.channel.send(msg)

    elif message.content.startswith("!ip"):
        server_ip_list = (
            "List of available servers : \n\n :green_circle:  Minecraft Server : `66.206.27.170:50501`  \n\n :red_circle:  TeamSpeak Server : `66.206.27.170:9964`  \n --------------------------------------------------------- \n :green_circle: Server is online  \n\n :red_circle: Server is offline"
        )
        await message.channel.send(server_ip_list)

# DISCORD SERVER WELCOME AND GOOD BYE MESSAGE SENDER
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        description=f"Welcome {member.mention} to the **MatriX e-Sports** discord server! \n\n **Good Luck Have Fun Guys...** \n Please go through our discord server rules :)",
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

# MINECRAFT SERVER STATUS CHECKER
#------------------------------------------------------------------------------------------------------------------------------------------------------

# Replace this value with your server ID and channel ID
GUILD_ID = '1183117936408404148'
CHANNEL_ID = '1183117938937577629'

# Function to clear messages in the specified channel
async def clear_channel_messages():
    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(CHANNEL_ID))

    print(f"Clearing messages in channel: {channel}")

    # Fetch and delete messages in the channel
    async for message in channel.history(limit=None):
        await message.delete()

    print("Messages cleared in this channel")

last_status = None  # Initialize last_status
last_message_id = None  # Initialize last_message_id

@tasks.loop(seconds=5)
async def check_minecraft_status():
    global last_status
    global last_message_id

    # THI 101,101,102 LINES USING FOR GET SPECIFIC DISCORD SERVER MEMBER COUNT AND DISPLAY IT ON BOT'S STATUS WITH WATCHING ACTIVITY...
    guild = bot.get_guild(int(GUILD_ID))
    member_count = len(guild.members)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} members"))

    server_ip = "66.206.27.170"
    server_port = 50501  # Replace with your Minecraft server port

    try:
        with socket.create_connection((server_ip, server_port), timeout=5):
            is_online = True
    except OSError:
        is_online = False

    guild = bot.get_guild(int(GUILD_ID))
    channel = guild.get_channel(int(CHANNEL_ID))

    print(f"Server Status: {is_online}")

    if last_message_id:
        try:
            message = await channel.fetch_message(last_message_id)
            print(f"Editing Message ID: {last_message_id}")
            await message.edit(embed=online_embed() if is_online else offline_embed())
        except discord.NotFound:
            print(f"Old Message ID {last_message_id} not found. Proceeding with sending a new message.")
    else:
        print("No previous message ID. Sending a new message.")
        message = await channel.send(embed=online_embed() if is_online else offline_embed())
        last_message_id = message.id

    last_status = "online" if is_online else "offline"

    print(f"Last Status: {last_status}, Last Message ID: {last_message_id}")

def online_embed():
    return discord.Embed(
        title="Minecraft Server Status",
        description=":green_circle:  The Minecraft server is currently online! \n ```66.206.27.170:50501```",
        color=discord.Color.green()
    )

def offline_embed():
    return discord.Embed(
        title="Minecraft Server Status",
        description=":red_circle:  The Minecraft server is currently offline. \n ```66.206.27.170:50501```",
        color=discord.Color.red()
    )

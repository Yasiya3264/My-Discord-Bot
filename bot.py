import discord
from discord.ext import commands
from discord.ext import tasks
import ping3
import socket


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace this value with your server ID and channel ID
# Function to clear messages in the specified channel
async def clear_channel_messages():
    guild = bot.get_guild(int(1183117936408404148))
    channel = guild.get_channel(int(1183117938937577629))

    print(f"Clearing messages in channel: {channel}")

    # Fetch and delete messages in the channel
    async for message in channel.history(limit=None):
        await message.delete()

    print("Messages cleared in this channel")

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

    if message.content.startswith("!say"):
        msg = message.content.split(" ", 1)[1]
        await message.delete()
        await message.channel.send(msg)

    elif message.content.startswith("!ips"):
        server_ip_list = (
            "**List of available servers** :\n\n💚 Minecraft Server : ```66.206.27.170:50501``` \n🔴 TeamSpeak Server : ```66.206.27.170:9964```\n --------------------------------------------------------- \n💚 = Server is online \n🔴 = Server is offline"
        )
        await message.channel.send(server_ip_list)
    # This command for send announcement from your message
    elif message.content.startswith("!type"):  # Fix: use `startswith` instead of `start`
        # Extract the content after "!type "
        content = message.content[len("!type "):]
        
        # Create an embedded message
        embed = discord.Embed(
            title="MatriX s-Sport announcements :loudspeaker:",
            description=f"```{content}```",
            color=discord.Color.red()
        )
        
        # Delete the original command message
        await message.delete()

        # Set timestamp in the footer
        embed.set_footer(text=f"{bot.user} || {message.author}")

        # Set thumbnail to a custom image URL
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1127473106731151430/1189204614961172530/wallpaper_minecraft_pc_bundle_1920x1080.png")

        # Send the embedded message to the same channel where the command was invoked
        await message.channel.send(embed=embed)

# DISCORD SERVER WELCOME AND GOOD BYE MESSAGE SENDER
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Replace this value with your server ID and channel ID
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(int(1183117936408404148))
    channel = guild.get_channel(int(1188706807770787842))
    
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
    guild = bot.get_guild(int(1183117936408404148))
    channel = guild.get_channel(int(1188706807770787842))
    
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
# ------------------------------------------------------------------------------------------------------------------------------------------------------

last_status = None  # Initialize last_status
last_message_id = None  # Initialize last_message_id

# Define the channel ID where you want to send error messages
error_channel_id = 1189202119283183726  # Replace with the actual channel ID

# Get the error channel
error_channel = bot.get_channel(error_channel_id)

@tasks.loop(seconds=5)
async def check_minecraft_status():
    global last_status
    global last_message_id  # Add this line

    # Get server and channel information
    guild = bot.get_guild(int(1183117936408404148))
    member_count = len(guild.members)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} members | `!ips` to view available servers"))

    server_ip = "66.206.27.170"
    server_port = 50501  # Replace with your Minecraft server port

    try:
        with socket.create_connection((server_ip, server_port), timeout=5):
            is_online = True
    except OSError:
        is_online = False

        # Send a message to the error channel
        if error_channel:
            await error_channel.send("Error checking server status. Check the logs for details.")

    guild = bot.get_guild(int(1183117936408404148))
    channel = guild.get_channel(int(1183117938937577629))

    message = None  # Declare message outside the if block

    if last_message_id:
        try:
            message = await channel.fetch_message(last_message_id)
            await message.edit(embed=online_embed() if is_online else offline_embed())
            last_message_id = message.id  # Set last_message_id here
        except discord.NotFound:
            # Proceeding with sending a new message
            last_message_id = None  # or set it to some default value if needed
    else:
        # Sending a new message
        message = await channel.send(embed=online_embed() if is_online else offline_embed())
        last_message_id = message.id  # Now it won't raise UnboundLocalError

    last_status = is_online

def online_embed():
    embed = discord.Embed(
        title="Minecraft Server Status",
        description=":green_circle:  The Minecraft server is currently online! \n ```66.206.27.170:50501```",
        color=discord.Color.green()
    )
    # Set the thumbnail to an image URL
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1183401724698951681/dd1af5c577d45c8d5a2299756f5f2b2f.png")
    return embed

def offline_embed():
    embed = discord.Embed(
        title="Minecraft Server Status",
        description=":red_circle:  The Minecraft server is currently offline. \n ```66.206.27.170:50501```",
        color=discord.Color.red()
    )
    # Set the thumbnail to an image URL
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1183401724698951681/dd1af5c577d45c8d5a2299756f5f2b2f.png")
    return embed

bot.run("ADD_YOUR_BOT_TOKEN_HERE")

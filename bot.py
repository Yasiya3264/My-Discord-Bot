import discord
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Use the bot.event decorator to wait until the bot is ready before adding the cog
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

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

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!ip"):
        # msg = message.content.split(" ", 1)[1]
        # await message.delete()
        server_ip_list = (
            "List of available servers : \n\n :green_circle:  Minecraft Server : `66.206.27.170:50501`  \n\n :red_circle:  TeamSpeak Server : `66.206.27.170:9964`  \n --------------------------------------------------------- \n :green_circle: Server is online  \n\n :red_circle: Server is offline"
        )
        await message.channel.send(server_ip_list)
#please add your bot token to run this scripts
bot.run("")

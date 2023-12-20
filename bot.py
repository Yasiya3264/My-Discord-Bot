import discord
from discord.ext import commands
from discord.ext import tasks


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

@bot.event
async def on_member_join(member):
    target_channel_id = 1126551692511555675

    target_channel = bot.get_channel(target_channel_id)

    if target_channel:
        embed = discord.Embed(
            title=f"Welcome to the server, {member.name}!",
            description="We're glad to have you here \n **🚀Please read rules before playing on MatriX Minecraft SMP server...**",
            color=discord.Color.red()
        )

        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/UqpL7RQ2kkeRlUALWic3LwyEjT9GNt33yK962ONldv0/https/cdn.discordapp.com/avatars/1183401724698951681/dd1af5c577d45c8d5a2299756f5f2b2f.png?format=webp&quality=lossless")

        await target_channel.send(embed=embed)
    else:
        print(f"Error: Target channel with ID {target_channel_id} not found.")


@bot.event
async def on_member_remove(member):
    target_channel_id = 1126551692511555675

    target_channel = bot.get_channel(target_channel_id)

    if target_channel:
        await target_channel.send(f"Goodbye {member.name}! We'll miss you.")
    else:
        print(f"Error: Target channel with ID {target_channel_id} not found.")

    update_status.start()

@tasks.loop(seconds=1)
async def update_status():
    target_guild_id = 1124047934011490347
    target_guild = bot.get_guild(target_guild_id)

    if target_guild:
        member_count = target_guild.member_count

        activity = discord.Activity(type=discord.ActivityType.watching,name=f"over {member_count} members")
        await bot.change_presence(activity=activity)
    else:
        print(f"Error: Target guild with ID {target_guild_id} not found.")



bot.run("MTE4MzQ0NTA4NzE1MDE1Nzg2NA.GbXXAn.8ec_3-epoTmaKY03TO_y--4P6UZXuRexSTRTQY")

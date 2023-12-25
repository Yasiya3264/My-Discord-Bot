Please make sure to add the required imports to your file head.

````
import discord
from discord.ext import commands, tasks
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
````


Please make sure to change ``discord_bot_token``, ``channel_id`` and ``server_id`` to actual values. Mine values may not works.

````
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
````

To get you bot token please visit **```https://discord.com/developers/applications > Your application > Bot > Copy token```** and paste it here

# dependencies

<ul>
  <li>Python 3.12.10 <a href="https://www.python.org/downloads/">Click Here to download letest python vertion</a></li>
  <li>Discord.py Library</li>
</ul>

# Discord.py Library

* To install discord.py on Windows, you can use the following steps:

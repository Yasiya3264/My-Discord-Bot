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
<hr>

## Dependencies

1. **discord.py:**
   - *Description:* `discord.py` is a Python library for interacting with the Discord API. It provides an asynchronous interface to interact with Discord servers, channels, and users.
   - *Installation:* Install using `pip install discord.py`.

2. **asyncio:**
   - *Description:* `asyncio` is a Python library for writing asynchronous code. It is often used in conjunction with `discord.py` to handle asynchronous tasks efficiently.
   - *Installation:* It comes with the Python standard library, so no additional installation is needed.

3. **Python-dotenv:**
   - *Description:* `python-dotenv` allows you to load environment variables from a file (`.env`) into your Python script, which is useful for storing sensitive information like API tokens.
   - *Installation:* Install using `pip install python-dotenv`.

4. **Others:**
   - *Optional Dependencies:* Depending on the specific functionality of your bot, you might use additional libraries. For example, `requests` for making HTTP requests, `beautifulsoup4` for web scraping, or `google-api-python-client` for interacting with Google APIs.

## Installation

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```

<hr>

#Discord.py Library

To install discord.py on ```Windows```, you can use the following steps:

**Open Command Prompt:**
Open the Command Prompt or PowerShell on your Windows machine. You can do this by searching for "cmd" or "PowerShell" in the Start menu.
<br>
**Install discord.py:**
Use the following command to install the `discord.py` library using `pip`:

````
pip install discord.py
````

**Save the file and run it using the command:**

````
python your_bot.py
````
If everything is set up correctly, it should print the version of discord.py without any errors.

<hr>



# Run bot
To run a Discord bot in `Ubuntu` using **screen**, follow these steps:
01. Open a terminal window.
02. Navigate to the directory where your `bot.py` file is located using the `cd` command:
````
cd /path/to/your/bot/directory
````
03. Start a new screen session:
    This command creates a new screen session named "bot_session."
````
screen -S bot_session
````
04. Run your bot inside the screen session: `Replace python3 with the appropriate Python version if needed.`
````
python3 bot.py
````

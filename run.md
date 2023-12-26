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
05. Detach from the screen session by pressing **`Ctrl + A`, then `D`**. This leaves the screen session running in the background.<br>
    Your bot should now be running in the screen session. To reattach to the session later, use the following command:
````
screen -r bot_session
````
Remember, the specifics may vary depending on your system and setup, and you might need to install `screen` using:

````
sudo apt-get install screen
````

Make sure your Python environment is set up correctly and that you have installed all the required dependencies for your bot. Adjust the commands based on your specific requirements and configurations.

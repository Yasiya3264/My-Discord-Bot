# MatriX Discord Bot v1.0.0 Release Notes

## What's New

- **Minecraft Server Status Updates**
  - The bot now provides real-time updates on the Minecraft server status.
  - Receive notifications when the server goes online or offline.

- **Welcome and Goodbye Messages**
  - Improved welcome and goodbye messages for new members and those leaving the server.

- **Custom Commands**
  - Introducing the `!send` command for admins to send custom messages.

- **Server Information**
  - Use `!ip` to get a list of available servers and their status.

- **Watching Activity**
  - The bot now displays the server's member count as its activity.

## Bug Fixes and Enhancements

- **Channel Cleanup**
  - Implemented a channel cleanup feature to remove old messages on bot startup.

- **Improved Stability**
  - Various bug fixes and improvements for a smoother experience.

## How to Use

- Refer to the documentation for updated commands and features: <a href="https://github.com/Yasiya3264/My-Discord-Bot/blob/main/dependencies.md" target="_blank">[Documentation Link]</a>

## Installation

- Follow the installation guide in the [run.md](<a href="https://github.com/Yasiya3264/My-Discord-Bot/blob/main/installation.md" target="_blank">Link to README.md</a>) file.

## Notes

- [Optional: Any additional notes or acknowledgments.]

Thank you for using [Your Bot Name]! If you encounter any issues or have suggestions, feel free to open an issue on GitHub.

<a href="https://github.com/Yasiya3264/My-Discord-Bot" target="_blank">[GitHub Repository Link]</a>

<hr>

Certainly! Here's a template you can use for the "How to Use" section in your GitHub repository:

## How to Use
```markdown


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd your-repository
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Configure your Discord bot token:**
   - Open `config.py` and replace `YOUR_TOKEN_HERE` with your actual Discord bot token.

2. **Configure Discord server and channel IDs:**
   - Update the `GUILD_ID` and `CHANNEL_ID` variables in the script with your Discord server and channel IDs.

### Running the Bot

1. **Run the bot script:**
   ```bash
   python bot.py
   ```

2. **Invite the bot to your Discord server:**
   - Create a new Discord bot [here](https://discord.com/developers/applications).
   - Copy the bot token and replace `YOUR_BOT_TOKEN` in the following URL:
     ```
     https://discord.com/oauth2/authorize?client_id=1183445087150157864&scope=bot&permissions=YOUR_BOT_PERMISSIONS
     ```
   - Visit the modified URL to invite the bot to your server.

### Commands

- `!send <message>`: Send a custom message to the channel.
- `!ip`: Display a list of available servers and their status.

### Minecraft Server Status

- The bot will automatically check the status of your Minecraft server every 5 seconds.
- It will update the server status message in the specified Discord channel.

Feel free to customize the bot according to your needs and explore additional features!

```

Make sure to replace placeholders like `your-username`, `your-repository`, `YOUR_TOKEN_HERE`, `YOUR_BOT_TOKEN`, `YOUR_BOT_CLIENT_ID`, and `YOUR_BOT_PERMISSIONS` with your actual details. Additionally, adjust any paths or instructions based on your project structure and requirements.

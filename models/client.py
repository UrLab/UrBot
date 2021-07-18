import discord

from discord_slash import SlashCommand

from models.command_manager import CommandManager


class UrBot(discord.client):
    instance = None

    @staticmethod
    def getInstance():
        if UrBot.instance is None:
            UrBot()
        return UrBot.instance

    def __init__(self):
        if UrBot.instance is not None:
            raise RuntimeError(
                f"Trying to instanciate a second object of {__class__}")
        UrBot.instance = self
        super().__init__()

        self.slash = SlashCommand(self, sync_commands=True)
        self.commandManager = CommandManager.getInstance()

    async def on_ready(self):
        """This is called when the connection to disord's API has succeed"""
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: discord.Message):
        """Called when a message is sent womewhere the bot can access
        Args:
            message (discord.Message): The message with its metadata
        """
        if message.content and message.content[0] == "/":
            await self.commandManager.execCommand(message.content[1:], message.channel)

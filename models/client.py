import discord

from discord_slash import SlashCommand

from src.parser import parse_command
from models.command_registry import CommandRegistry


class UrBot(discord.Client):
    """UrBoT's client"""

    instance = None

    @staticmethod
    def getInstance():
        """Singleton Pattern"""
        if UrBot.instance is None:
            UrBot()
        return UrBot.instance

    def __init__(self):
        if UrBot.instance is not None:
            raise RuntimeError(
                f"Trying to instanciate a second object of {__class__}")
        UrBot.instance = self
        super().__init__()

        import src.commands  # NOQA

        self.slash = SlashCommand(self, sync_commands=True)
        self.registry = CommandRegistry.getInstance()

    async def on_ready(self):
        """This is called when the connection to disord's API has succeed"""
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: discord.Message):
        """Called when a message is sent womewhere the bot can access
        Args:
            message (discord.Message): The message with its metadata
        """
        if message.content and message.content[0] == "$":
            formatted = await parse_command(message)
            print(formatted)
            command = self.registry.get(formatted["command"]["command"])
            print(self.registry.get(formatted["command"]["command"]))
            await command(**formatted)

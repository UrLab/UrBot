import discord

from models.command_registry import CommandRegistry

registry = CommandRegistry.getInstance()


@registry.register(
    command="hi",
    description="Say hello",
    help="..."
)
async def greet(user: discord.Member, guild: discord.Guild, channel: discord.channel, command: list, initial: discord.Message):
    await channel.send("Hello")

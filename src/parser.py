import re
import discord

from exceptions.bad_format_exception import BadFormatException


async def parse_command(command: discord.Message) -> dict:
    """Parse a given string into a dictionnary of information relative to the command
    Args:
        command (string): The command the user typed
    Returns:
        Infos: An dictionnary containing the information about the command
    """

    regex = r"^\$([a-zA-Z0-9])+( (([<@&#>a-zA-Z0-9?!',éèàù\-_])+|(\"([<@&#>a-zA-Z0-9?!',éèàù\-_ ])+\")))*?$"
    if not re.match(regex, command.content):
        raise BadFormatException(msg=f"La commande ne suit pas le format {regex}")

    splitted = re.findall(
        r"((?:[<@&#>a-zA-Z0-9?!\$'éèàù\-_])+)|\"((?:[<@&#>a-zA-Z0-9?!',éèàù\-_ ])+)\"",
        command.content,
    )

    command_dict = {"command": splitted[0][0][1:]}
    command_dict["args"] = [arg[0] if arg[0] != "" else arg[1] for arg in splitted[1:]]

    return {
        "user": command.author,
        "guild": command.guild,
        "channel": command.channel,
        "command": command_dict,
        "initial": command
    }

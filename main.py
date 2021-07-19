import os
import discord
from models.client import UrBot


API_KEY = os.environ.get("API_KEY", "")
if API_KEY == "":
    raise RuntimeError("You must specify an API key")

client = UrBot.getInstance()

intents = discord.Intents.default()
intents.members = True

client.run(API_KEY)

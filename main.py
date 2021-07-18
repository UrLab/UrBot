import os

from singleton.client import Bert


API_KEY = os.environ.get("API_KEY", "")
if API_KEY == "":
    raise RuntimeError("You must specify an API key")

client = Bert.getInstance()

client.run(API_KEY)

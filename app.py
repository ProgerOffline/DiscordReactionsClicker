#-*- coding: utf-8 -*-

from data import config
from disnake import Client as DiscordClient
from disnake.ext import commands


class Clicker(DiscordClient):
    async def on_ready(self):
        print(f"Log {self.user} {self.user.id}")
    
    async def on_message(self, message):
        if message.content.startswith("!rep"):
            await message.add_reaction("✅")


client = Clicker(command_prefix=config.BOTS_SETTINGS[0]['prefix'])
client.run(config.BOTS_SETTINGS[0]['token'])
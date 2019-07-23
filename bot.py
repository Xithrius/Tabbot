"""
>> Tabbot
> Copyright (c) 2019 Xithrius
> MIT license, Refer to LICENSE for more info
"""


import sqlite3
import os
import asyncio
import json

from discord.ext import commands as comms
import discord

from handlers.modules.output import path, now, printc


class MainCog(comms.Cog):
    """ """
    def __init__(self, bot):
        """ Objects:
        comms.Bot as a class attribute
        Path to database
        Connection to the database
        Meower background task
        """
        self.bot = bot
        self.db_path = path('data', 'meow_info.db')

        if not os.path.isfile(self.db_path):
            self.createDB()

        self.conn = sqlite3.connect(self.db_path)

        self.load_meower = self.bot.loop.create_task(self.meower())
    
    """ Databasing """
    
    def createDB(self):
        self.conn = sqlite3.connect(self.db_path)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE MeowDB(id INTEGER NOT NULL PRIMARY KEY UNIQUE, meows INTEGER)''')
        self.conn.commit()
        self.conn.close()

    """ Background task loop safety """

    def cog_unload(self):
        """ Cancel background task(s) when cog is unloaded """
        self.load_meower.cancel()

    """ Background tasks """

    async def meower(self):
        """ Meowes at everyone """
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            members = [member for member in self.bot.guilds]
            print(members)
            break
        self.conn.close()

    """ Events """

    @comms.Cog.listener()
    async def on_ready(self):
        """ Alerting the owner of startup """
        printc('[ ! ]: MEOWER IS ACTIVE')

    """ Commands """

    @comms.command()
    @comms.is_owner()
    async def exit(self, ctx):
        """ Makes the client logout """
        printc('[WARNING]: CLIENT IS LOGGING OUT')
        await ctx.bot.logout()
        try:
            self.conn.close()
        except Exception as e:
            pass


if __name__ == "__main__":
    with open(path('handlers', 'configuration', 'config.json'), 'r') as f:
        token = json.load(f)
    bot = comms.Bot(command_prefix='cat ', help_command=None)
    bot.add_cog(MainCog(bot))
    bot.run(token['discord'], bot=True, reconnect=True)

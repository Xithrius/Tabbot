"""
>> Tabbot
> Copyright (c) 2019 Xithrius
> MIT license, Refer to LICENSE for more info
"""


import sqlite3
import os
import asyncio
import json
import random
import traceback

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
        c.execute('''CREATE TABLE MeowDB(id INTEGER NOT NULL PRIMARY KEY UNIQUE, name TEXT, meows INTEGER)''')
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
            members = [guild.members for guild in self.bot.guilds]
            member = random.choice(random.choice(members))
            meow = ''.join(str(y) for y in [f'{letter * random.choice(range(1, 7))}' for letter in 'Meow'])
            await member.send(meow)
            printc(f'Sent {meow} to {member.name}#{member.discriminator}')
            c = self.conn.cursor()
            try:
                c.execute('''SELECT id, meows FROM MeowDB WHERE id = ?''', (member.id,))
                meows = c.fetchall()[0][1]
                c.execute('''UPDATE MeowDB SET meows = ? WHERE id = ?''', (meows + 1, member.id))
            except IndexError:
                c.execute('''INSERT INTO MeowDB VALUES (?, ?, ?)''', (member.id, f'{member.name}#{member.discriminator}', 1))
            self.conn.commit()
            await asyncio.sleep(600)
        self.conn.commit()
        self.conn.close()

    """ Events """

    @comms.Cog.listener()
    async def on_ready(self):
        """ Alerting the owner of startup """
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with cats'))
        printc('[ ! ]: MEOWER IS ACTIVE')

    @comms.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

    """ Commands """

    @comms.command(hidden=True)
    @comms.is_owner()
    async def exit(self, ctx):
        """ Makes the client logout """
        printc('[WARNING]: MEOWER IS LOGGING OUT')
        await ctx.bot.logout()
        self.conn.close()


if __name__ == "__main__":
    with open(path('handlers', 'configuration', 'config.json'), 'r') as f:
        token = json.load(f)
    bot = comms.Bot(command_prefix='cat ', help_command=None)
    bot.add_cog(MainCog(bot))
    bot.run(token['discord'], bot=True, reconnect=True)

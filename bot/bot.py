import random

from discord import Game, Message, Status
from discord.ext.commands import Bot


class Tabbot(Bot):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def on_ready(self) -> None:
        """Sets the presence of the bot."""

        await self.change_presence(status=Status.idle, activity=Game(':3'))

    async def on_message(self, message: Message) -> None:
        send_meow = random.randint(1, 10)
        if send_meow == 1:
            await message.channel.send('Meow')

from discord.ext.commands import Cog, Context, command

from bot.bot import Tabbot


class Meowing(Cog):

    def __init__(self, bot: Tabbot) -> None:
        self.bot = bot

    @command()
    async def meows(self, ctx: Context) -> None:
        pass


def setup(bot) -> None:
    """The necessary function for loading cog(s)."""
    bot.add_cog(Meowing(bot))

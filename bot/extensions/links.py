from discord.ext.commands import Cog, command, Context

from bot.bot import Tabbot


class Links(Cog):

    def __init__(self, bot: Tabbot) -> None:
        self.bot = bot

    @command()
    async def invite(self, ctx: Context) -> None:
        pass

    @command()
    async def links(self, ctx: Context) -> None:
        pass


def setup(bot) -> None:
    """The necessary function for loading cog(s)."""
    bot.add_cog(Links(bot))

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

log = logging.getLogger("ballsdex.packages.battle")

async def setup(bot: "BallsDexBot"):
    log.info("Loading Battle package...")
    from .cog import Battle
    await bot.add_cog(Battle(bot))
    log.info("Battle package loaded successfully!")

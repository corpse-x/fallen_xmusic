import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NelXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("NelXMusic").info(
        "\x4e\x65\x6c\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x73\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x0a\x0a\x50\x6f\x77\x65\x72\x65\x64\x20\x62\x79\x20\x40\x53\x54\x45\x52\x4e\x5f\x4c\x45\x47\x49\x4f\x4e\x0a\x0a\x44\x65\x76\x20\x3a\x20\x40\x67\x68\x6f\x73\x74\x5f\x6b\x75\x6e"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NelXMusic").info("Stopping Nel Music Bot..... Shutting Down!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

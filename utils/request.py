import aiohttp
import plistlib
from .logger import getlogger

logger = getlogger("Request")

NORMAL_BASE = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version"
BRIDGEOS_BASE = "https://mesu.apple.com/assets/bridgeos/com_apple_bridgeOSIPSW/com_apple_bridgeOSIPSW.xml"
ASIMAC_BASE = (
    "https://mesu.apple.com/assets/macos/com_apple_macOSIPSW/com_apple_macOSIPSW.xml"
)


class Parser:
    @staticmethod
    async def ipsw_metadata():
        async with aiohttp.ClientSession() as session:
            async with session.get(NORMAL_BASE) as resp:
                if resp.status == 200:
                    logger.info("Successfully got result from iTunes server.")
                    data = await resp.text(encoding="utf-8")
                    return plistlib.loads(data)

                logger.error(
                    f"IPSW Server returned status code {resp.status}. Failed to get data."
                )

    @staticmethod
    async def bridgeos():
        async with aiohttp.ClientSession() as session:
            async with session.get(BRIDGEOS_BASE) as resp:
                if resp.status == 200:
                    logger.info("Successfully got result from iBridgeOS server.")
                    data = await resp.text(encoding="utf-8")
                    return plistlib.loads(data)

                logger.error(
                    f"iBridgeOS Server returned status code {resp.status}. Failed to get data."
                )

    @staticmethod
    async def mac():
        async with aiohttp.ClientSession() as session:
            async with session.get(ASIMAC_BASE) as resp:
                if resp.status == 200:
                    logger.info("Successfully got result from macOS update server.")
                    data = await resp.text(encoding="utf-8")
                    return plistlib.loads(data)

                logger.error(
                    f"macOS Update Server returned status code {resp.status}. Failed to get data."
                )

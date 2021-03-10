import asyncio

from .utils.config import load_config
from .utils.logger import getlogger
from .apple import AppleFirmware

logger = getlogger("Main")


async def run():
    logger.info("Loading config")
    config = load_config()["apple"]

    for device in config:
        logger.info(f"Loaded device : {device['identifier']}")

    main = AppleFirmware(config["apple"])
    await main.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
import os
from typing import List
from ..utils.request import Parser
from ..utils.logger import getlogger


class AppleFirmware:
    def __init__(self, device_list: List) -> None:
        self.device_list = device_list
        self.logger = getlogger("Downloader")
        if not os.path.isdir("results"):
            os.mkdir("results")

    async def start(self):
        for device in self.device_list:

            if device["type"] == "Mac":
                self.plist_data = await Parser.mac()

            elif device["type"] == "T2":
                self.plist_data = await Parser.bridgeos()

            else:
                self.plist_data = await Parser.ipsw_metadata()

            await self.download(device["identifier"])

    async def download(self, device: str):
        self.logger.info(f"Searching firmwares for {device}")
        firmware_list = self.plist_data["MobileDeviceSoftwareVersionsByVersion"]

        # 대충 찾고 download

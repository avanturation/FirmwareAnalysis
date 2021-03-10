import plistlib


async def parse_plist(plist_data, identifier: str):
    index = str(max([int(tmp) for tmp in plist_data]))
    target = plist_data[index]["MobileDeviceSoftwareVersions"][identifier][
        next(iter(plist_data[index]["MobileDeviceSoftwareVersions"][identifier]))
    ]["Restore"]

    return target["FirmwareURL"]

import orjson


def load_config():
    with open("FirmwareAnalysis/config.json", "r", encoding="utf-8") as f:
        return orjson.loads(f.read())
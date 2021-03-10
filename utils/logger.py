import logging


FORMATTER = logging.Formatter(
    "[%(asctime)s] [%(filename)s] [%(name)s:%(module)s] [%(levelname)s]: %(message)s"
)


def getlogger(name) -> logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)

    if not log.hasHandlers():
        stream_handler = logging.StreamHandler()
        filehandler = logging.FileHandler(
            "FirmwareAnalysis/logs/{}.txt".format(name), "a"
        )

        stream_handler.setFormatter(FORMATTER)
        filehandler.setFormatter(FORMATTER)
        
        log.addHandler(filehandler)
        log.addHandler(stream_handler)

    return log

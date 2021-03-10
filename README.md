# FirmwareAnalysis
The Analysis of Apple internal firmware servers

## Description

A tool that can download iPhone, iPod, iPad, Apple TV, Mac (Apple Silicon), and T2 Chip.

** THIS TOOL CAN NOT DOWNLOAD INTEL-BASED MAC FIRMWARES **

(maybe HomePods either)

Apple Watch and AirPods are not available due to Apple's complicated OTA servers.

## how did u analyzed it?????

[Listening to C JAMM's music, and f**king around.](https://www.notion.so/Apple-5155739356004e66967a93309df6757b)

## How to use

clone it, write config.json like i did, and run it.

```bash
git clone https://github.com/fxrcha/FirmwareAnalysis

vi FirmwareAnalysis/config.json

mkdir FirmwareAnalysis/logs

python3 -m pip install -r FirmwareAnalysis/requirements.txt

python3 -m FirmwareAnalysis
```

and this tool will download firmwares in `results` folder.
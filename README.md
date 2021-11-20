# FirmwareAnalysis
The Analysis of Apple internal firmware servers

## Description

A tool that can download iPhone, iPod, iPad, Apple TV (partially), Mac (Apple Silicon), HomePod mini, and T2 Chip.

Basically, grabs the latest IPSW file from Apple's asset servers.

Apple Watch, AirPods, Some Apple TVs, and HomePods are not available because they only support OTA payloads.

## The Way How I analyzed it (Korean)

https://www.notion.so/Apple-5155739356004e66967a93309df6757b

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

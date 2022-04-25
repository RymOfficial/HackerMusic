import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "14621169"))
API_HASH = getenv("API_HASH", "61e480d82ff09acbf967ccea4fa2884f")
BOT_USERNAME = getenv("BOT_USERNAME", "TrishaMusicBot")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN", "5323995137:AAHCiJXcHNJgKzB5cWGLBQLZFIOGNYam98Y")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "BQBYyPf85xxq079gAA6zPIFnvuIe7cc4EqXg-U0f49BHPxNO9NGRyzZD1pIP19HXF_jpiMCPRHa0VmxNSJ4uFe9K-dUiVr3QmBP805taV79MfSP7I7utB5supuLcxUSEz-4anu2NDIU9vbLA2ctwOVceXYU9NXJcOAPimZeXlDuZmyY03tmTR56PjcqNR3dA5wPM9TgaqptDde95xiO1UP360qt8xAbbR2YBFtWbn7P8Otqv0PoDCjOUUTrRReBRQckfZs-jNvgN_Uawtd-3GLEjnTTv-kcFAiqXaGr6Rd1aaJjlX7GX3hYjvi0Kdi9Y7KrotFYC_qpuohxRyWIFA7mwAAAAAS1N7eYA")
YOUR_NAME = getenv("https://telegra.ph/file/8fddb775d567de8a63940.jpg")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5265780945").split()))
aiohttpsession = aiohttp.ClientSession()

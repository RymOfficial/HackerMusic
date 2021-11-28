import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "session")
YOUR_NAME = getenv("https://telegra.ph/file/8fddb775d567de8a63940.jpg")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1973129294 2023126723 1442442077").split()))
aiohttpsession = aiohttp.ClientSession()

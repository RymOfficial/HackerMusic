import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8763029"))
API_HASH = getenv("API_HASH", "5d0648a0d427266ec999d75f709376db")
BOT_USERNAME = getenv("BOT_USERNAME", "AdityaProbot")
BOT_TOKEN = getenv("BOT_TOKEN")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/b68d40fc2759ea46277b3.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
STRING_SESSION = getenv("STRING_SESSION")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1659876787").split()))
aiohttpsession = aiohttp.ClientSession()

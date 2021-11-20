import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8236321"))
API_HASH = getenv("API_HASH", "974c0347e3de1ba02b540f07fb970e55")
ARQ_API_KEY = getenv("ARQ_API_KEY", "FQRTDU-SYSNFN-TZKITE-ZNNMMS-ARQ")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
SESSION_NAME = getenv("SESSION_NAME", "STRING_SESSION")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
aiohttpsession = aiohttp.ClientSession()

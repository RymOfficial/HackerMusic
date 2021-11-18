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
BOT_TOKEN = getenv("BOT_TOKEN", "2120048918:AAH7p2eS_QVTb7YZRJTmFv_b8whmeyq74Pw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
SESSION_NAME = getenv("SESSION_NAME", "BQCUQzMKjuW--U77rKQgiGZIT1ttjnkCAmBU7rIbaOs3ImnnceRp2qrp6dz8FTehz7qM1d9oYSsNb0w302ZGyTj6O_ES3N6DnHUimSfy2CdoefWCdEK_3R2LImPj9v19Yzyiq4fdJGXzk-Ezvy2rTakdGavdZs3_VoogiDDfa0S_mZm3F7NYsbR8GHZ4LhG1eLESaF7GANNTsG3GO5XvI9UYlm_n-RdvIzfzdy_JY72NCXERM1KMbdYieqaMLi_FaErdCIxTcpxOuoyeucrJ0FDK6HcuqdCL8s3gH8Tptj8l9mBHY0QwGKiubJ0kJs2vw-eQRz2wbYEBLqfWMiWt1NR9d3NCKAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
aiohttpsession = aiohttp.ClientSession()


import os

from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBafho6_xVlYDnZK4cJJ_y4XIcAzNv0wTGVdx3LQN7u3VZPR64rk0szW4P3WV0ihZnfm9uTElKORftCGTf0nkn927x8AhMRPHfZQGftsYCmdCgaZT8zB8Yc43inV4mOpF8vUgPAovsou6S8ig3ty69BRQGBuicw1ZjQw-6ZzAECfpCa-84Ncxd37JjQVMnLM-xBVVyB9ZbnmDwRmAoVAUsYm5JaAAVcRhr5V5vS4b3Z4LArh15qCQ83nuuh9VBWTwVL4GboSkUnJCIecB7CZf6YQnNOqMVYlyNZMFHJ7eYTSzYrDRACaDXiZbL5trDpH4MKmLeQBSg-FOhS0OkV_dQ4a2D2nwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1986647784:AAHt08U19flMxF5oIGs8Sl8w6rhdUEf0QGU")
BOT_NAME = getenv("BOT_NAME", "MUSICBOT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DEECODEBOTS")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "7343230"))
API_HASH = getenv("API_HASH", "66ef09b43e03eeafb6a215df1948285a")
BOT_USERNAME = getenv("BOT_USERNAME", "Decode")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "xdAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DeCodeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "PatriciaXmusic")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/puroXpower")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1972352624").split()))

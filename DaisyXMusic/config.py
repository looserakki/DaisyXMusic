
import os


que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBcXQWRl31A37HdaRaZ7CblVJwv2DOb9d5keN9MFm81cQRPJBkBk6uabB4sRYDnABwJxwzrdUAwgi6B9rl0Dl44AJapDjc45F3hQsoajU6_xPSTjq3hS4AikFBEYKXWeUMsZsuhU3EZ2p-x94BA00smAm4wSs7Mi95NjVklE73-qx8MwgERPzeq_ey1yiCDaYMntO59sfOeeZEd17XjYdmha_2F3nk3AvohFi0FPOx19FY7hStIBQMMTZbUrQWKHNPcTijgfQAXYQFhYHhDkiVqaE5kO7-NL2-hIJkOxl2T7Hrw9ElRirBl0awpDUssLqTTAlwrO6MN4fSpJXiK5YxRdeEnewA")
BOT_TOKEN = getenv("BOT_TOKEN", "1942268270:AAHtPGD5rKaK_gFTL9OQasqQRHGUrAZr5aA")
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

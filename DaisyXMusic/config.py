
import os

from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCLwBS4iWuWm-dfo021j8bh-GRn2ssqdaJ9AQdiOj_4RL3X5hrOgzEVpBP_MI3GwavxuWrWn5uvXtpslD1oCX7FLlDgW6MQ6o02iIDTHY-poVTeJAPf6uE-k5HQF9B2dL6ryIHdhhGKgiHkPZMeCFqgXIMMWcnqJQ5QyIculNCmJkxmnctjXLk0KCeIg79n3Hlww2ovWwvBzR87DQwziskzJoyFUVBqyUrKyutKtFIYdFg0UfN7bpHb-YtrDwlSOaXXuu3BnqzmQmY6_ZrqYRehivatzUZPbnMHMv4Gc7IxKmMxlZW2-m3ax31CAPKI-6DAaLI6nMrmhivEDBzFj7Hea2D2nwA")
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

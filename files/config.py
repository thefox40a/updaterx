from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from pyro import validate_session

APP_ID = "24944143"
APP_HASH = "c3a7a7e23f79042411d74e870f480ae3"

ss = "1BJWap1sBuxRlwmBL_boDOEaH-0kPdoPbglNZzPAx-0S5X8UOrFHzUKhOD6g_meCMxVyrONMbsVTaY84VKbkVrIFlu6Ma-o7-_5pvdL4Tqr6kqDzKMlFprfJrFukDJxmUStGNc6yHoNZ29IHs1qO1uwc4wS1PHrokPMX4wI-arBDp_y9ZB_CUkgcKm578Xv6es1-n2ndBx89I2CFhdBXxMJaBRioUq4SzFd0iQhVxFTZhLqhohY-b5N6-u9CMyXVEIqx5Wd2Fv-ALFz3j-rQ-FuGPIpBB2e_8Zq_MAv0HgHeNe1DEiGCDqt7tOhkHSheQzoDNP1xlCeGJqSfQiy0kf_mGXmCLrsY="
session = validate_session(ss)
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# BOT_USERNAME = "YoMidobot"
# token = "7179039513:AAHPuNBfCLgq4Yf4zgLLKrQAPFKR4hZvqJM"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
from core import state
from modules import screen, logger
from modules import telegram

import time

telegram.poller.start_polling_async()

time.sleep(1)

# screen.poller.start_polling_async(2, telegram.screen_glue.send_screen)

while 1:
    input('Waiting')
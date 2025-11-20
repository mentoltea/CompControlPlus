from . import common, hooks, poller, send
from modules import logger
import telebot
import time
from tasks import task

def try_start_bot():
    try:
        common.bot = telebot.TeleBot(common.token)
        hooks.register_handlers()
        logger.LOG("Bot settled")
    except Exception as e:
        common.bot = None
        logger.ERROR(str(e))
        
def keep_trying_to_start():
    try:
        while (common.bot == None):
            try_start_bot()
        poller.start_polling_async()
    except Exception as e:
        logger.ERROR(str(e))

def keep_trying_to_start_async():
    task.ThreadTask(keep_trying_to_start)()
    
    
def queue_emptier(interval: float = 1):
    while True:
        send.empty_queue()
        time.sleep(interval)
        
def start_queue_emptier(interval: float):
    task.ThreadTask(queue_emptier, interval)()
        
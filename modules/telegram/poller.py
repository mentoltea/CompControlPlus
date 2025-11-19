from . import common
import requests
import telebot
import time
from modules import logger
from tasks import task

def poll():
    wait = 1
    maxiterations = 10
    iterations = 1
    while True:
        if not common.bot: return
        try:
            logger.LOG(f"--- Iteration {iterations} ---")
            common.bot.polling(non_stop=True)
        except requests.exceptions.ConnectionError as e:
            logger.ERROR(str(e))
        except telebot.apihelper.ApiException as e:
            logger.ERROR(str(e))
        except Exception as e:
            logger.ERROR(str(e))
            
        iterations += 1
        if (iterations > maxiterations):
            # Перезапустить бота
            pass
        
        time.sleep(wait)


def start_polling_async():
    task.ThreadTask(poll)()
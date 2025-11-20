from modules import telegram, screen

def deinitialize():
    screen.poller.stop_polling()
    telegram.poller.stop_polling()
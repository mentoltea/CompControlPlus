from . import common, handlers, hooks, poller, screen_glue
import telebot
import global_settings

common.token = global_settings.TELEGRAM_TOKEN
common.admin = global_settings.TELEGRAM_ADMIN

common.bot = telebot.TeleBot(common.token)
hooks.register_handlers()
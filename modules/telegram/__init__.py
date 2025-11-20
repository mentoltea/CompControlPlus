from . import common, handlers, hooks, poller, glue, tg_commands
import telebot
import global_settings

common.token = global_settings.TELEGRAM_TOKEN
common.admin = global_settings.TELEGRAM_ADMIN
common.MAX_TIME_SHIFT = global_settings.TELEGRAM_MAX_TIME_SHIFT

common.bot = telebot.TeleBot(common.token)
hooks.register_handlers()
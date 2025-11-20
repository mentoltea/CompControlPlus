from . import common, handlers, hooks, poller, glue, tg_commands, persistent, send
import telebot
import global_settings


common.token = global_settings.TELEGRAM_TOKEN
common.admin = global_settings.TELEGRAM_ADMIN
common.MAX_TIME_SHIFT = global_settings.TELEGRAM_MAX_TIME_SHIFT

persistent.try_start_bot()
persistent.start_queue_emptier(2)

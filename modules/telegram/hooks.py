from . import handlers
from . import common

def register_handlers():
    if (common.bot):
        common.bot.register_message_handler(handlers.text_handler, content_types=["text"])
        common.bot.register_message_handler(handlers.photo_handler, content_types=["photo"])
        common.bot.register_message_handler(handlers.document_handler, content_types=["document"])
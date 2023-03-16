# codex/__init__.py

from .core import codex
from .data import personality
from .recipes import *
from .endpoints.telegram import TelegramClient

if __name__ == '__main__':
    # Initialize CODEX AI with personality traits
    codex.initialize(personality)

    # Connect to Telegram client
    telegram_client = codex.connect_telegram_client()

    # Register recipe modules
    # ...
    # Register additional modules as needed

    # Start Telegram client
    telegram_client.run_until_disconnected()

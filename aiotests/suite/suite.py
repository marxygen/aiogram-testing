from aiogram import bot, dispatcher
from typing import Union, Type, List


class AiogramTestingSuite:
    """Aiogram testing suite class."""

    tests: List[callable]
    bot: bot.BaseBot
    dispatcher: dispatcher.Dispatcher

    def __init__(
        self,
        bot_extractor: Union[callable, Type[bot.BaseBot]],
        dispatcher_extractor: Union[callable, Type[dispatcher.Dispatcher]],
    ):
        """Initialize aiogram testing suite

        Args:
            bot_extractor (Union[callable, Type[bot.BaseBot]]): A function that returns the aiogram bot instance
            dispatcher_extractor (Union[callable, Type[dispatcher.Dispatcher]]): A function that returns the aiogram dispatcher instance
        """
        self.bot = bot_extractor() if callable(bot_extractor) else bot_extractor
        self.dispatcher = (
            dispatcher_extractor()
            if callable(dispatcher_extractor)
            else dispatcher_extractor
        )

    def register(func: callable):
        """A decorator to register a bot test"""

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

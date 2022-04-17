# aiotests

A package to test aiogram bots

# How to use it

To start you'll need to initialize the `aiotests.AiogramTestingSuite` class. It receives your bot and dispatcher (or callables that return them) as arguments.

```Python
import aiogram
import os

bot = aiogram.Bot(token=os.getenv("TEST_BOT_TOKEN"), parse_mode="HTML")
dp = aiogram.Dispatcher(bot)

suite = AiogramTestingSuite(lambda: bot, lambda: dp)
```

After that, just add the `suite.register` decorator to the function you want to call:

```Python
@suite.register()
def test_echo():
    # Do your tests here...
    ...
```

**Note**: this function must be a regular Pytest test case!

## What can I test

After you perform the steps above, your `bot` object should have additional methods provided by `aiotests`:

- `ensureAnswers()` - Makes sure the bot answers a message to the specified message

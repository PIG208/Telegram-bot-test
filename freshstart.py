from utils import get_token
import telegram

bot = telegram.Bot(token=get_token())
print(bot.get_me())


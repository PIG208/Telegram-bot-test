import json
import telegram

credentials = json.load(open('token.json'))
bot = telegram.Bot(token=credentials['token'])
print(bot.get_me())


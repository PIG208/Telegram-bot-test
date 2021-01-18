from utils import get_token
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    Filters,
    MessageHandler,
    CallbackContext
)


ARTIST, TITLE = 0, 1

data = {ARTIST: None,
        TITLE: None}


def intro(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Hi! Looking for some songs? I can help!')
    update.message.reply_text('Which artist are you looking for?')
    return ARTIST


def artist(update: Update, context: CallbackContext) -> int:
    data[ARTIST] = update.message.text
    update.message.reply_text('{}?OK!'.format(data[ARTIST]))
    update.message.reply_text('What about the song title?')
    return TITLE


def title(update: Update, context: CallbackContext) -> int:
    data[TITLE] = update.message.text
    update.message.reply_text('Great! I\'ll then be looking for {}\'s song titled {}.'
                              .format(data[ARTIST], data[TITLE]))
    return ConversationHandler.END


def quit(update: Update, context: CallbackContext):
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(get_token(), use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler("start", intro)],
        states={
            ARTIST: [MessageHandler(Filters.text, callback=artist)],
            TITLE: [MessageHandler(Filters.text, callback=title)]
        },
        fallbacks=[CommandHandler('quit', quit)]
    ))

    updater.start_polling()

    print("Bot started polling")

    updater.idle()


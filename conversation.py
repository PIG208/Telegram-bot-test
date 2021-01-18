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


ARTIST, LYRICS = 0, 1

def intro(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Hi! Looking for some songs? I can help!'
                              'Which artist are you looking for?')
    return ARTIST


def artist(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('{}?OK!'.format(update.message.text))
    return LYRICS


def lyrics(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('{}?OK!'.format(update.message.text))
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
            LYRICS: [MessageHandler(Filters.text, callback=lyrics)]
        },
        fallbacks=[CommandHandler('quit', quit)]
    ))

    updater.start_polling()

    print("Bot started polling")

    updater.idle()


from telegram import ReplyKeyboardMarkup

from Constants.bot_messages import BotMessage
from Constants.button_messages import ButtonMessage
from Constants.common import BotState, LogMessage
from Utils.general_handlers import get_chat_id
from Utils.logger import iqr_bot_logger
from database import database


def start(bot, update, user_data):
    result = update.message.to_dict()

    if update['_effective_user']['username']:
        # check username is admin
        is_admin = database().is_admin(update['_effective_user']['username'])
        user_data["is_admin"] = is_admin
        if is_admin:
            bot.send_message(get_chat_id(update), BotMessage.admin_menu,
                             reply_markup=ReplyKeyboardMarkup([[
                                 ButtonMessage.add_admin,
                                 ButtonMessage.add_user,
                                 ButtonMessage.remove_user,
                                 ButtonMessage.submit_help,
                                 ButtonMessage.show_help_by_user,
                                 ButtonMessage.show_all_helps,
                                 ButtonMessage.back_to_main]],
                                 one_time_keyboard=True))
            return BotState.admin_menu
        else:
            reply_keyboard = [[ButtonMessage.start]]
            bot.send_message(get_chat_id(update), BotMessage.not_auth,
                             reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
            return BotState.start
    else:
        reply_keyboard = [[ButtonMessage.start]]
        bot.send_message(get_chat_id(update), BotMessage.not_auth,
                         reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
        return BotState.start


def error(bot, update):
    iqr_bot_logger.warning(LogMessage.warrning, update, update.message)

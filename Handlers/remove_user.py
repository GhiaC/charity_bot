from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from database import database
from Constants.bot_messages import BotMessage

from telegram import ReplyKeyboardMarkup
from Constants.button_messages import ButtonMessage


def remove_user_step_0_handler(bot, update, user_data):
    bot.send_message(get_chat_id(update), BotMessage.select_user)
    return BotState.remove_user_step_1


def remove_user_step_1_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["remove_user"] = {"nation_id": text}

    bot.send_message(get_chat_id(update), BotMessage.are_u_sure,
                     reply_markup=ReplyKeyboardMarkup([[
                         ButtonMessage.yes,
                         ButtonMessage.no]],
                         one_time_keyboard=True))

    return BotState.remove_user_step_2

def remove_user_step_2_handler(bot, update, user_data):
    database().remove_user(user_data["remove_user"]["nation_id"])
    bot.send_message(get_chat_id(update), BotMessage.success, reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
    return BotState.admin_menu


def remove_user_step_2_cancel_handler(bot, update, user_data):
    bot.send_message(get_chat_id(update), BotMessage.cancel, reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
    return BotState.admin_menu

from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from database import database
from Constants.bot_messages import BotMessage

from telegram import ReplyKeyboardMarkup
from Constants.button_messages import ButtonMessage


def add_user_step_0_handler(bot, update, user_data):
    bot.send_message(get_chat_id(update), BotMessage.enter_name)
    return BotState.add_user_step_1


def add_user_step_1_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["add_user"] = {"name": text}

    bot.send_message(get_chat_id(update), BotMessage.enter_phone)
    return BotState.add_user_step_2


def add_user_step_2_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["add_user"]["phonenumber"] = text

    bot.send_message(get_chat_id(update), BotMessage.enter_nation_id)
    return BotState.add_user_step_3


def add_user_step_3_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["add_user"]["nationid"] = text
        bot.send_message(get_chat_id(update), BotMessage.description)
        return BotState.add_user_step_4


def add_user_step_4_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["add_user"]["description"] = text
        if database().is_exist_user(user_data["add_user"]["nationid"], user_data["add_user"]["phonenumber"]):
            bot.send_message(get_chat_id(update), BotMessage.exist, reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
            return BotState.admin_menu
        else:
            database().insert_user(user_data["add_user"]["name"], user_data["add_user"]["phonenumber"],
                                   user_data["add_user"]["nationid"], user_data["add_user"]["description"])
            bot.send_message(get_chat_id(update), BotMessage.success_insert, reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
            return BotState.admin_menu

from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from database import database
from Constants.bot_messages import BotMessage


def add_admin_step_0_handler(bot, update, user_data):
    bot.send_message(get_chat_id(update), BotMessage.enter_username)
    return BotState.add_admin_step_1


def add_admin_step_1_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["add_admin"] = text
    bot.send_message(get_chat_id(update), BotMessage.are_u_sure)
    return BotState.add_admin_step_2


def add_admin_step_2_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0 and result.get("text") == "بله":
        database().insert_admin(user_data["add_admin"])
        bot.send_message(get_chat_id(update), BotMessage.success)
    else:
        bot.send_message(get_chat_id(update), BotMessage.cancel)

    return BotState.admin_menu

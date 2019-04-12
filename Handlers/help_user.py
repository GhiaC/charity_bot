from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from database import database
from Constants.bot_messages import BotMessage


def help_user_step_0_handler(bot, update, user_data):
    def users_to_replymarkup():
        result = ''
        for user in database().get_all_user():
            result += \
                "[" + user["name"] + "]" + \
                '(send:' + str(user['id']) + ') \n'
        return result

    bot.send_message(get_chat_id(update), BotMessage.select_user + "\n" + users_to_replymarkup(), )
    return BotState.help_user_step_1


def help_user_step_1_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["help_user"] = {"id": text}

    bot.send_message(get_chat_id(update), BotMessage.enter_amount)
    return BotState.help_user_step_2


def help_user_step_2_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["help_user"]["amount"] = text
    bot.send_message(get_chat_id(update), BotMessage.description)
    return BotState.help_user_step_3


def help_user_step_3_handler(bot, update, user_data):
    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        user_data["help_user"]["description"] = text
        if not database().is_exist_user_by_id(user_data["help_user"]["id"]):
            bot.send_message(get_chat_id(update), BotMessage.dosnt_exist)
            return BotState.admin_menu
        else:
            database().insert_help(user_data["help_user"]["id"], user_data["help_user"]["amount"],
                                   user_data["help_user"]["description"])
            bot.send_message(get_chat_id(update), BotMessage.success_insert)
            return BotState.admin_menu

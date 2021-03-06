from database import database
from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from Constants.bot_messages import BotMessage
from telegram import ReplyKeyboardMarkup
from Constants.button_messages import ButtonMessage

def show_helps_by_user_step_0_handler(bot, update, user_data):
    def users_to_replymarkup():
        result = ''
        for user in database().get_all_user():
            result += \
                "[" + user["name"] + "]" + \
                '(send:' + str(user['nation_id']) + ') \n'
        return result

    bot.send_message(get_chat_id(update), BotMessage.select_user + "\n" + users_to_replymarkup())
    return BotState.show_helps_by_user_step_1_handler


def show_helps_by_user_step_1_handler(bot, update, user_data):
    def helps_to_text(id):
        result = ''
        for temp_help in database().get_all_helps_order_by_nation_id(id):
            result += \
                "توضیحات : " + temp_help["description"] + " | " + \
                'مبلغ : ' + temp_help["amount"] + '\n'
        return result

    result = update.message.to_dict()
    if len(result.get("text")) > 0:
        text = result.get("text")
        if not database().is_exist_user_by_nation_id(text):
            bot.send_message(get_chat_id(update), BotMessage.dosnt_exist,
				 reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
            return BotState.admin_menu
        else:
            bot.send_message(get_chat_id(update), helps_to_text(text), reply_markup=ReplyKeyboardMarkup([[ButtonMessage.back_to_main]], one_time_keyboard=True))
            return BotState.admin_menu
    return BotState.admin_menu

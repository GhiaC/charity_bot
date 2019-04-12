from database import database
from Constants.common import BotState
from Utils.general_handlers import get_chat_id
from Constants.bot_messages import BotMessage


def show_helps_step_0_handler(bot, update, user_data):
    def show_helps():
        result = ''
        for temp_help in database().get_all_helps():
            result += \
                "نام : " + temp_help["name"] + " | " + \
                "توضیحات : " + temp_help["description"] + " | " + \
                'مبلغ : ' + temp_help["amount"] + '\n'
        return result

    bot.send_message(get_chat_id(update), show_helps())
    return BotState.admin_menu

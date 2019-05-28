from telegram.ext import *

from Constants.bot_command import Command
from Constants.common import Pattern
from Handlers.add_admin import *
from Handlers.add_user import *
from Handlers.remove_user import *
from Handlers.authentication import *
from Handlers.help_user import *
from Handlers.show_helps import *
from Handlers.show_helps_by_user import *


def bot_handlers(dp):
    dp.add_error_handler(error)
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler(Command.start, start, pass_user_data=True), 
	RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.back_to_main),
                             callback=start, pass_user_data=True)], states={

            # authentication
            BotState.start: [
                CommandHandler(Command.start, start, pass_user_data=True),
		],

            BotState.admin_menu: [
                CommandHandler(Command.start, start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.back_to_main),
                             callback=start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.add_user),
                             callback=add_user_step_0_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.remove_user),
                             callback=remove_user_step_0_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.add_admin),
                             callback=add_admin_step_0_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.submit_help),
                             callback=help_user_step_0_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_help_by_user),
                             callback=show_helps_by_user_step_0_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.show_all_helps),
                             callback=show_helps_step_0_handler, pass_user_data=True),
            ],

            ##############################################################
            # get name
            BotState.add_user_step_1: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=add_user_step_1_handler, pass_user_data=True)
            ],
            # get phone number
            BotState.add_user_step_2: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=add_user_step_2_handler, pass_user_data=True)
            ],
            # get nation id
            BotState.add_user_step_3: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=add_user_step_3_handler, pass_user_data=True)
            ],

            # get description
            BotState.add_user_step_4: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=add_user_step_4_handler, pass_user_data=True)
            ],

            ##############################################################
            BotState.remove_user_step_1: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=remove_user_step_1_handler, pass_user_data=True)
            ],
            BotState.remove_user_step_2: [
                CommandHandler(Command.start, start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.yes),
                             callback=remove_user_step_2_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.no),
                             callback=remove_user_step_2_cancel_handler, pass_user_data=True),
            ],
            ##############################################################
            BotState.help_user_step_1: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=help_user_step_1_handler, pass_user_data=True)
            ],
            BotState.help_user_step_2: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=help_user_step_2_handler, pass_user_data=True)
            ],
            BotState.help_user_step_3: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=help_user_step_3_handler, pass_user_data=True)
            ],
            ##############################################################
            BotState.add_admin_step_1: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=add_admin_step_1_handler, pass_user_data=True)
            ],
            BotState.add_admin_step_2: [
                CommandHandler(Command.start, start, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.yes),
                             callback=add_admin_step_2_handler, pass_user_data=True),
                RegexHandler(pattern=Pattern.absolute.format(ButtonMessage.no),
                             callback=add_admin_step_2_cancel_handler, pass_user_data=True),
            ],
            ##############################################################
            BotState.show_helps_by_user_step_1_handler: [
                CommandHandler(Command.start, start, pass_user_data=True),
                MessageHandler(filters=Filters.text, callback=show_helps_by_user_step_1_handler, pass_user_data=True)
            ],
            ##############################################################
        },
        fallbacks=[CommandHandler(Command.cancel, start)]
    )
    dp.add_handler(conversation_handler)

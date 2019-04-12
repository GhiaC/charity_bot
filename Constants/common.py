class BotState:
    start = "START"

    add_user_step_1 = "ADD_USER_STEP_1"
    add_user_step_2 = "ADD_USER_STEP_2"
    add_user_step_3 = "ADD_USER_STEP_3"
    add_user_step_4 = "ADD_USER_STEP_4"

    help_user_step_1 = "HELP_USER_STEP_1"
    help_user_step_2 = "HELP_USER_STEP_2"
    help_user_step_3 = "HELP_USER_STEP_3"

    add_admin_step_1 = "ADD_ADMIN_STEP_1"
    add_admin_step_2 = "ADD_ADMIN_STEP_2"

    admin_menu = "ADMIN_MENU"

    show_helps_by_user_step_1_handler = "show_helps_by_user_step_1_handler"


class Pattern:
    absolute = "^{}$"
    zero = 0


class LogMessage:
    warrning = 'Update "%s" caused error "%s"'

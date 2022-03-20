import config 
import telebot
from main import main
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    text = """
    Здравствуйте, этот бот может говорить вам,
    разные анекдоты, выберите котегорию
    которую хотите послушать
    """
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    funny_anekdot = InlineKeyboardButton("Смешной",callback_data = "funny")
    markup.add(funny_anekdot)
    bot.send_message(message.chat.id, text, reply_markup=[markup])

@bot.callback_query_handler(func=lambda call: call.data == "funny_anekdot")
def funny_anekdot(call): 
    categories = main()
    print(categories)

    










# @bot.callback_query_handler(func=lambda call: call.data == "funny")
# def funny_anekdot(call):
#     message = call.message
#     categories = get_categories()
#     if categories['status']:



# https://clck.ru/dXnDg
# https://iplogger.org/1Vbki7
# https://iplogger.org/logger/rftt9b1Vbki7/
# https://iplogger.org/


# https://speed-tester.info/check_another_ip.php
# https://speed-tester.info/check_another_ip_info.php?id=685649&code=44464
# https://clck.ru/
























bot.infinity_polling()
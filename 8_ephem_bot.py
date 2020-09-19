"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def planet_constellation(update, context):
    today = datetime.date.today().strftime("%Y/%m/%d")
    user_text = update.message.text
    _, user_planet = user_text.split()
    if user_planet == 'Mars':
        planet = ephem.Mars(today)
    elif user_planet == 'Venus':
        planet = ephem.Venus(today)
    elif user_planet == 'Saturn':
        planet = ephem.Saturn(today)
    try:
        constellation = ephem.constellation(planet)
        update.message.reply_text(f'{user_planet} in constellation {constellation}')
    except UnboundLocalError:
        update.message.reply_text(f'We have no data for "{user_planet}"')
 

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

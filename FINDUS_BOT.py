import telebot
from flask import Flask

bot = telebot.TeleBot('5269033501:AAGwh7Nk05yzUFDwIGosVamyrqsBZvqzc30')


app = Flask(__name__)


@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, "Привет, я findus, могу ответить на следующие вопросы \n"
                                     '1)Вопросы по регистрации \n'
                                     '2)Вопросы по заполнению данных \n'
                                     '3)Вопросы по использованию площадки.Выберите нужную цифру вашего вопроса \n')


@bot.message_handler(content_types=['text'])
def answers(message):
    if message.text == "1":
        bot.send_message(message.from_user.id, "1)При регистрации нужны достоверные данные? \n")
        bot.register_next_step_handler(message, first_question)
    elif message.text == "2":
        bot.send_message(message.from_user.id, " 1)Какое минимальное количество данных нужно заполнить? \n"
                                               " 2)Какие фотографии нужны? \n"
                                               " 3) Что делать, если я не знаю русский и английский.Мне обязательно заполнять эти данные? \n "
                                               " 4)Почему я не могу создать акцию прямо сейчас? \n"
                                               " 5)Как долго проходит верификация? \n")
        bot.register_next_step_handler(message, second_question)
    elif message.text == "3":
        bot.send_message(message.from_user.id," 1)Как происходит оплата за услуги? \n"
	                                          " 2)Как мне изменить статус со «стандарт» на «бесплатный» или наоборот? \n"                  
                                              " 3)Как отменить акцию или событие? \n "
                                              " 4)Могу ли я отменить отосланное подписчикам сообщение? \n "
                                              " 5)Почему отменили мою верификацию? \n")
        bot.register_next_step_handler(message, third_question)

def first_question(message):
    if message.text.lower() == "1":
        bot.send_message(message.chat.id,'бу')
        bot.register_next_step_handler(message, first_question)
    else:
        bot.send_message(message.chat.id,
                         "Ваш запрос неккоректен.Вернитесь в начало")
        bot.register_next_step_handler(message, answers)

def second_question(message):
    if message.text.lower() == "1":
        bot.send_message(message.chat.id,"б")
        bot.register_next_step_handler(message, second_question)
    elif message.text.lower() == "2":
        bot.send_message(message.chat.id, 'бу')
        bot.register_next_step_handler(message, second_question)
    elif message.text.lower() =="3":
        bot.send_message(message.chat.id, 'буга')
        bot.register_next_step_handler(message, second_question)
    elif message.text.lower() == "4":
        bot.send_message(message.chat.id, 'бугаг')
        bot.register_next_step_handler(message, second_question)
    elif message.text.lower() == "5":
         bot.send_message(message.chat.id, 'бугага')
         bot.register_next_step_handler(message, second_question)
    else:
        bot.send_message(message.chat.id,
                         "Ваш запрос неккоректен.Вернитесь в начало")
        bot.register_next_step_handler(message, answers)
                        

def third_question(message):
    if message.text.lower() == "1":
        bot.send_message(message.chat.id,"бубу")
        bot.register_next_step_handler(message, third_question)
    elif message.text.lower() == "2":
        bot.send_message(message.chat.id,"буб")
        bot.register_next_step_handler(message, third_question)
    elif message.text.lower() == "3":
        bot.send_message(message.chat.id,"буга")
        bot.register_next_step_handler(message, third_question)
    elif message.text.lower() == "4":
        bot.send_message(message.chat.id, "бугага")
        bot.register_next_step_handler(message, third_question)
    elif message.text.lower() == "5":
        bot.send_message(message.chat.id, "бугагаг")
        bot.register_next_step_handler(message, third_question)
    else:
        bot.send_message(message.chat.id,
                         "Ваш запрос неккоректен.Вернитесь в начало")
        bot.register_next_step_handler(message, answers)

"""
@bot.message_handler(content_types=['text'])
def default_text(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Visit the website", url="http://80.78.241.142/")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку,чтобы перейти на сайт", reply_markup=keyboard)"""


bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    app.run(debug=True)

import telebot
import pandas as pd
from flask import Flask
from datetime import datetime


app = Flask(__name__)

bot: telebot.TeleBot = telebot.TeleBot("5565513901:AAFUPOQ2IxRLXKTJ4dp5-5JiFSMATl-pz98")


data: pd.DataFrame = pd.read_excel("peak_flow_metry_new.xlsx")

new_data = {
    "First try": 0,
    "Second try": 0,
    "Third try": 0,
    "Maximum": 0,
    "Date": None,
    "Symbicort Turbuhaler": 0,
    "Salbutamol": 0,
    "Relvar Ellipta": 0,
    "Pulmicort": 0,
}


@bot.message_handler(commands=["start"])
def get_info(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Enter info", callback_data="info")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Enter your data: ", reply_markup=keyboard)
    bot.register_next_step_handler(message, process_info)


@bot.message_handler(content_types=["text"])
def process_info(message):
    if message.text == "Enter info":
        bot.send_message(message.chat.id, "Hello, enter your data, separated by comma: x, y, z")
        bot.register_next_step_handler(message, get_data)


def get_data(message):
    values = [int(number) for number in message.text.split(",")]
    new_data["First try"] = values[0]
    new_data["Second try"] = values[1]
    new_data["Third try"] = values[2]
    new_data["Maximum"] = max(values)
    new_data["Date"] = pd.to_datetime(datetime.today().date())

    bot.send_message(
        message.chat.id,
        "Registered. Now write, what drugs you used:"
        "Symbicort Turbuhaler(ST), Salbutamol(S), Relvar Ellipta(RE), Pulmicort(P)",
    )
    bot.register_next_step_handler(message, process_drugs)


def process_drugs(message):
    drugs = {"ST": "Symbicort Turbuhaler", "S": "Salbutamol", "RE": "Relvar Ellipta", "P": "Pulmicort"}
    drug = message.text
    new_data[drugs[drug]] = 1
    bot.send_message(message.chat.id, f"Thank you! Your data is: {new_data}")

    new_df = pd.DataFrame(new_data, index=[data.index[-1] + 1])
    new_df = data.append(new_df)

    new_df.to_excel("peak_flow_metry_new.xlsx")


if __name__ == "__main__":
    bot.polling(non_stop=True)
    app.run(debug=True)

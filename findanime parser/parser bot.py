import requests
import pprint
import telebot
import time
import pickle
import random

with open('report.txt', mode='rb') as f:
    info = pickle.load(f)

TOKEN = 'Ваш токен'

url = f'https://api.telegram.org/bot{TOKEN}/getMe'

# Иногда прокси надо менять, чтобы код работал
proxy ={
     'http': 'http//:8.222.249.190:80'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
          }

telebot.apihelper.proxy = {'http': 'http//:8.222.249.190:80'}

bot = telebot.TeleBot(TOKEN)

results = requests.get(url, headers=headers, proxies=proxy)

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'



while True:
    time.sleep(5)
    results = requests.get(url, headers=headers, proxies=proxy)

    pprint.pprint(results.json())

    @bot.message_handler(commands=['help'])
    def show_commands(message):
        text = ''
        for i in bot.get_my_commands():
            text += str(i.command) + ' — ' + str(i.description) + '\n'
        bot.send_message(message.chat.id, text=text)


    @bot.message_handler(commands=['start'])
    def random(message):
        r_index = random.randint(0, 8325)
        text =f'Название:\n{info[r_index][0]}\n\nОписание:\n{info[r_index][1]}\n\nСсылка:\n{info[r_index][2]}'
        bot.send_message(message.chat.id, text=text)

    bot.polling()


import telebot as TB
import botconfig
import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)

bot = TB.TeleBot(botconfig.token)
logging.info("Бот стартовал")

#приветствуем пользователя
@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id,f"Привет! \n Ты выбрал /start")
    bot.send_message(message.chat.id,f"Это простой эхобот \n Отправь любое сообщение и получишь его в ответ")

#эхуем последнее сообщение
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id,message.text)

bot.infinity_polling()

def main():
    hello_message()
    echo()

if __name__ == "__main__":
    main()

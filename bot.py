import telebot as TB
import botconfig
import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)

bot = TB.TeleBot(botconfig.token)


@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id,f"Привет! \n Ты выбрал /start")
    bot.send_message(message.chat.id,f"Это простой эхобот \n Отправь любое сообщение и получишь его в ответ")


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id,message.text)

bot.infinity_polling()

def main():
    
    logging.info("Бот стартовал")
    hello_message()
    echo()

#приветствуем пользователя


#эхуем последнее сообщение
    

    

if __name__ == "__main__":
    main()

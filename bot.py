import telebot as TB
import botconfig

#logging.basicConfig(filename='bot.log', level=logging.INFO)
def main():
    bot = TB.TeleBot(botconfig.token)
    with open(u'bot.log.','a') as f:
        f.write ('Бот стартовал')
        f.close()
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

if __name__ == "__main__":
    main()

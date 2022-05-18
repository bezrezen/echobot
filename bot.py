import telebot as TB
import botconfig
import logging
import ephem
from datetime import datetime

logging.basicConfig(filename="bot.log", level=logging.INFO)

bot = TB.TeleBot(botconfig.token)

logging.info("Бот стартовал")


@bot.message_handler(commands=["start"])
def main_func(message):
    bot.send_message(
        message.chat.id,
        f"Смотри, что я умею:\n/echo\nвключает эхобот\n/planet\nскажет в каком созвездии сегодня находится выбранная планета",
    )


# приветствуем пользователя
@bot.message_handler(commands=["echo"])
def hello_message(message):
    bot.send_message(
        message.chat.id, f"Привет, {message.chat.username}! \nТы выбрал /echo"
    )
    msg = bot.send_message(
        message.chat.id,
        f'Это простой эхобот \nОтправь любое сообщение и получишь его в ответ.\nИли напиши "Стоп", если наигрался.',
    )
    bot.register_next_step_handler(msg, echo)


# эхуем последнее сообщение
def echo(message):
    if message.text != "Стоп":
        msg = bot.send_message(message.chat.id, message.text)
        bot.register_next_step_handler(msg, echo)
    else:
        bot.send_message(
            message.chat.id,
            f"Смотри, что я умею:\n/echo\nвключает эхобот\n/planet\nскажет в каком созвездии сегодня находится выбранная планета",
        )


@bot.message_handler(commands=["planet"])
def planet_const(message):
    planet_und = message.text.split(" ")[1]
    date = datetime.today().strftime("%Y/%m/%d")
    planets = {
        "Mercury": ("меркурий", "Меркурий", "mercury", "Mercury"),
        "Venus": ("венера", "Венера", "venus", "Venus"),
        "Earth": ("земля", "Земля", "earth", "Earth"),
        "Mars": ("марс", "Марс", "mars", "Mars"),
        "Jupiter": ("юпитер", "Юпитер", "jupiter", "Jupiter"),
        "Saturn": ("сатурн", "Сатурн", "saturn", "Saturn"),
        "Uranus": ("уран", "Уран", "uranus", "Uranus"),
        "Neptune": ("нептун", "Нептун", "neptune", "Neptune"),
    }
    #planet_und = "neptune"
    for planet, values in planets.items():
        try:
            if planet_und in values:
                planet_coord = getattr(ephem, planet)(date)
                sozvezdie = ephem.constellation(planet_coord)[1]
                constellations = {
                    "Capricornus": "Козерог",
                    "Aquarius": "Водолей",
                    "Pisces": "Рыбы",
                    "Aries": "Овен",
                    "Taurus": "Бык",
                    "Gemini": "Близнецы",
                    "Cancer": "Рак",
                    "Leo": "Лев",
                    "Virgo": "Дева",
                    "Libra": "Весы",
                    "Scorpio": "Скорпион",
                    "Ophiuchus": "Змееносец",
                    "Sagittarius": "Стрелец",
                }
                bot.send_message(
                    message.chat.id,
                    f"Сегодня {planets.get(planet)[1]} в созвездии {constellations.get(sozvezdie)}",
                )
        except AttributeError:
            bot.send_message(message.chat.id,'Земля ни в каком созвездии,бро')


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()

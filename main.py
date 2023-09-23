import telebot

# Замените 'YOUR_API_TOKEN' на свой токен API
API_TOKEN = '5427969151:AAHA6PsKQRurQQ8Z_MiFfHyW3qARDYHtTYw'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот. Отправь мне текст, и я его повторю.")

# Обработчик всех текстовых сообщений

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, f"Вы сказали: {message.text}")

if __name__ == "__main__":
    bot.polling(none_stop=True)

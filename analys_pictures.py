import os
import telebot
import speech_recognition
from pydub import AudioSegment

# ↓↓↓ Ниже нужно вставить токен, который дал BotFather при регистрации
# Пример: token = '2007628239:AAEF4ZVqLiRKG7j49EC4vaRwXjJ6DN6xng8'
token = '7289860039:AAEXNl48PihpgrJFfW1KKPxP11sHOeKOZCk'  # <<< Ваш токен

bot = telebot.TeleBot(token)

def download_file(bot, file_id):
    # Функция загрузки файла, присланного пользователем
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = file_id + file_info.file_path
    filename = filename.replace('/', '_')
    with open(filename, 'wb') as f:
        f.write(downloaded_file)
    return filename


# ↓↓↓ Пусть функция реагирует на изображения
@bot.message_handler(content_types=['photo'])
def resend_photo(message):
    # Скачиваем последний файл в списке с максимальным разрешением по file_id
    file_id = message.photo[1].file_id
    filename = download_file(bot, file_id)

    # Открываем изображение из файла с помощью функции open, 'rb' = read bytes
    image = open(filename, 'rb')

    # Отправляем изображение в чат с пользователем
    bot.send_photo(message.chat.id, image)

    # Не забываем закрыть файл
    image.close()


# Запускаем бота. Он будет работать до тех пор, пока
# работает ячейка (крутится значок слева).
# Остановим ячейку - остановится бот
bot.polling()
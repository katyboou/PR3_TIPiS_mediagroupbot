# Бот отправки медиа группы
# https://t.me/Media_Group_bot

import telebot

token = '5989008749:AAEob6K7Mmni3t-SiwZtAumFP0qxci6Mfp8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    name = f'Привет, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, name)
    list_photo_url = ['https://n1s1.elle.ru/48/7b/36/487b36300c62c5f0cb905da52aa874b4/940x627_0xc0a839a4_18087198581488362059.jpeg',
                      'https://klike.net/uploads/posts/2018-10/1539499416_1.jpg',
                      'https://wl-adme.cf.tsp.li/resize/728x/jpg/f07/720/ae50cf5c09b5273af2f24440ce.jpg']
    media_group = []
    for num, url in enumerate(list_photo_url):
        media_group.append(telebot.types.InputMediaPhoto(media = url))
    bot.send_media_group(chat_id = message.chat.id, media = media_group)


bot.polling(none_stop=True)

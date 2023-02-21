import telebot

import re

TOKEN = '5822724198:AAHADBmli7hZrH-FC6EAibVt0bz_5xVNjzs'

bot = telebot.TeleBot(TOKEN)

print("✅")

@bot.message_handler(commands=['start'])

def send_welcome(message):

    bot.reply_to(message, f"مرحباً {message.from_user.first_name}، وظيفه هذا بوت حذف اي كلمه سيئه او شتم يمكنك اضافه هذا بوت في مجموعه واضعه مشرف ويشتغل بوت")

@bot.message_handler(func=lambda message: True)

def filter_message(message):

    bad_words = ['كس', 'عير', 'نيج', 'كحبة', 'كحبه', 'بلاع', 'زب', 'شرموطة', 'شرموطه', 'ديس', '🖕', '🍆', '🍑', 'طيز', 'كسي', 'عريض', 'غبي', 'كلب', 'منيوك']

    for word in bad_words:

        if re.search(word, message.text, re.IGNORECASE):

            bot.delete_message(message.chat.id, message.message_id)

            bot.send_message(message.chat.id, f"تم حذف رسالتك لأنها تحتوي على كلمات سيئة، يرجى عدم استخدام هذه اللغة @{message.from_user.username}")

            break

bot.polling()

import telebot
from telebot import types
import ConstantsBeton

bot = telebot.TeleBot(ConstantsBeton.token)

print(bot.get_me())
def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

upd = bot.get_updates()
print(upd)
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Начать расчет пропорций и состава бетона🔢')
    bot.send_message(message.from_user.id, 'BetonCalculator v1.0.0', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Клава скрыта. /start - чтобы открыть', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Начать расчет пропорций и состава бетона🔢':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        callback_button = types.InlineKeyboardButton(text="М200/В15", callback_data="М200/В15")
        callback_button1 = types.InlineKeyboardButton(text="М250/В20", callback_data="М250/В20")
        callback_button2 = types.InlineKeyboardButton(text="М350/В25", callback_data="М350/В25")
        callback_button3 = types.InlineKeyboardButton(text="М400/В30", callback_data="М400/В30")
        callback_button4 = types.InlineKeyboardButton(text="М600/В45", callback_data="М600/В45")
        keyboard.add(callback_button, callback_button1, callback_button2, callback_button3, callback_button4)
        bot.send_message(message.from_user.id, 'Выберите марку/класс бетона',
                         reply_markup=keyboard)
@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'М200/В15':
        keyboard1 = types.InlineKeyboardMarkup(row_width=2)
        callback_button = types.InlineKeyboardButton(text="М300", callback_data="М300(М200/В15)")
        callback_button1 = types.InlineKeyboardButton(text="М400", callback_data="М400(М200/В15)")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button1, callback_button5)
        bot.edit_message_text(text='Бетон М200/В15 \n *Выберите марку цемента*',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'М250/В20':
        keyboard1 = types.InlineKeyboardMarkup(row_width=2)
        callback_button = types.InlineKeyboardButton(text="М300", callback_data="М300(М250/В20)")
        callback_button1 = types.InlineKeyboardButton(text="М400", callback_data="М400(М250/В20)")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button1, callback_button5)
        bot.edit_message_text(text='Бетон М250/В20 \n *Выберите марку цемента*',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'М350/В25':
        keyboard1 = types.InlineKeyboardMarkup(row_width=2)
        callback_button = types.InlineKeyboardButton(text="М400", callback_data="М400(М350/В25)")
        callback_button1 = types.InlineKeyboardButton(text="М500", callback_data="М500")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button1, callback_button5)
        bot.edit_message_text(text='Бетон М350/В25 \n *Выберите марку цемента*',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'М400/В30':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="М500", callback_data="М500(М400/В30)")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М400/В30 \n *Выберите марку цемента*',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'М600/В45':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="М600", callback_data="М600")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М600/В45 \n *Выберите марку цемента*',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Назад':
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        callback_button = types.InlineKeyboardButton(text="М200/В15", callback_data="М200/В15")
        callback_button1 = types.InlineKeyboardButton(text="М250/В20", callback_data="М250/В20")
        callback_button2 = types.InlineKeyboardButton(text="М350/В25", callback_data="М350/В25")
        callback_button3 = types.InlineKeyboardButton(text="М400/В30", callback_data="М400/В30")
        callback_button4 = types.InlineKeyboardButton(text="М600/В45", callback_data="М600/В45")
        keyboard.add(callback_button, callback_button1, callback_button2, callback_button3, callback_button4)
        bot.edit_message_text(text='Выберите марку/класс бетона',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard)



    if c.data == 'М300(М200/В15)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М200-М300")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М200/В15 \nЦемент марки М300',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М200-М300':
        bot.send_message(text='Бетон М200/В15 \nЦемент марки М300'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')
    if c.data == 'М400(М200/В15)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М200-М400")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М200/В15 \nЦемент марки М400',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М200-М400':
        bot.send_message(text='Бетон М200/В15 \nЦемент марки М400'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')


    # для М250


    if c.data == 'М300(М250/В20)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М250-М300")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М250/В20 \nЦемент марки М300',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М250-М300':
        bot.send_message(text='Бетон М250/В20 \nЦемент марки М300'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')
    if c.data == 'М400(М250/В20)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М250-М400")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М250/В20 \nЦемент марки М400',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М250-М400':
        bot.send_message(text='Бетон М250/В20 \nЦемент марки М400'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')


# для М350

    if c.data == 'М400(М350/В25)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М350-М400")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М350/В25 \nЦемент марки М400',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М350-М400':
        bot.send_message(text='Бетон М350/В25 \nЦемент марки М400'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')
    if c.data == 'М500':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М500")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М350/В25 \nЦемент марки М500',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М500':
        bot.send_message(text='Бетон М350/В25 \nЦемент марки М500'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')


        # для М400


  # для М400

    if c.data == 'М500(М400/В30)':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет", callback_data="Рассчет для М500(М400/В30)")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М400/В30 \nЦемент марки М500',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М500(М400/В30)':
        bot.send_message(text='Бетон М400/В30 \nЦемент марки М500'
                                   '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                                   '\nКрупный заполнитель: щебень фракции 20мм',
                              chat_id=c.message.chat.id,
                              parse_mode='markdown')


        # для М600

# для М600


    if c.data == 'М600':
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        callback_button = types.InlineKeyboardButton(text="Выполнить рассчет",
                                                     callback_data="Рассчет для М600")
        callback_button5 = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboard1.add(callback_button, callback_button5)
        bot.edit_message_text(text='Бетон М600/В45 \nЦемент марки М600',
                              chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              reply_markup=keyboard1,
                              parse_mode='markdown')
    if c.data == 'Рассчет для М600':
        bot.send_message(text='Бетон М600/В45 \nЦемент марки М600'
                              '\nМелкий заполнитель: средний песок фракции 2,0-2,5 мм'
                              '\nКрупный заполнитель: щебень фракции 20мм',
                         chat_id=c.message.chat.id,
                         parse_mode='markdown')



bot.polling(none_stop=True)
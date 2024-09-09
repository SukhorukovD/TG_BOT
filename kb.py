from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



button1 = KeyboardButton('Консультация')
button2 = KeyboardButton('Аудиоконсультация')
button3 = KeyboardButton('Разбор натальной карты')
button4 = KeyboardButton('Детская натальная карта')
button5 = KeyboardButton('Ответ на вопрос')
button6 = KeyboardButton('Совместимость')
button7 = KeyboardButton('Разбор периодов')
button8 = KeyboardButton('Финансы')
button9 = KeyboardButton('Телеграм канал')
button10 = KeyboardButton('Назад')


markup5 = ReplyKeyboardMarkup(one_time_keyboard=True).row(button1, button2, button3)
markup5.row(button4, button5, button6)
markup5.row(button7, button8, button9)
markup5.row(button10)



button_Name_Yes = KeyboardButton('Да, это я и я хочу это выбрать!')
button_Name_No = KeyboardButton ('Нет, это не мои данные(')
button_Name_Cancel = KeyboardButton('Я хочу подумать ещё')

markup = ReplyKeyboardMarkup(one_time_keyboard=True).row(button_Name_Yes, button_Name_No)
markup.row(button_Name_Cancel)



inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_kb_full1 = InlineKeyboardMarkup(row_width=2)
inline_kb_full4 = InlineKeyboardMarkup(row_width=2)
kbfull = InlineKeyboardMarkup(row_width=1)
kbfull1 = InlineKeyboardMarkup(row_width=1)


inline_btn_1 = InlineKeyboardButton('Обо мне', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Мои услуги', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Мой сайт', url = 'http://astrologyzabanova.com')
inline_btn_4 = InlineKeyboardButton('FQU', callback_data='button3')
inline_btn_5 = InlineKeyboardButton('Назад', callback_data='button4')



inline_kb_full.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4)
inline_kb_full1.add(inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full4.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_5)



btn1 = InlineKeyboardButton('Выбрать услугу', callback_data='btn1')
btn2 = InlineKeyboardButton('Вернуться ко всем услугам', callback_data='btn2')
btn3 = InlineKeyboardButton('Принять', callback_data='btn3')
btn4 = InlineKeyboardButton('Отклонить', callback_data='btn4')


kbfull.add(btn1, btn2)
kbfull1.add(btn3, btn4)



markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить свой контакт ☎️', request_contact=True))
import json
import os
from config import BOT_TOKEN, MY_TOKEN
#Импортируются свои баблиотеки

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import kb
#Импортируются сторонние библиотеки

bot = Bot(token=BOT_TOKEN)
my = MY_TOKEN
dp = Dispatcher(bot)


with open("client.txt", "r", encoding="utf-8") as file:
    #Открывает файл с клиентами, проверяет файл на пустоту
    if os.stat("client.txt").st_size != 0:
        client_dict = json.load(file)
    else:
        client_dict = {}



@dp.message_handler(commands=['start'])
#Триггерится командой /start
async def process_command_strt(message: types.Message):
    with open("main.jpg", 'rb') as photo_main:
        with open("main.txt", "r", encoding="utf-8") as file:
            txt = file.read()
            await bot.send_photo(message.chat.id, photo_main, caption = txt, reply_markup = kb.inline_kb_full)


@dp.message_handler(commands=['help'])
#Триггерится командой /help
async def process_command_help(message: types.Message):
    if str(message.from_user.id) == my:
        await bot.send_message(message.from_user.id, "Для того, чтобы изменить фото или текст обратитесь к команде <</replacement>>")


@dp.message_handler(commands=['replacement'])
#Триггерится командой /replacement
async def process_command_replacement(message: types.Message):
    if str(message.from_user.id) == my:
        #id админа
        await bot.send_message(message.from_user.id, "Чтобы изменить текст, загрузите новый файл txt с существующим названием\n\n" +
                               "Чтобы изменить фото, загрузите новый файл jpg с существующим названием\n\n" +
                               'us - чтобы изменить файл <<Обо мне>>\n' +
                               'тариф - чтобы изменить файл <<Мои услуги>>\n' +
                               'Консультация - чтобы изменить файл <<Консультация>>\n' +
                               'Аудиоконсультация - чтобы изменить файл <<Аудиоконсультация>>\n' +
                               'Разбор натальной карты - чтобы изменить файл <<Разбор натальной карты>>\n' +
                               'Детская натальная карта - чтобы изменить файл <<Детская натальная карта>>\n' +
                               'Ответ на вопрос - чтобы изменить файл <<Ответ на вопрос>>\n' +
                               'Совместимость - чтобы изменить файл <<Совместимость>>\n' +
                               'Разбор периодов - чтобы изменить файл <<Разбор периодов>>\n' +
                               'Финансы - чтобы изменить файл <<Финансы>>\n' +
                               'Телеграм канал - чтобы изменить файл <<Телеграм канал>>\n' +
                               'main - чтобы изменить файл <<Здравствуйте. Я - Ваш личный астролог>>\n' +
                               'FQU - чтобы изменить файл <<FQU>>\n')


@dp.message_handler(content_types=['photo'])
#Триггерится на отправку фото
async def replacement_photo(message: types.Message):
    if str(message.from_user.id) == my:
        #id админа, роизводится проверка на право менять информацию
        spisok_photo = ['us', 'main', 'fqu', 'тариф', 'консультация', 'аудиоконсультация', 'разбор натальной карты', 'детская натальная карта',
              'ответ на вопрос', 'совместимость', 'разбор периодов', 'финансы', 'телеграм канал']
        if message.caption.lower() in spisok_photo:
            file = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
            file_path = file.file_path
            await bot.download_file(file_path, message.caption.capitalize() + '.jpg')
            #Заменяет старое фото на новое под тем же именем
        else:
            await message.answer('Введено неверное имя файла')
    else:
        await message.answer('Очень красиво)')


@dp.message_handler(content_types=['document'])
#Триггерится на отправку документа
async def replacement_txt(message: types.Message):
    if str(message.from_user.id) == my:
        #id админа, роизводится проверка на право менять информацию
        spisok_txt = ['us.txt', 'main.txt', 'fqu.txt', 'тариф.txt', 'консультация.txt', 'аудиоконсультация.txt',
                      'разбор натальной карты.txt', 'детская натальная карта.txt', 'ответ на вопрос.txt',
                      'совместимость.txt', 'разбор периодов.txt', 'финансы.txt', 'телеграм канал.txt']
        if message.document.file_name.lower() in spisok_txt:
            file = await bot.get_file(message.document.file_id)
            file_path = file.file_path
            await bot.download_file(file_path, message.document.file_name.capitalize())
            #Заменяет старое фото на новое под тем же именем
        else:
            await message.answer('Введено неверное имя файла')
    else:
        await message.answer('Зачитаться можно)')



@dp.callback_query_handler(lambda c: c.data == 'button1')
#Триггерится кнопкой "Обо мне"
async def process_callback_button1(callback_query: types.CallbackQuery):
    with open("us.jpg", 'rb') as photo_us:
        with open("us.txt", "r", encoding="utf-8") as file:
            txt = file.read()
        await bot.send_photo(callback_query.message.chat.id, photo_us, caption = txt, reply_markup=kb.inline_kb_full1)
        await callback_query.answer()
        file.close()


@dp.callback_query_handler(lambda c: c.data == 'button2' or c.data == 'btn2')
#Триггерится кнопкой "Мои услуги" или кнопкой "Вернуться ко всем услугам"
async def process_callback_button2(callback_query: types.CallbackQuery):
    with open("тариф.jpg", 'rb') as photo_tarif:
        await bot.send_photo(callback_query.message.chat.id, photo_tarif, 'Можете выбрать какую-то услугу', reply_markup=kb.markup5)
        await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'button3')
#Триггерится кнопкой "FQU"
async def process_callback_button3(callback_query: types.CallbackQuery):
    with open("FQU.jpg", 'rb') as photo_FQU:
        with open("FQU.txt", "r", encoding="utf-8") as file:
            FQU = file.read()
            await bot.send_photo(callback_query.message.chat.id, photo_FQU, caption=FQU, reply_markup=kb.inline_kb_full4)
            await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'button4')
#Триггерится кнопкой "Назад"
async def process_callback_button4(callback_query: types.CallbackQuery):
    with open("main.jpg", 'rb') as photo_main:
        with open("main.txt", "r", encoding="utf-8") as file:
            txt = file.read()
            await bot.send_photo(callback_query.message.chat.id, photo_main, caption=txt, reply_markup=kb.inline_kb_full)
            await callback_query.answer()


@dp.callback_query_handler(lambda c: c.data == 'btn1')
#Триггерится кнопкой "Выбрать услугу"
async def process_callback_btn1(callback_query: types.CallbackQuery):
    global client_dict
    text = 'Простите, произошел сбой, выберите услугу еще раз'
    if 'Service' in client_dict[str(callback_query.from_user.id)].keys():
        text = 'Выбрать услугу ' + client_dict[str(callback_query.from_user.id)]['Service']
    await bot.send_message(callback_query.message.chat.id, text=text, reply_markup=kb.markup_request)
    await callback_query.answer()



@dp.message_handler(lambda message: message.text)
#Основная часть программы, триггерится любым сообщением кроме фото и документов
@dp.message_handler(content_types= ['contact'])
#Триггерится отправлением контакта
async def main(message: types.Message):
    global client_dict
    spisok = ['Консультация', 'Аудиоконсультация', 'Разбор натальной карты', 'Детская натальная карта',
              'Ответ на вопрос', 'Совместимость', 'Разбор периодов', 'Финансы', 'Телеграм канал']

    if message.text == None:
        #Заходит в цикл, если сообщение от пользователя является контактом

        client_dict[str(message.from_user.id)]['№'] = message.contact.phone_number
        client_dict[str(message.from_user.id)]['to_Name'] = 'Yes'
        with open("client.txt", "w", encoding="utf-8") as client_db:
            json.dump(client_dict, client_db)
            #Сохраняет данные пользователя в файле

        await message.reply("Введите свои ФИО")

    elif message.text in spisok:
        #Заходит в цикл если выбрана услуга из списка услуг
        if str(message.from_user.id) not in client_dict.keys():
            #Проверяет, есть ли уже клиент с таким id
            client_dict[str(message.from_user.id)] = {'Service': message.text}
            #Записывает данные пользователя в словарь
        else:
            client_dict[str(message.from_user.id)]['Service'] = message.text
            #Обновляет данные пользователя в словаре
        if 'to_Name' in client_dict[str(message.from_user.id)].keys():
            client_dict[str(message.from_user.id)]['to_Name'] = 'No'
        with open("client.txt", "w", encoding="utf-8") as client_db:
            json.dump(client_dict, client_db)
            #Сохраняет данные пользователя в файле

        with open(message.text+ ".txt", "r", encoding="utf-8") as file:
            txt = file.read()
        pho = '' + message.text+ '.jpg'
        with open(pho, 'rb') as photo:
            await bot.send_photo(message.chat.id, photo, caption = txt, reply_markup=kb.kbfull)
            #Отправляет фото и текст выбраной услуги и добавляет клавиатуру "kbfull"

    elif str(message.from_user.id) in client_dict.keys() and ('to_Name' in client_dict[str(message.from_user.id)].keys()) and (client_dict[str(message.from_user.id)]['to_Name'] == 'Yes'):
        #Заходит в цикл только один раз после отправки контакта

        client_dict[str(message.from_user.id)]['Name'] = message.text
        client_dict[str(message.from_user.id)]['to_Name'] = 'No'
        with open("client.txt", "w", encoding="utf-8") as client_db:
            json.dump(client_dict, client_db)
            #Сохраняет данные пользователя в файле

        text = 'Ваши данные:\n' + 'ФИО - ' + client_dict[str(message.from_user.id)]['Name'] + '\n' + 'Услуга - ' + \
               client_dict[str(message.from_user.id)]['Service'] + '\n' + 'Ваш номер - ' + \
               client_dict[str(message.from_user.id)]['№']
        #Отправляет клиенту запрос на подтверждение информации
        await bot.send_message(message.from_user.id, text=text, reply_markup=kb.markup)

        if message.from_user.username == None:
            await bot.send_message(message.from_user.id, 'Важно! Если Вы подтверждаете выбор, удостоверьтесь в том, '
                                                         'что у Вас не включен режим приватности, '
                                                         'и Вас можно будет найти по номеру')

    elif message.text == 'Да, это я и я хочу это выбрать!':
        #Заходит в цикл если клиент подтвердил информацию
        #Записывает в переменные значения словаря
        first_tg_name = 'Имя пользователя в телеграм - ' + message.from_user.first_name + '\n'
        phone_number = 'Номер телефона - ' + client_dict[str(message.from_user.id)]['№'] + '\n'
        first_name = 'ФИО - ' + client_dict[str(message.from_user.id)]['Name'] + '\n'
        last_name = 'Услуга- ' + client_dict[str(message.from_user.id)]['Service'] + '\n'

        if message.from_user.username == None:
            #Проверяет есть ли username у пользователя
            to_me = last_name + first_name + phone_number + first_tg_name
        else:
            user_name = 'Ссылка на профиль пользователя - @' + message.from_user.username
            to_me = last_name + first_name + phone_number + first_tg_name + user_name

        await bot.send_message(my, to_me)
        await bot.send_message(message.chat.id, 'Спасибо за Ваш выбор) Я свяжусь с Вами совсем скоро. '
                                                'Можете также взгянуть на другие услуги)', reply_markup=kb.markup5)

    elif message.text ==  'Нет, это не мои данные(':
        #Заходит в цикл если клиент отклонил информацию, предлагает выбрать что то ещё
        with open("тариф.jpg", 'rb') as photo_tarif:
            await bot.send_photo(message.chat.id, photo_tarif, 'Можете выбрать какую-то услугу', reply_markup=kb.markup5)

    elif message.text ==  'Я хочу подумать ещё':
        #Заходит в цикл если клиент передумал, возвращает клиента на старт
        with open("main.jpg", 'rb') as photo_main:
            await bot.send_photo(message.chat.id, photo_main, "Хорошо) Буду ждать. Я всегда Вам рада.", reply_markup=kb.inline_kb_full)

    elif message.text == 'Назад':
        #Заходит в цикл если нажата кнопка "Назад"
        with open("main.jpg", 'rb') as photo_main:
            with open("main.txt", "r", encoding="utf-8") as file:
                txt = file.read()
                await bot.send_photo(message.chat.id, photo_main, caption=txt, reply_markup=kb.inline_kb_full)

    else:
        #Заходит в цикл, если отправленное никуда не подошло
        await bot.send_message(message.chat.id, 'Такой услуги нет')



if __name__ == '__main__':
    #Запускает бота
    executor.start_polling(dp)
import telebot
import random
import datetime
from pytz import timezone
from datetime import datetime

bot = telebot.TeleBot('1207806133:AAHlgaNF38ZBGtRSNlklsHEF07urjtHUf1s')

A = {'я' : 'смотрящий'}

a = ['блатной👊', 'блатной👊', 'блатной👊', 'блатной👊', 'блатной👊',
     'отрицала🙅', 'фраер😎', 'фраер😎', 'фраер😎', 'фраер😎', 'фраер😎',
     'отрицала🙅', 'отрицала🙅', 'отрицала🙅', 'отрицала🙅', 'мужик🙎',
     'фраер😎', 'фраер😎', 'фраер😎', 'фраер😎', 'фраер😎', 'жмур⚰️',
     'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'подпетушник🐓',
     'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎',
     'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'мужик🙎', 'шерстяной',
     'мужик🙎', 'мужик🙎', 'чепушило', 'президент параши🚽', 'залётный🏃',
     'шнырь', 'барыга💸', 'гастролёр🎪', 'коцаный', 'лепила👨', 'сучила',
     'терпила😢', 'козёл🐐', 'чухан', 'крысяра🐀' , 'шестёрка', 'чёрт👿', 'петушара🐓',
     'главпетух🐔', 'вафлёр👅', 'водолаз💨', 'малолетка👶', 'король чуханов👑']

c = ['короче', 'по ходу', 'по жизни', 'то выходит', 'у нас',  'настоящий', 'то', 'по масти',
     'то бишь', 'одним словом', 'с головы до ног', 'натуральный', 'чисто', 'без базара']


cit = ['Люби меня как роза воду, а я тебя как вор свободу',
        'Смотри с кем воруешь, может с ним и сидеть',
        'Ворам власти, мусорам по пасти',
        'Бог создал вора, а чёрт прокурора',
        'Дай бог двух сыновей, одного - вора, второго - прокурора,'+'\n'+'Чтоб один воровал, а другой прикрывал',
        'Не плачь отец, что сын твой вор, '+'\n'+'пусть плачет тот, чей сын козёл',
        'Всегда найдутся суки среди тех, кто жмут руки, '+'\n'+'всегда найдутся бляди,что ударят сзади.',
        'От всей души, для всей братвы,'+'\n'+'кому не чуждо ВОРОВСКОЕ!'+'\n'+'Здоровья, фарта, пацаны,'+'\n'+'за вас, за нас, за все людское',
        'Главный в зоне - Вор в законе!!!',
        'Любить Бандита - Это гордость ,'+'\n'+'Забыть Бандита - Это подолость , '+'\n'+'А быть с Бандитом - это честь, '+'\n'+'Что не у каждой бабы есть',
        'Я за слова свои в ответе строгом, '+'\n'+'А за грехи свои отвечу только перед Богом',
        'Быть-добру, жизнь Ворам! '+'\n'+'В рот мента, смерть Блядям!!!',
        'Я воровское уважаю, '+'\n'+'А мусорское презираю, '+'\n'+'Пусть мент вора не закрывает, '+'\n'+'А Вор живет и процветает',
        'Воровство не преступление, '+'\n'+'а Божье наставление.',
        '♣ ♣живу - грешу, '+'\n'+'умру - отвечу♣',
        'Жизнь ворам, хуй мусорам',
        'Свети ворам а не ментам, пол жизни здесь пол жизни там',
        'Вору дай хоть миллион, он воровать не перестанет',
        'Шагая весело по жизни, клопа дави и масть держи',]




d = datetime.now(timezone('Europe/Moscow')).day
b = 'А В ХАТЕ НЫНЧЕ:️' + '\n' + '\n'

citstr = '📝МАЛЯВА ДНЯ:'+'\n' + '\n' + random.choice(cit)



@bot.message_handler(commands=['slovit_mast'])
def start_message(message):
    global A
    global d
    global citstr
    if d == datetime.now(timezone('Europe/Moscow')).day:
        if message.from_user.first_name not in A:
            A[message.from_user.first_name] = random.choice(a)
            bot.send_message(message.chat.id, message.from_user.first_name + ' ' + random.choice(c) + ' ' + A[message.from_user.first_name])
        else:
            bot.send_message(message.chat.id, message.from_user.first_name + ', я те повторяю, ты ' + A[message.from_user.first_name] + ' по жизни.')
    else:
        d = datetime.now(timezone('Europe/Moscow')).day
        A = {'я' : 'смотрящий'}
        A[message.from_user.first_name] = random.choice(a)
        bot.send_message(message.chat.id, message.from_user.first_name + ' ' + random.choice(c) + ' ' + A[message.from_user.first_name])
        citstr = '📝МАЛЯВА ДНЯ:'+'\n' + '\n' + random.choice(cit)


@bot.message_handler(commands=['kto_v_hate'])
def start_message(message):
    global d
    global b
    if d == datetime.now(timezone('Europe/Moscow')).day:
        for i in A:
            b += A[i] + ' ' + i + '\n'
        bot.send_message(message.chat.id, b)
        b = 'А В ХАТЕ НЫНЧЕ:️' + '\n' + '\n'
    else:
        bot.send_message(message.chat.id, 'Я один тут чалюсь.')




@bot.message_handler(commands=['citata'])
def start_message(message):
    if d == datetime.now(timezone('Europe/Moscow')).day:
        bot.send_message(message.chat.id, citstr)
    else:
        bot.send_message(message.chat.id, 'Чё? В пустую хату царапать собрался?')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'О новичок пожаловал... Узнай, кем сам будешь /slovit_mast, а c кем чалиться придётся /kto_v_hate. Или гляди, что братва ровная по понятиям трёт /citata. Здоровья близким и по воле фарта. АУЕ.')






bot.polling(none_stop=True, interval=0)

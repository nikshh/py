import telebot

bot = telebot.TeleBot("TOKEN", parse_mode='HTML')

def start_message(message):
    #message.text = '/start {id}' <- есть пробел
    if " " in message.text: #проверяем пробел
        refferer_candidate = message.text.split()[1] #любимый сплит
        
        try:
            refferer_candidate = int(refferer_candidate) #если в ссылке не INT
            
            if message.from_user.id != refferer_candidate: #если рефер пригласил сам себя
                refferer = refferer_candidate #рефер и id разные люди
                #...запись в бд...
        except Exception:
            pass

def my_link(message):
    bot.send_message(message.chat.id,
                     f'https://t.me/<BOT_NAME>?start={message.from_user.id}')


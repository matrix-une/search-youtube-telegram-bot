import time 
from telepot.loop import MessageLoop
from config import *

###AQUI DEFIMOS O TOKEN DO NOSSO BOT###
###O TOKEN ESTÁ NO ARQUIVO CONFIG###


###AQUI ESTA A HANDLE DO NOSSO CODE!###
###JUNTAMENTE COM ALGUMAS VARIAVEIS IMPORTANTES###
def handle(msg):
    text = msg['text']
    first_name = msg['from']['first_name']
    user_id = msg['from']['id']
    username = '@' + msg['from']['username']
    chat_id = msg['chat']['id']

    if text == '/start':
        bot.sendMessage(chat_id, f'Olá {first_name}')


###ESSE LOOP E DEFINIDO PARA QUE NOSSO BOT FIQUE ONLINE!###
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)

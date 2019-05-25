from config import *
import time 
from telepot.loop import MessageLoop

###ALGUMAS FUNCÕES###
def search_yt(query):
    url_base = "https://www.youtube.com/results"
    url_yt = "https://www.youtube.com"
    r = requests.get(url_base, params=dict(search_query=query))
    page = r.text
    soup = BeautifulSoup(page, "html.parser")
    id_url = None
    list_videos = []
    for link in soup.find_all('a'):
        url = link.get('href')
        title = link.get('title')
        if url.startswith("/watch") and (id_url != url) and (title is not None):
            id_url = url
            dic = {'title': title, 'url': url_yt + url}
            list_videos.append(dic)
        else:
            pass
    return list_videos

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
    else:
        pass

    if msg['text'].startswith('/yt '):
            try:
                res = search_yt(msg['text'][4:])
                vids = ''
                for num, i in enumerate(res):
                    vids += '{}: <a href="{}">{}</a>\n'.format(num + 1, i['url'], i['title'])
            except IndexError:
                vids = "Nenhum resultado foi encontrado"

            bot.sendMessage(msg['chat']['id'], vids, 'HTML',
                            reply_to_message_id=msg['message_id'],
                            disable_web_page_preview=True)
            return True


###ESSE LOOP E DEFINIDO PARA QUE NOSSO BOT FIQUE ONLINE!###
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)

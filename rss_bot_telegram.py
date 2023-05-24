import feedparser
import requests
import logging
import schedule
import time
import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot_token = "COLE AQUI O TOKEN DO BOT DO TELEGRAM"

#URL de feed RSS de OLiberal.com IA
rss_url = "COLE AQUI A URL DO RSS"

session = requests.Session()

sent_news = []

# cria o nome do arquivo de notícias postadas
now = datetime.datetime.now()
file_name = f"log_noticias_postadas-{now.day}-{now.month}-{now.year}.txt"

try:
    # abre o arquivo de notícias postadas para leitura
    with open(file_name, "r") as f:
        sent_news = f.read().splitlines()
except FileNotFoundError:
    # cria o arquivo de notícias postadas
    open(file_name, "w").close()

# enviar mensagens utilizando o bot para um chat específico
def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        session.post(url, data=data)
    except Exception as e:
        logger.error(f"Erro no sendMessage: {e}")

# adiciona a nova notícia ao arquivo de notícias postadas
def add_to_sent_news(link):
    with open(file_name, "a") as f:
        f.write(f"{link}\n")

# id do grupo ou canal que será enviado as mensagens
chat_id = "COLE AQUI O ID DO GRUPO DO TELEGRAM ONDE O BOT VAI ENVIAR AS NOTICIAS"

def send_news(token, chat_id, rss_url):
    feed = feedparser.parse(rss_url)
    for entry in feed.entries[:1]: 
        title = entry.title
        link = entry.link
        message = f"{title}. - notícia via oliberal.com\n\n{link}"
        with open(file_name, "r") as f:
            sent_news = f.read().splitlines()
            # verifica se o link da notícia já foi enviada
            if link not in sent_news:
                send_message(token, chat_id, message)
                add_to_sent_news(link)
            else:
                logger.debug("Notícia já enviada, ignorando...")


#define a periodicidade de envio de notícias.
schedule.every(1).minutes.do(send_news, bot_token, chat_id, rss_url)

#Função para criar um novo arquivo de notícias postadas a cada 15 dias:
def create_new_file():
    global file_name, sent_news
    now = datetime.datetime.now()
    file_name = f"log_noticias_postadas-{now.day}-{now.month}-{now.year}.txt"
    open(file_name, "w").close()
    sent_news = []


#define a periodicidade de criação de novo arquivo de notícias postadas
schedule.every(15).days.do(create_new_file)


while True:
    schedule.run_pending()
    time.sleep(1)
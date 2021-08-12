
import requests
import random
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.update import Update
from settings import *
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 5000))


root_url = "https://gnews.io/api/v4/top-headlines?country=in&lang=en"

def start(update: Update, context):
    # send a welcome message when /start command is issued
    welcome_text = "Welcome to instant news bot.\nType in a topic name to get latest news about that topic.\nUse /help to know more"
    update.message.reply_text(welcome_text)



def error(update, context):
    logger.warning('Update {} caused error {}'.format(update, context.error))

def business(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'business', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting business related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def sports(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'sports', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting sports related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def education(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'education', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting education related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def technology(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'technology', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting tech related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def covid(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'covid', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting covid related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def entertainment(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'entertainment', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting entertainment related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def random_query(update, context):
    query = update.message.text
    query.lower()
    url = '{}&q={}&token={}'.format(root_url, query, api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting {} related news...\n{}'.format(query, result))
    except:
        update.message.reply_text('no articles available')

def politics(update, context):
    url = '{}&category={}&token={}'.format(root_url, 'covid', api_key)
    try:

        contents = requests.get(url).json()
        num_articles = len(contents['articles'])
        rand_ind = random.randint(0, num_articles - 1)
        source = contents['articles'][rand_ind]['source']['name']
        title = contents['articles'][rand_ind]['title']
        descr = contents['articles'][rand_ind]['description']
        link = contents['articles'][rand_ind]['url']
        result = "Source: {}\nTitle: {}\nDescription: {}\nLink: {}".format(source, title, descr, link)
        update.message.reply_text('Getting politics related news...\n{}'.format(result))
    except:
        update.message.reply_text('no articles available')

def help(update, context):
    help_text = """Type in your query to get news related to that topic.\nYou can also use these commands to get related news about that topic\n
    /business - To get Business news\n
    /technology - To get Technology news\n
    /politics - To get Politics news\n
    /education - To get Education news\n
    /sports - To get Sports news\n
    /covid - To get Covid news\n
    /entertainment - To get Entertainment news\n
    """

    update.message.reply_text(help_text)




def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_error_handler(error)
    dp.add_handler(CommandHandler('business', business))
    dp.add_handler(CommandHandler('sports', sports))
    dp.add_handler(CommandHandler('education', education))
    dp.add_handler(CommandHandler('technology', technology))
    dp.add_handler(CommandHandler('covid', covid))
    dp.add_handler(CommandHandler('entertainment', entertainment))
    dp.add_handler(MessageHandler(Filters.text, random_query))
    dp.add_handler(CommandHandler('politics', politics))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://instant-news.herokuapp.com/' + TOKEN)
    # updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()
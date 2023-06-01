#Importing the libraries
import environ
import telebot


#Reading enviroment variables
env = environ.Env()
environ.Env().read_env()

TOKEN = env('BOT_TOKEN')


#Creating the bot
bot = telebot.TeleBot(TOKEN)


#Creating the function to handle initial messages
@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, how are you doing?")


bot.infinity_polling()
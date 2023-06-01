#Importing the libraries
import environ
import telebot


#Reading enviroment variables
env = environ.Env()
environ.Env().read_env()

TOKEN = env('BOT_TOKEN')
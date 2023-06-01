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

#Creating the function to handle expenses messages
@bot.message_handler(commands=['expense'])
def handle_income(message):
    # Get the message text
    message_text = message.text
    user = message.from_user  # Get the User object
    user_id = user.id  # Retrieve the user ID

    # Remove the "/income" part from the message text
    message_text = message_text.replace("/expense ", "").strip()

    # Split the message text by commas
    values = message_text.split(',')

    if len(values) == 4:
        date = values[0].strip()  # Extract the date value from the first element of the values list
        amount = float(values[1].strip())
        category = values[2].strip()
        subcategory = values[3].strip()

        # Reply to the user
        reply = f"Expense recorded:\nDate: {date}\nAmount: ${amount}\nCategory: {category}\nSubcategory: {subcategory}"
        bot.reply_to(message, reply)
        reply_2 = f"Your user ID is: {user_id}"
        bot.reply_to(message,reply_2)
    else:
        bot.reply_to(message, "Invalid format. Please provide date, amount, category, and subcategory separated by commas.")


bot.infinity_polling()
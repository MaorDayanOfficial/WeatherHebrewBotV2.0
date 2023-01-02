import requests
from telegram.bot import Bot
import schedule
import time
import datetime

# Replace YOUR_OPENWEATHER_API_KEY with your actual OpenWeather API key
OPENWEATHER_API_KEY = "replace"

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram bot token
TELEGRAM_BOT_TOKEN = "replace"

# Replace YOUR_CHAT_ID with your actual chat ID
YOUR_CHAT_ID = "replace"

def send_weather_message(city):
    # Send a request to the OpenWeather API to get the current weather in the specified city
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}")

    # Check if the request was successful
    if response.status_code != 200:
        # Use the Telegram bot to send a message if the weather data cannot be retrieved
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(
            chat_id=YOUR_CHAT_ID,
            text=f"מידע לגבי מזג האוויר בעיר {city} אינו זמין כרגע. תקלה בטיפול."
        )
    else:
        # Get the current temperature from the API response
        temperature = response.json()["main"]["temp"]

        # Convert the temperature from Kelvin to Celsius
        temperature = round(temperature - 273.15)

        # Get the current hour
        current_hour = datetime.datetime.now().hour

        # Set the greeting message based on the current hour
        if current_hour >= 6 and current_hour < 12:
            greeting = "בוקר טוב!"
        elif current_hour >= 12 and current_hour < 18:
            greeting = "אחר הצהריים טובים!"
        elif current_hour >= 18 and current_hour < 22:
            greeting = "ערב טוב!"
        else:
            greeting = "לילה טוב!"

        # Use the Telegram bot to send a message with the current weather
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(
            chat_id=YOUR_CHAT_ID,
            text=f"{greeting} הטמפרטורה הנוכחית בעיר {city} היא {temperature}°C"
        )

# Define a list of cities to get the weather data for
cities = ["תל אביב", "ירושלים", "לוד", "באר שבע", "בית שאן", "אשדוד", "אילת", "חיפה", "טבריה", "קריית שמונה"]

# Schedule the function to run every hour for each city in the list
for city in cities:
    schedule.every().day.at("00:00:00").do(send_weather_message, city)
    schedule.every().day.at("01:00:00").do(send_weather_message, city)
    schedule.every().day.at("02:00:00").do(send_weather_message, city)
    schedule.every().day.at("03:00:00").do(send_weather_message, city)
    schedule.every().day.at("04:00:00").do(send_weather_message, city)
    schedule.every().day.at("05:00:00").do(send_weather_message, city)
    schedule.every().day.at("06:00:00").do(send_weather_message, city)
    schedule.every().day.at("07:00:00").do(send_weather_message, city)
    schedule.every().day.at("08:00:00").do(send_weather_message, city)
    schedule.every().day.at("09:00:00").do(send_weather_message, city)
    schedule.every().day.at("10:00:00").do(send_weather_message, city)
    schedule.every().day.at("11:00:00").do(send_weather_message, city)
    schedule.every().day.at("12:00:00").do(send_weather_message, city)
    schedule.every().day.at("13:00:00").do(send_weather_message, city)
    schedule.every().day.at("14:00:00").do(send_weather_message, city)
    schedule.every().day.at("15:00:00").do(send_weather_message, city)
    schedule.every().day.at("16:00:00").do(send_weather_message, city)
    schedule.every().day.at("17:00:00").do(send_weather_message, city)
    schedule.every().day.at("18:00:00").do(send_weather_message, city)
    schedule.every().day.at("19:00:00").do(send_weather_message, city)
    schedule.every().day.at("20:00:00").do(send_weather_message, city)
    schedule.every().day.at("21:00:00").do(send_weather_message, city)
    schedule.every().day.at("22:00:00").do(send_weather_message, city)
    schedule.every().day.at("23:00:00").do(send_weather_message, city)

    # Run the function in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)


    #MaorDayan all rights reservered you may use and change 

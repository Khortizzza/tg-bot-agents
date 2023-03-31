import requests
from bs4 import BeautifulSoup
import schedule
import time
import telegram

# Встановлюємо токен бота та ідентифікатор чату для повідомлень
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# Функція для збору даних з розділу Admins All
def get_admins_all():
    # Задаємо URL сторінки з розділом Admins All
    url = 'https://example.com/admins_all'

    # Виконуємо запит до сторінки та отримуємо її HTML-код
    response = requests.get(url)
    html = response.text

    # Розбираємо HTML-код з використанням бібліотеки BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Знаходимо всіх агентів в розділі Admins All
    agents_all = soup.select('div.agent')

    return agents_all

# Функція для відправки повідомлення в телеграм
def send_telegram_message(message):
    # Створюємо об'єкт бота
    bot = telegram.Bot(token=bot_token)
    # Відправляємо повідомлення в чат з використанням методу bot.send_message()
    bot.send_message(chat_id=chat_id, text=message)

# Функція, яка перевірятиме чергу та відправлятиме повідомлення в телеграм, якщо умова виконується
def check_queue():
    # Отримуємо список агентів з розділу Admins All
    agents_all = get_admins_all()

    # Перевіряємо кількість агентів та час дня
    current_hour = time.localtime().tm_hour
    if 10 <= current_hour < 18 and len(agents_all) < 3:
        # Збільшуємо лічильник протягом 5 хвилин
        counter = 0
        while counter < 5:
            # Почекайте 1 хвилину
            time.sleep(60)
            # Оновлюємо список агентів
            agents_all = get_admins_all()
            # Перевіряємо, чи є 2 а

 
from pyrogram import Client, filters

# Твои данные
API_ID = 28992824  # Замени на свой API ID
API_HASH = "90d4f1eaa5a901e8cfd5cdb307d1f5a9"  # Замени на свой API Hash
BOT_TOKEN = "7175805241:AAEQiJ0BEjieDmHr8u45KLM4MPnUJKV8IP0"  # Уже вставил

# Аккаунт, куда пересылать сообщения
ADMIN_USERNAME = "@KOSTYANSHK"

# Создаем бота
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Автоответ на любое сообщение
WELCOME_MESSAGE = """✨ Приветствую! Я помощник клана ISXOD! Буду рад видеть тебя в нашем клане! ✨
Заполни, пожалуйста, анкету:
🌟 1. Имя и возраст
🌟 2. Игровой ник и ID, а также скрин профиля
🌟 3. Прокачка оружия (скриншот брони и оружия)
🌟 4. В какое время по МСК обычно играешь
🌟 5. Предыдущие кланы (если нет, то прочерк)
🌟 6. Почему ты хочешь присоединиться к нашему клану?
"""

@app.on_message(filters.private & filters.text)
def reply_and_forward(client, message):
    # Отвечаем пользователю
    message.reply_text(WELCOME_MESSAGE)

    # Пересылаем админу
    forward_text = f"@{message.from_user.username} : {message.text}"
    client.send_message(ADMIN_USERNAME, forward_text)

# Запуск бота
app.run()

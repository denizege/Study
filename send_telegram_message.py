def send_telegram_message():

    api_key = "api_key"

    url = f'https://api.telegram.org/bot{api_key}/sendMessage'

    param = {
        "chat_id": chat_id,
        "text": f'Привет! Твое сообщение'
    }

    print(requests.get(url, param).json())


send_telegram_message()

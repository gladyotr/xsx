from telethon import TelegramClient

# Use your own values here
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
phone_number = '+34600000000'

assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

client = TelegramClient('anon', api_id, api_hash)
client.start()
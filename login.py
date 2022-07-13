from telethon import TelegramClient

# Use your own values here
api_id = 3456473
api_hash = 'c1ffd87a77975a9c1bc7f230b3676547'
phone_number = '+905537693079'

client = TelegramClient('anon', api_id, api_hash)
assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

client = TelegramClient('anon', api_id, api_hash)
client.start()
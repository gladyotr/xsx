from telethon.sync import TelegramClient

session_path = Path("sessions")
if not session_path.exists():
    session_path.mkdir()

phone_number = '+905537693079'
api_id = 3456473
api_hash = 'c1ffd87a77975a9c1bc7f230b3676547'
client = TelegramClient(f"sessions/{phone_number}", api_id, api_hash, proxy=proxy)


async def main():
    await client.connect()

    await client.send_code_request(f"+{phone_number}", force_sms=True)
    verification_code = get_verification_code()
    await client.sign_up(verification_code, names.get_first_name(), names.get_last_name())

    await client.disconnect()


client.loop.run_until_complete(main())



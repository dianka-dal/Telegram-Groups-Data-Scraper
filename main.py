import configparser
import json
import csv

from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 0000000
api_hash = ''
phone = ''

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

all_participants = []
all_participants = client.get_participants('')

print('Saving In file...')
with open("mm_members_list.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['User name', 'User Id'])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            continue
        writer.writerow([username, user.id])
print('Data scraped successfully.')

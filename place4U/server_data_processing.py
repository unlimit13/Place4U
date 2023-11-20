import pandas as pd
from openai import OpenAI
import time

DATABASE = 'crawling_result_top.xlsx'
GPT_KEY = "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"
CLIENT = OpenAI(
        api_key=GPT_KEY,
    )
LOCATION = "제주"

global db


# Open Database
def open_database():
    global db
    db = pd.read_excel(DATABASE, engine='openpyxl')


# Extract Location
def extract_location():
    global db
    location_list = []
    for i in range(len(db)):
        if LOCATION in str(db['caption'][i]):
            location_list.append((i, db['caption'][i]))
    return location_list


# Return Address w/ chatGPT
def return_address_w_chatgpt(client, input_message):
    USER_INPUT_MSG = input_message + "\n위의 글에서 주소만 반환해줘. 주소 정보가 없으면 NO만 반환해줘"

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": USER_INPUT_MSG}
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


# Extract Address
def extract_address(location_list):
    address_list = []
    for loc in location_list:
        address_list.append((loc[0], return_address_w_chatgpt(CLIENT, loc[1])))
        time.sleep(1)
    return address_list


# Update Database
def update_database(address_list):
    global db
    addr = []
    datas_idx = 0
    for i in range(len(db)):
        if datas_idx == len(address_list):
            break
        if i == address_list[datas_idx][0]:
            addr.append(address_list[datas_idx][1])
            datas_idx += 1
        else:
            addr.append("")
    for i in range(len(db) - len(addr)):
        addr.append('')
    db['address'] = addr
    db.to_excel(DATABASE)


if __name__ == '__main__':
    print('Open Database...', end='')
    open_database()
    print('Complete')
    print('Extract Location...', end='')
    location_list = extract_location()
    print('Complete')
    print('Total Item Size : ' + str(len(location_list)))
    print('Extract address from chatGPT...')
    address_list = extract_address(location_list)
    print('Complete')
    print('Update Database...', end='')
    update_database(address_list)
    print('Complete')
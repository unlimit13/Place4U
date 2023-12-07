from openai import OpenAI

DATABASE = 'crawling_data.csv'
GPT_KEY = "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"
CLIENT = OpenAI(
        api_key=GPT_KEY,
    )


# input_message type : string
def return_silimar_word(client, input_message):
    USER_INPUT_MSG = input_message + "를 좋아해. 내가 또 좋아할만한 음식을 하나 추천해줘. 답변은 단어로만 해줘"

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": USER_INPUT_MSG}
        ],
        model="gpt-3.5-turbo",
    )
    #print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


#input_message_list type : list
def return_silimar_word_list(client, input_message_list):
    USER_INPUT_MSG = ','.join(input_message_list) + "를 좋아해. 내가 또 좋아할만한 음식을 하나 추천해줘. 답변은 단어로만 해줘"

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": USER_INPUT_MSG}
        ],
        model="gpt-3.5-turbo",
    )
    #print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


def get_word(latest_Tag_List):
#if __name__ == '__main__':
    return_result=[]
    words = "빵, 초코우유, 라떼, 소고기, 탕후루, 자몽에이드, 아메리카노, 돼지고기, 짬뽕, 떡볶이, 피자, 스테이크, 치킨"
    #words_list = ['빵', '초코우유', '라떼', '소고기', '탕후루', '자몽에이드', '아메리카노', '돼지고기', '짬뽕', '떡볶이']
    words_list=[]
    for i in range(len(latest_Tag_List)):
        words_list.append(str(latest_Tag_List[i]).split('-')[0])
        
    result_word1 = return_silimar_word(CLIENT, words)
    return_result.append(result_word1)
    
    print(words_list)
    result_word = return_silimar_word_list(CLIENT, words_list)
    return_result.append(result_word)
    
    return return_result
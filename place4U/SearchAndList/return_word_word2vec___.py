#!pip install Okt
#!pip install gensim
#!pip install konlpy
from konlpy.tag import Okt
from gensim.models import Word2Vec

def w2v(recent_search_word, words):
    # 사용자의 태그 검색 기록 (한국어)
    words_list = []
    for word in words.split(', '):
        words_list.append(word)
    user_search_history = [words_list]

    # KoNLPy 형태소 분석기 사용 (Okt)
    okt = Okt()

    # 형태소 분석 및 토큰화
    tokenized_user_search_history = [okt.morphs(" ".join(search)) for search in user_search_history]

    # Word2Vec 모델 학습
    model = Word2Vec(sentences=tokenized_user_search_history, vector_size=20, window=2, min_count=1, workers=4)

    # 사용자의 가장 최근 검색 기록 (한국어)
    recent_search = [recent_search_word]

    # 추천할 태그의 수
    num_recommendations = 3

    # 가장 최근 검색한 태그에 대한 유사한 태그 추천
    similar_tags = model.wv.most_similar(positive=recent_search, topn=num_recommendations)
    return similar_tags[0][0]

def w2v_list(recent_search_word, words_list):
    # 사용자의 태그 검색 기록 (한국어)
    user_search_history = [words_list]

    # KoNLPy 형태소 분석기 사용 (Okt)
    okt = Okt()

    # 형태소 분석 및 토큰화
    tokenized_user_search_history = [okt.morphs(" ".join(search)) for search in user_search_history]

    # Word2Vec 모델 학습
    model = Word2Vec(sentences=tokenized_user_search_history, vector_size=20, window=2, min_count=1, workers=4)

    # 사용자의 가장 최근 검색 기록 (한국어)
    recent_search = [recent_search_word]

    # 추천할 태그의 수
    num_recommendations = 3

    # 가장 최근 검색한 태그에 대한 유사한 태그 추천
    similar_tags = model.wv.most_similar(positive=recent_search, topn=num_recommendations)
    return similar_tags[0][0]


if __name__ =="__main__":
   # words = "짬뽕, 아메리카노,아메리카노, 짜장면, 유린기, 탕수육, 삼선짜장, 삼선짬뽕, 볶음밥, 유산슬, 팔보채"
    words_list = ['짜장면','아메리카노','아메리카노',   '짬뽕']

    print(words_list)
    #recent_search_word = str(recent_search_word).split('-')[1][0:-1]
    recent_search_word = '짜장면'
    print(recent_search_word)
    '''similar_tag = w2v(recent_search_word, words)
    print(f"최근 검색 : {recent_search_word}")
    print("추천된 태그 : ", end='')
    print(similar_tag)'''
    similar_tag = w2v_list(recent_search_word, words_list)
    print(f"최근 검색 : {recent_search_word}")
    print("추천된 태그 : ", end='')
    print(similar_tag)
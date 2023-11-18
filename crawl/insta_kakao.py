from konlpy.tag import Mecab
import re
import requests

# Mecab 형태소 분석기 인스턴스 생성
mecab = Mecab()

# 해시태그에서 위치 정보 추출 함수
def extract_location_from_hashtag(hashtag):
    clean_hashtag = hashtag.strip('#')
    korean_only = re.sub("[^가-힣]", " ", clean_hashtag)
    nouns = mecab.nouns(korean_only)
    return nouns

# 카카오 맵 API를 사용한 위치 검색 함수
def kakao_map_search(query, rest_api_key):
    headers = {"Authorization": f"KakaoAK {rest_api_key}"}
    params = {"query": query}
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    response = requests.get(url, headers=headers, params=params)
    return response.json()['documents'] if response.status_code == 200 else None

# REST API 키 
REST_API_KEY = 'e529d35c1be98ff9caee1a18e3de0e2e'

# 해시태그 예시
hashtags = ['#서초커피작업실', '#소미담 대치점']

# 각 해시태그에 대한 위치 정보 검색 및 출력
for hashtag in hashtags:
    locations = extract_location_from_hashtag(hashtag)
    for location in locations:
        location_info = kakao_map_search(location, REST_API_KEY)
        if location_info:
            for place in location_info:
                print(f"Hashtag: {hashtag}")
                print(f"Extracted Keyword: {location}")
                print(f"Place Name: {place['place_name']}")
                print(f"Address: {place['address_name']}")
                print(f"Latitude: {place['y']}")
                print(f"Longitude: {place['x']}")
                print("-----------")
        else:
            print(f"Hashtag: {hashtag}, Keyword: {location}, No results found.")
            print("-----------")

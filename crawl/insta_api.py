import requests

# 액세스 토큰 및 기타 필요한 파라미터 설정
ACCESS_TOKEN = 'EAAPTZBQWNfXABOZB6y6aDWCDBlpqp4dbpRsYxxjZCrwpvzZC7o9H0BQp0QAUOCMt36pNEeOQf7SI3MxfhKjAalRGtQ6JOgZCtbrHiqZCsuBcKvc6tBe4QQBQLeV0gDY3LzvSbBIRUVr5p1so1A6bPPFgieiu2lFG9DraKZBvHQ3uR7b9ZBJCpy5OhUuH6dpqDRtIHrK5DxP2ZAcfzWkBB5BrnsGbLWLWV5u6p4XcqbEMZB76COtZAKkuWNgIZAMC5rtbI4cKmwZDZD'
USER_ID = '17841402282149254'
# HASHTAG_ID = '17841594520072102'  # 예시 해시태그 ID
LIMIT = 25
F_VERSION = 'v18.0'


# 사용자로부터 해시태그 입력받기
input_hashtag = input("Enter hashtag (without '#'): ")

def get_hashtag_id(hashtag):
    """해시태그 ID를 가져오는 함수"""
    url = f'https://graph.facebook.com/{F_VERSION}/ig_hashtag_search'
    params = {
        'user_id': USER_ID,
        'q': input_hashtag,
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()['data'][0]['id']

# 해시태그로 데이터 가져오기
def get_media(hashtag_id, after_param=None):
    """미디어 데이터를 가져오는 함수"""
    url = f'https://graph.facebook.com/{F_VERSION}/{hashtag_id}/recent_media'
    params = {
        'user_id': USER_ID,
        'fields': 'id,media_type,media_url,permalink,caption',
        'limit': LIMIT,
        'access_token': ACCESS_TOKEN
    }
    if after_param:
        params['after'] = after_param
    return requests.get(url, params=params).json()


hashtag_id = get_hashtag_id(input_hashtag) # 해시태그 ID
media_list = []  # 게시물 데이터를 저장할 리스트
after_param = None  # 페이징을 위한 파라미터
max_list = 50 # 가져올 데이터 수

# N개 게시물을 가져올 때까지 반복
while len(media_list) < max_list:
    media_data = get_media(hashtag_id, after_param)

    media_list.extend(media_data['data'])

    # 다음 페이지가 없으면 반복 중단
    if 'next' in media_data['paging']:
        after_param = media_data['paging']['cursors']['after']
    else:
        break

# 결과 출력
for media in media_list:
    print(media)



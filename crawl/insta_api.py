import requests

# 액세스 토큰 및 필요한 파라미터 설정
ACCESS_TOKEN = 'EAAPTZBQWNfXABO5mhJg1VOtWToZCQsSTLBiIIhDdvPpZA3HlOnfbhj32MSN4IuqH4iLARkmyRcaSe1lW85aGnOJgPNX0ZBd1uIt6daxAgik4ZBDw2k3tjXlMaUtbtzYt3HFpsqOrwgcs7r9hoKa1d2F56NyHaxh5Rd7lIE0mx2emEqHj2EEvEjDZBqBZBZBQaovPvI1Gr25jc8wlgAHkXZBaOWSDZCtIHCs3nU2QWTqjmWZA02xTpz1WmZADbhM1EOcr3ELNHMMZD'
FACEBOOK_PAGE_ID = '176816622176909' # 예: '176816622176909'
# USER_ID = 'YOUR_USER_ID' # 예: '17841402282149254'
LIMIT = 25
F_VERSION = 'v18.0'

# 연속 7일 동안 Instagram 비즈니스 또는 크리에이터 계정 대신 최대 30개의 고유한 해시태그를 쿼리

def get_instagram_business_id(page_id, access_token):
    """Instagram 비즈니스 계정 ID를 가져오는 함수"""
    url = f'https://graph.facebook.com/v18.0/{page_id}?fields=instagram_business_account'
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json().get('instagram_business_account', {}).get('id')

# requst: 'https://graph.facebook.com/v18.0/ig_hashtag_search?user_id=17841402282149254&q=떡볶이'
def get_hashtag_id(hashtag, instagram_business_id, access_token):
    """해시태그 ID를 가져오는 함수"""
    url = f'https://graph.facebook.com/{F_VERSION}/ig_hashtag_search'
    params = {
        'user_id': instagram_business_id,
        'q': hashtag,
        'access_token': access_token
    }
    response = requests.get(url, params=params)

    try:
        return response.json()['data'][0]['id']
    except IndexError:
        print("해시태그에 해당하는 데이터가 없습니다.")
        return None

    except KeyError:
        print("API 요청이 실패했습니다. 응답:", response.json())
        return None

def get_media(hashtag_id, instagram_business_id, access_token, limit=25, after_param=None):
    """미디어 데이터를 가져오는 함수"""
    url = f'https://graph.facebook.com/{F_VERSION}/{hashtag_id}/recent_media'
    params = {
        'user_id': instagram_business_id,
        'fields': 'id,media_type,media_url,permalink,caption,location',
        'limit': limit,
        'access_token': access_token
    }
    if after_param:
        params['after'] = after_param
    return requests.get(url, params=params).json()

# Instagram 비즈니스 계정 ID 가져오기
instagram_business_id = get_instagram_business_id(FACEBOOK_PAGE_ID, ACCESS_TOKEN)
print(f'Instagram Business ID: {instagram_business_id}')

# 사용자로부터 해시태그 입력받기
input_hashtag = input("Enter hashtag (without '#'): ")
hashtag_id = get_hashtag_id(input_hashtag, instagram_business_id, ACCESS_TOKEN) # 해시태그 ID


media_list = []  # 게시물 데이터를 저장할 리스트
after_param = None  # 페이징을 위한 파라미터
max_list = 300 # 가져올 데이터 수

# N개 게시물을 가져올 때까지 반복
while len(media_list) < max_list:
    media_data = get_media(hashtag_id, instagram_business_id, ACCESS_TOKEN, LIMIT, after_param)

    media_list.extend(media_data['data'])

    # 다음 페이지가 없으면 반복 중단
    if 'next' in media_data['paging']:
        after_param = media_data['paging']['cursors']['after']
    else:
        break

# 결과 출력
for i, media in enumerate(media_list):
    print(i)
    print(media)

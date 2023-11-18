import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'place4U.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.utils import timezone

def gptcall(caption):
    place = 0#chatgpt return
    return place

def main():
    from SearchAndList.models import searchedList,searchedTag
    file = open("crawling_data.csv",'r')
    reader = csv.reader(file)
    new_tag = searchedTag(searchedTag_text="TEST", location="동탄",pub_date=timezone.now()) #입력한 태그&위치
    new_tag.save()
    #print(new_tag.id)
    for line in reader: #태그로 검색된 모든 crawling data DB에 저장
        print(line)
        tag = searchedTag.objects.get(id=new_tag.id)
        tag.searchedlist_set.create(caption=line.caption,likes=line.like_count,place=gptcall())
    
if __name__=="__main__":
    main()

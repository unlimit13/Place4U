import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'place4U.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.utils import timezone


def main():
    from SearchAndList.models import searchedList,searchedTag
    file = open("crawling_data.csv",'r')
    reader = csv.reader(file)
    new_tag = searchedTag(searchedTag_text="TEST", location="동탄",pub_date=timezone.now())
    new_tag.save()
    for line in reader:
        print(line)
        print(new_tag.id)
        new_tag.searchedlist_set.create(caption=line,likes=line,place=line)
    
if __name__=="__main__":
    main()
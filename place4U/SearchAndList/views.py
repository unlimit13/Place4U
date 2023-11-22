from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.template import loader
from django.utils import timezone
from .models import searchedTag
from .forms import searchedTagForm,likethresholdForm

def index(request):
    
    latest_Tag_List = searchedTag.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("SearchAndList/index.html")
    context = {
        "latest_searchedTag_list" : latest_Tag_List,
    }
    __tag=0
    if request.method=='POST':
        form = searchedTagForm(request.POST)
        print(form)
        if form.is_valid():
            location = form.cleaned_data['input_location']
            print(location)
            whole_Tag_List = searchedTag.objects.filter(
                searchedTag_text=form.cleaned_data['input_tag'],searchedLocation_text=location
                )
            if len(whole_Tag_List)==0:
                tag = searchedTag()
                tag.searchedTag_text = form.cleaned_data['input_tag']
                tag.searchedLocation_text = location
                tag.pub_date = timezone.now()
                tag.save()
                __tag=tag
            else:
                whole_Tag_List[0].pub_date = timezone.now()
                #whole_Tag_List[0].location = location
                whole_Tag_List[0].save()
                __tag=whole_Tag_List[0]
            return redirect('SearchAndList:results',__tag.id,location)
           # return results(request,__tag.id,location)
            
    return render(request,"SearchAndList/index.html",context)
    #return HttpResponse(template.render(context,request))
    '''output = ", ".join([q.searchedTag_text for q in latest_Tag_List])
    return HttpResponse(output)'''

def results(request,tag_id,location):
    try:
        tag = searchedTag.objects.get(pk=tag_id)
        tag.pub_date = timezone.now()
        tag.save()
    except searchedTag.DoesNotExist:
        raise Http404("Tag does not exist")
    if request.method =='POST':
        form = likethresholdForm(request.POST)
        if form.is_valid():
            like_threshold=form.cleaned_data['input_threshold']
            return redirect('SearchAndList:filtered_results',tag.id,location,like_threshold)
    
    context = {
        "tag" : tag,
        "location" : location,
    }

    return render(request,"SearchAndList/results.html",context)
    #return HttpResponse("You're looking at Tag %s." % tag_id)
    
def filtered_results(request,tag_id,location,like_threshold):
    try:
        tag = searchedTag.objects.get(pk=tag_id)
        tag.pub_date = timezone.now()
        tag.save()
    except searchedTag.DoesNotExist:
        raise Http404("Tag does not exist")
    if request.method=='POST':
        form = likethresholdForm(request.POST)
        if form.is_valid():
            __like_threshold=form.cleaned_data['input_threshold']
            return redirect('SearchAndList:filtered_results',tag.id,location,__like_threshold)
    
    context = {
        "tag" : tag,
        "location" : location,
        "threshold" : like_threshold
    }

    return render(request,"SearchAndList/filtered_results.html",context)

def recent_results(request,tag_id):
    like_threshold=0
    try:
        tag = searchedTag.objects.get(pk=tag_id)
        tag.pub_date = timezone.now()
        tag.save()
    except searchedTag.DoesNotExist:
        raise Http404("Tag does not exist")

    if request.method =='POST':
        form = likethresholdForm(request.POST)
        if form.is_valid():
            like_threshold=form.cleaned_data['input_threshold']
            return redirect('SearchAndList:filtered_recent_results',tag.id,like_threshold)
    
    context = {
        "tag" : tag,
        "threshold" : like_threshold,
    }

    return render(request,"SearchAndList/recent_results.html",context)



def filtered_recent_results(request,tag_id,like_threshold):
    try:
        tag = searchedTag.objects.get(pk=tag_id)
        tag.pub_date = timezone.now()
        tag.save()
    except searchedTag.DoesNotExist:
        raise Http404("Tag does not exist")
    
    if request.method=='POST':
        form = likethresholdForm(request.POST)
        if form.is_valid():
            __like_threshold=form.cleaned_data['input_threshold']
            return redirect('SearchAndList:filtered_recent_results',tag.id,__like_threshold)
            
    context = {
        "tag" : tag,
        "threshold" : like_threshold,
    }

    return render(request,"SearchAndList/filtered_recent_results.html",context)



# Create your views here.
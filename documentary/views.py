# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from documentary.models import Title
from documentary.models import Author
from documentary.models import Site
from django.core.cache import cache
import requests


def paging_title(page):
    max_titles = 10
    total_titles = Title.objects.all()
    # get pages
    if (len(total_titles)%max_titles==0):
        total_pages = (len(total_titles)/max_titles)
    else:
        total_pages =(len(total_titles)/max_titles) +1

    if (page>total_pages):
        return HttpResponseRedirect('/documentary/error')

    last_page = total_pages
    # get pervious page
    if (page > 1):
        previous_page = page-1
    else:
        previous_page = 1
    # get next page
    if (page < last_page):
        next_page = page + 1
    else:
        next_page = last_page

    titles = total_titles[((page-1)*max_titles):(page*max_titles)]

    return titles, previous_page, next_page, total_pages

def get_file_path():
    return "/var/www/html/hobby/documentary/file/"

# Create your views here.
def home(request):
    page = 1
    titles, previous_page, next_page, total_pages = paging_title(page)
    return render(request,'index.html',{"titles": titles,"previous_page":previous_page,"current":page,"next_page":next_page,"total_pages":total_pages})

def index(request):
    page = 1
    titles, previous_page, next_page, total_pages = paging_title(page)
    return render(request,'documentary/index.html',{"titles": titles,"previous_page":previous_page,"current":page,"next_page":next_page,"total_pages":total_pages})

def title_add(request):
    return render(request, 'documentary/title_add.html')

def title_show(request):
    titles = Title.objects.all()
    return render(request,"documentary/title_show.html", {"titles": titles})

def title_batch_add(request):
    filename = get_file_path()+"title.txt"
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines:
        title = Title(title_name=line,)
        title.save()
    return HttpResponseRedirect('/documentary/title/show')

def title_page(request,page):
    page = int(page)
    titles, previous_page, next_page, total_pages = paging_title(page)
    return render(request,"documentary/title_page.html", {"titles": titles,"previous_page":previous_page,"current":page,"next_page":next_page,"total_pages":total_pages})

def site_add(request):
    return render(request,'documentary/site_add.html')

def site_show(request,title_id):
    title_id = int(title_id)
    sites = Site.objects.filter(title_id=title_id)
    title = Title.objects.get(id=title_id)
    return render(request,"documentary/site_show.html", {"sites": sites,"title":title})

def site_batch_add(request):
    to = Author.objects.get(name='to')
    filename = get_file_path()+"BT.txt"
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines:
        fields = line.split('\t')
        title = Title.objects.get(title_name=fields[(len(fields)-1)])
        for x in range(0,(len(fields)-1)):
            site = Site(title=title , author = to,seed=fields[x])
            site.save()

    return HttpResponseRedirect('/documentary/title/show')

def error(request):
    return render(request,"documentary/error.html")

def about(request):
    return render(request,"documentary/about.html")

def test(request):
#temp = req.json()['results'][0]
#pm25 = temp['pm25']
#temperature = temp['weather_data'][0]['temperature']
    cache.delete('weather')
    if not cache.get('weather'):
        URL = 'http://api.map.baidu.com/telematics/v3/weather?location=南京&output=json&ak=FK9mkfdQsloEngodbFl4FeY3'
        req = requests.get(URL)
        temp = req.json()['results'][0]
        pm25 = int(temp['pm25'])
        temperature = temp['weather_data'][0]['temperature']
       #pattern = re.compile(r'(\d+)')
       #temperature = re.findall(pattern,temperature)
       #temperature_low = temperature[1]
       #temperature_high = temperature[0]
       #data = {'pm25':pm25,'temperature_low':temperature_low,'temperature_high':temperature_high}
        data = {'pm25':pm25,'temperature':temperature}
        cache.set('weather',data,3600)
        data_cache = cache.get('weather')
    else:
        data_cache = cache.get('weather')
    return render(request,"documentary/test.html",{'data':data_cache})

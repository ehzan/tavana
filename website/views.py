from django.shortcuts import render
from django.http import HttpResponse
from website.models import *
from os import listdir, path
import mimetypes
import jdatetime
import random
import re

# Create your views here.


def home(request):
    header_local_path = './website/static/headers/'
    header_web_path = '/static/headers/'
    header_bgs = [header_web_path+bg for bg in listdir(header_local_path)
                  if path.isfile(header_local_path+bg) and re.search('.jpg$', bg)]
    header_bg = random.choice(header_bgs)
    # if path.isfile(sequencePath+file) and re.search('.dcm$', file)
    header_items = Highlight.objects.filter(header=True)
    body_items = Highlight.objects.filter(body=True)
    coaches = Coach.objects.all()
    articles = Article.objects.all()

    return render(request, 'home.html',
                  context={'header_bg': header_bg, 'header_items': header_items, 'body_items': body_items, 'coaches': coaches, 'articles': articles}, )


def get_page_data(pagename):
    pageData = Page.objects.get(name=pagename)
    images = [pageData.image_filename_1,
              pageData.image_filename_2, pageData.image_filename_3, ]
    captions = [pageData.image_caption_1,
                pageData.image_caption_2, pageData.image_caption_3, ]
    for i in range(len(images)):
        if images[i] != None:
            print(images[i])
            image_html = '</p> <figure> <img src="/static/images/{}" alt="{}"> <figcaption> {} </figcaption> </figure> <p>' \
                .format(images[i], images[i], captions[i] if captions[i] != None else '')
            pageData.content = pageData.content.replace(
                '<image>', image_html, 1)
    return pageData


def about(request):
    return render(request, 'about.html', context={'data': get_page_data('about')}, )


def coaches(request):
    categories = Coach.objects.all().values_list(
        'category', flat=True).distinct().order_by('order')
    toc = {category: Coach.objects.filter(category=category).values('english_name', 'persian_name')
           for category in categories}
    coaches = Coach.objects.all()

    return render(request, 'coaches.html', context={'toc': toc, 'coaches': coaches}, )


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', context={'contacts': contacts},)


def courses(request):
    semesters = Semester.objects.filter(active=True)
    courses = Course.objects.filter(semester__active=True)
    return render(request, 'courses.html', context={'semesters': semesters, 'courses': courses}, )


def page(request):
    pagename = request.resolver_match.url_name
    return render(request, 'page.html', context={'data': get_page_data(pagename)}, )


def tournaments(request):
    return render(request, 'tournaments.html', context={'data': get_page_data('tournaments')}, )


def articles(request):
    print(jdatetime.date.today())
    articles = Article.objects.all()
    return render(request, 'articles.html', context={'articles': articles, }, )

def article(request, id):
    article=Article.objects.get(pk=id)
    return render(request, 'page.html', context={'data': article}, )


def videos(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', context={'videos': videos}, )


def file_delivery(request, filename):
    filetype, fuck = mimetypes.guess_type('./website/files/'+filename)
    print(filetype)
    try:
        with open('./website/files/'+filename, 'rb') as f:
            resp = HttpResponse(f.read(), filetype)
        # response['Content-Type'] = filetype
        return resp
    except:
        return HttpResponse('sorry')

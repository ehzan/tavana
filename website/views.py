from django.shortcuts import render
from django.http import HttpResponse
from website.models import *
import mimetypes
import jdatetime

# Create your views here.


def home(request):
    header_items = Highlight.objects.filter(header=True)
    body_items = Highlight.objects.filter(body=True)
    return render(request, 'home.html', context={'header_items': header_items, 'body_items': body_items}, )


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


def news(request):
    print(jdatetime.date.today())
    header_items = Highlight.objects.filter(header=True)
    body_items = Highlight.objects.filter(body=True)
    print(header_items)
    return render(request, 'news.html', context={'header_items': header_items, 'body_items': body_items}, )


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

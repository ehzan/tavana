from django.shortcuts import render
from django.http import HttpResponse
from website.models import *
import mimetypes
import jdatetime

# Create your views here.


def home(request):
    highlights = Highlight.objects.filter(header=True)
    print(highlights)
    return render(request, 'home.html', context={'highlights': highlights}, )


def get_page_data(pagename):
    page = Page.objects.get(name=pagename)
    images = [page.image_filename_1,
              page.image_filename_2, page.image_filename_3, ]
    captions = [page.image_caption_1,
                page.image_caption_2, page.image_caption_3, ]
    for i in range(len(images)):
        if images[i] != None:
            print(images[i])
            image_html = '</p> <figure> <img src="/static/images/{}" alt="{}"> <figcaption> {} </figcaption> </figure> <p>' \
                .format(images[i], images[i], captions[i] if captions[i] != None else '')
            page.content = page.content.replace('<image>', image_html, 1)
    return page


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
    return render(request, 'contact.html')


def courses(request):
    semesters = Semester.objects.filter(active=True)
    courses = Course.objects.filter(semester__active=True)
    return render(request, 'courses.html', context={'semesters': semesters, 'courses': courses}, )


def free_session(request):
    return render(request, 'free-session.html', context={'data': get_page_data('free-session')}, )


def para(request):
    return render(request, 'para.html', context={'data': get_page_data('para')}, )


def tournaments(request):
    return render(request, 'tournaments.html', context={'data': get_page_data('tournaments')}, )


def rating_system(request):
    return render(request, 'rating-system.html', context={'data': get_page_data('rating-system')}, )


def news(request):
    print(jdatetime.date.today())
    header_items = Highlight.objects.filter(header=True)
    body_items = Highlight.objects.filter(body=True)
    print(header_items)
    return render(request, 'sidebar.html', context={'header_items': header_items, 'body_items': body_items}, )


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

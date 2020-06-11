from http import HTTPStatus
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from hashtag.models import ScrapyItem

scrapyd = ScrapydAPI('http://localhost:6800')


def crawl(request, hashtag_value):
    unique_id = hashtag_value
    settings = {
        'unique_id': unique_id,
    }
    task = scrapyd.schedule('default', 'new_hashtag',settings=settings,
                            unique_id=unique_id)
    return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})
    

    # elif request.method == 'GET':
    #     unique_id = request.GET.get('tag', None)
    #     context = None
    #     if unique_id:
    #         items = ScrapyItem.objects.filter(unique_id=unique_id)
    #         image_urls = []
    #         for item in items:
    #             image_urls.append(item.unique_id)
    #         context = {
    #             'image_urls': image_urls
    #         }
    #     return render(request, 'hashtag/index.html', context)
    # #     unique_id = request.GET.get('tag', None)
    #     image_urls = ScrapyItem.objects.filter(unique_id=unique_id)
    #     context = {
    #         'image_urls': image_urls
    #     }

    #     return render(request, index.html, context)


        # task_id = request.GET.get('task_id', None)
        # unique_id = request.GET.get('tag', None)
    
        # if not task_id or not unique_id:
        #     return JsonResponse({'error': 'Missing args'})
    
        # status = scrapyd.job_status('default', task_id)
        # if status == 'finished':
        #     try:
        #         items = ScrapyItem.objects.filter(unique_id=unique_id)
        #         dict_list = []
        #         for i in list(items):
        #             dict_data = {
        #                 'url': i.url,
        #                 'date': i.date.strftime('%Y-%m-%d %H:%M')
        #             }
        #             dict_list.append(dict_data)
        #         data = {'data': dict_list}
        #         return JsonResponse(data)
        #     except Exception as e:
        #         return JsonResponse({'error': str(e)})
        # else:
        #     return JsonResponse({'status': status})


def show_data(request, hashtag_value):
    items = ScrapyItem.objects.filter(unique_id=hashtag_value)
    if not items:
        return JsonResponse(
            {'error': 'There is no data in database for this hashtag'},
            status=HTTPStatus.NOT_FOUND
        )
    image_urls = []
    for item in items:
        image_urls.append(item.data)        
    context = {
        'image_urls': image_urls,
        'hashtag_value': hashtag_value
    }
    return render(request, 'hashtag/index.html', context)
    # for i in list(items):
    #     dict_data = {
    #         'hashtag': i.unique_id,
    #         'img_url': i.data,
    #         'date': i.date.strftime('%Y-%m-%d %H:%M')
    #     }
    #     dict_list.append(dict_data)
    # data = {'data': dict_list}
    # return JsonResponse(data)
    # 
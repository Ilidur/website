from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import telegram
import json, datetime

@csrf_exempt
@require_POST
def hook(request):
    jsondata = request.body
    body = json.loads(jsondata)

    bot = telegram.Bot(token='360648398:AAG-vPZv-0GwPkqRkIs3sVogfM4M3wKxkFg')

    url = request.META['HTTP_X_DISCOURSE_INSTANCE'] + '/t/' + body['topic']['slug'] + '/' + str(body['topic']['id']) + '/' + str(body['topic']['posts_count'])
    msg = "Forum: " + request.META['HTTP_X_DISCOURSE_EVENT'] + ' in ' + url



    bot.sendMessage(chat_id=-150366976, text=msg)


    return HttpResponse(status=200)

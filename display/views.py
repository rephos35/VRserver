# from django.shortcuts import render
# from django.http import JsonResponse
from django.http import HttpResponse

from VRserver.serializers import StatusSerializer
from VRserver.models import StatusDB

from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# import json

import datetime


def all_data_view(request):
    all_db = StatusDB.objects.all()
    serializer = StatusSerializer(instance=all_db, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json', status=200)


def last_data_view(request):
    now = datetime.datetime.now()
    now_can_read_time = (now - datetime.timedelta(seconds=10)).strftime('%M:%S')

    # get last db time
    last_db = StatusDB.objects.last()
    last2_db = StatusDB.objects.all().filter(id=last_db.id - 1).last()

    if last_db is None:
        last_serializer = StatusSerializer(partial=True)
    else:
        if last2_db is None:
            if last_db.created.strftime('%M:%S') >= now_can_read_time:  # can read
                last_serializer = StatusSerializer(instance=last_db)
            else:
                last_serializer = StatusSerializer(partial=True)
        else:
            if last2_db.created.strftime('%M:%S') >= now_can_read_time:
                last_serializer = StatusSerializer(instance=last2_db)
            else:
                last_serializer = StatusSerializer(partial=True)

    json_data = JSONRenderer().render(last_serializer.data)
    return HttpResponse(json_data, content_type='application/json', status=200)
import plistlib

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from VRserver.models import StatusDB
from VRserver.serializers import StatusSerializer
import json
import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Min, Max

# 繼承 (inheritance)
# 如果子類有與父類擁有同名的函式，則子類會會覆蓋掉父類的函式。

# def  funA ( fn ):
# @funA
# def funB():
# @函數裝飾器/裝飾符: funB =  funA ( funB )

# MyModel.objects.filter(name='simple').last()

# from rest_framework.views import APIView
# class status_view(APIView):
#     def get_object(self, pk):
#         return StatusDB.objects.get(pk=pk)
#
#     def patch(self, request, pk):
#         testmodel_object = StatusDB.objects.get(pk=pk)
#         serializer = StatusSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(code=201, data=serializer.data)
#         return JsonResponse(code=400, data="wrong parameters")


last_hour = None
last_min_sec_end = None


@api_view(['STATUS'])
def status_view(request):
    # terminal postman ok
    # all_db = StatusDB.objects.all()  # 获取模型类数据
    # ser = StatusSerializer(instance=all_db, many=True)  # 序列化数据instance
    # json_data = JSONRenderer().render(ser.data)
    #
    # return HttpResponse(json_data, content_type='application/json', status=200)

    # terminal  ok postman XXXXXX
    # create_update_db = StatusDB.objects.filter(created__minute=datetime.datetime.now()).first()

    global last_hour
    global last_min_sec_end


    # table list created

    now = datetime.datetime.now()
    now_hour = now.hour
    now_min_sec = now.strftime('%M:%S')
    now_can_read_time = (now - datetime.timedelta(seconds=5)).strftime('%M:%S')

    # get last db time
    last_db = StatusDB.objects.last()
    if last_db is not None:
        last_min_sec_end = (last_db.created + datetime.timedelta(seconds=3)).strftime('%M:%S')
    else:
        last_min_sec_end = None

    # (db not empty) && not the same day > clear
    if last_hour != now_hour:
        StatusDB.objects.all().delete()
    # update day
    last_hour = now_hour

    # every k seconds save data to db
    if last_min_sec_end is not None and last_min_sec_end > now_min_sec:
        # update
        serializer = StatusSerializer(instance=last_db, data=request.data, partial=True)

        # last2_db = StatusDB.objects.all()
        # last2_db = last2_db[-1]
        last2_db = StatusDB.objects.all().filter(id=last_db.id - 1).last()  # [1]
        last_serializer = serializer
        if last2_db is not None:
            if last2_db.created.strftime('%M:%S') >= now_can_read_time:
                last_serializer = StatusSerializer(instance=last2_db)
    else:
        # create
        serializer = StatusSerializer(data=request.data, partial=True)

        last_serializer = serializer
        if last_db is not None:
            if last_db.created.strftime('%M:%S') >= now_can_read_time:
                last_serializer = StatusSerializer(instance=last_db)

    if serializer.is_valid():
        serializer.save()




    # data = StatusDB.objects.filter(user6__contains=78)
    # # StatusDB.objects.all().update(user4=444)
    # serializer = StatusSerializer(instance=data, partial=True)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(request.data)  # return change


def db_size_limiter():
    # limit table size = 100
    minmax_id = StatusDB.objects.all().aggregate(Min('id'), Max('id'))
    min_id = minmax_id.get('id__min')
    max_id = minmax_id.get('id__max')
    if max_id - min_id + 1 > 10:  # __gte __lte getXXX
        StatusDB.objects.get(id=min_id).delete()



        #class ->None

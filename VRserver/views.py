from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from VRserver.models import User
from VRserver.serializers import UserSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Min, Max
import datetime
user_name_set = []

def read_last_row(name):

    filtered_user_data = User.objects.filter(name=name).order_by('-id')
    serializer = UserSerializer(filtered_user_data, many=True)
    if serializer.data:
        data = serializer.data[0]
    else:
        data = []
    return data

@api_view(['GET', 'POST'])
def save_user_status(request):

    '''
    This url provides GET and POST APIs.

    POST: Save a status for a user.
    GET : Get the last recorded data.
    '''

    if request.method == 'POST':
        # Do save data.
        # TODO: Validate the parameters.
        serializer = UserSerializer(data=request.data)
        result = serializer.is_valid()
        if result:
            serializer.save()
        return Response({"result": result})
    elif request.method == 'GET':
        last_row = User.objects.last()
        serializer = UserSerializer(last_row)
        return Response(serializer.data)

@api_view(['GET'])
def get_last_data(request, name):

    '''
    GET method to get the last data of 1 specific user.
    '''
    response = read_last_row(name)

    return Response(response)

@api_view(['GET'])
def get_all_last_data(request):

    '''
    GET method to get all user's last data.
    '''

    user_name_set = User.objects.values_list('name')
    user_name_set = set(user_name_set)

    result = []
    data_status = {'date':'', 'status':''}
    result_dict = {}
    for username in user_name_set:
        last_row_dict = read_last_row(username[0]) #{"id":8,"created":"2022-04-24T18:58:40.173538","name":"allen","status":"soso"}
        data_status['status'] = last_row_dict['status']
        data_status['date'] = last_row_dict['created']
        result_dict[last_row_dict["name"]]= data_status
        # print(result_dict)
        result.append(read_last_row(username[0]))
    # print(result_dict)


    # TODO: Make result list to be json format.

    return Response(result_dict)
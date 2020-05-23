from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
import requests
from datetime import datetime

@api_view(['GET',])
def date_check(request,format= None):
    """
    pass the params as key value pairs for eg:-
    url = https://httpbin.org
    datetime = yy-mm-dd HH-MM
    sample url
    'http://127.0.0.1:8000/?url=https://httpbin.org&datetime=2020-05-24 11:25'
    if success returns
    'status':200
    """
    #get the params
    query_date = request.query_params.get('datetime')
    query_url = request.query_params.get('url')
    #get the current time
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    #print the time for reference
    print(now)
    #if the requested date is same as 'now'
    if query_date == now:
        #send a get request to the param URL
        response = requests.get(query_url)
        
        if response.status_code == 200:#returns the status code 
            return Response(data={'status':200})

        else:#if the website did not get the request return error
            return Response(data={'status':'error'})

    else: #if the time did not match
        return Response(data={'error':'date-time does not match'})

@api_view(['GET',])
def ping(request,format= None):
    """
    /ping/ to check status of the server
    returns a 'status:OK' object
    """
    return Response(data={'status':'OK'})
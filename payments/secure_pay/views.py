from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the secure pay index.")

def pay(request):
    # Get access token
    url = 'https://welcome.api2.sandbox.auspost.com.au/oauth/token'
    data = {'grant_type': 'client_credentials', 'audience': 'https://api.payments.auspost.com.au'}
    headers = {'Authorization': 'Basic xxxxxxxx', 'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=('0oaxb9i8P9vQdXTsn3l5', '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp'))
    # print(r.json())
    
    return HttpResponse("/pay")
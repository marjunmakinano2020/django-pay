from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the secure pay index.")

def pay(request):
    # Get access token
    # Todo: Fix 'grant_type': 'client_credentials' and 'Authorization': 'Basic xxxxxxxx'
    # And auth=('0oaxb9i8P9vQdXTsn3l5', '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp')
    url = 'https://welcome.api2.sandbox.auspost.com.au/oauth/token'
    data = {'grant_type': 'client_credentials', 'audience': 'https://api.payments.auspost.com.au'}
    headers = {'Authorization': 'Basic xxxxxxxx', 'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=('0oaxb9i8P9vQdXTsn3l5', '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp'))
    # print(r.json())

    # Create a payment
    payment_url = 'https://payments-stest.npe.auspost.zone/v2/payments'
    payment_data = {
        "amount": 10000,
        "merchantCode": "YOUR_MERCHANT_CODE",
        "token": "de305d54-75b4-431b-adb2-eb6b9e546014",
        "ip": "127.0.0.1",
        "orderId": "0475f32d-fc23-4c02-b19b-9fe4b0a848ac"
    }
    payment_headers = {"Content-Type": "application/json", "Idempotency-Key": "022361c6-3e59-40df-a58d-532bcc63c3ed", "Authorization": "Bearer xxxxxxxx"}
    payment_r = requests.post(payment_url, data=json.dumps(payment_data), headers=payment_headers, auth=('0oaxb9i8P9vQdXTsn3l5', '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp'))
    # print(payment_r.json())
    
    return HttpResponse("/pay")
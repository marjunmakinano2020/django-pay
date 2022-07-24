from django.shortcuts import render
from django.http import HttpResponse
from base64 import b64encode
import requests
import json


def index(request):
    return HttpResponse("Hello, world. You're at the secure pay index.")


def pay(request):
    merchant_code = '5AR0055'
    client_id = '0oaxb9i8P9vQdXTsn3l5'
    client_secret = '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp'

    basic_auth = client_id + ':' + client_secret
    basic_auth64 = b64encode(basic_auth.encode("utf-8"))
    basic_auth_string = 'Basic ' + basic_auth64.decode("utf-8")

    # Get access token
    # And auth=('0oaxb9i8P9vQdXTsn3l5', '0aBsGU3x1bc-UIF_vDBA2JzjpCPHjoCP7oI6jisp')
    url = 'https://welcome.api2.sandbox.auspost.com.au/oauth/token'
    data = {
        'grant_type': 'client_credentials',
        'audience': 'https://api.payments.auspost.com.au'
    }
    headers = {
        'Authorization': basic_auth_string,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, data=json.dumps(data), headers=headers).json()
    token = r["access_token"]

    # Create a payment
    # Todo: Fix token, orderId, Idempotency-Key, Authorization, auth
    bearer_auth = "Bearer " + token

    payment_url = 'https://payments-stest.npe.auspost.zone/v2/payments'
    payment_data = {
        "amount": 10000,
        "merchantCode": merchant_code,
        "token": 'de305d54-75b4-431b-adb2-eb6b9e546014',
        "ip": "127.0.0.1",
        "orderId": "0475f32d-fc23-4c02-b19b-9fe4b0a848ac"
    }
    payment_headers = {
        "Content-Type": "application/json",
        "Idempotency-Key": "022361c6-3e59-40df-a58d-532bcc63c3ed",
        "Authorization": bearer_auth
    }
    payment_r = requests.post(payment_url,
                              data=json.dumps(payment_data),
                              headers=payment_headers)
    # print(payment_r.json())

    return HttpResponse("/pay")

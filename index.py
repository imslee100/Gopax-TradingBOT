from traceback import print_list
import requests
import time

API_TOKEN = ''
API_KEY = ''

r = requests.get('https://api.gopax.co.kr/trading-pairs')

# Coin List on Gopax
res_list = r.json()

for rl in res_list:
    print(rl)
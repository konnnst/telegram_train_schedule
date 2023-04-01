import json

import requests
from apikey import YANDEX_API
from datetime import datetime
import json

def isLater(time, dep):
    return time[:8] < dep[11:19]

def getTrains(mode):
    data, time, start, end = datetime.now().date(), str(datetime.now().time()), 's9603770', 's9602498'
    if mode:
        start, end = 's9602498', 's9603770'
    params = {'from' : start, 'to' : end, 'apikey' : YANDEX_API, 'date' : data}
    raw = requests.get('https://api.rasp.yandex.net/v3.0/search/', params=params).json()
    table, n = raw['segments'], len(raw['segments'])
    for i in range(n):
        arr, dep = table[i]['arrival'], table[i]['departure']
        if isLater(time, dep):
           return [table[i], table[i + 1]] if i + 1 < n else [table[i]]

def strTrains(mode):
    trains = getTrains(mode)
    place = 'уника' if mode else 'Питера'
    res = '<b>Ближайшие поезда до ' + place + ':</b>\n'
    for tr in trains:
        name = tr['thread']['transport_subtype']['title']
        arr, dep = tr['arrival'], tr['departure']
        res += f'Поезд: {name}\nОтправление: {dep[11:19]}\nПрибытие: {arr[11:19]}\n\n'
    return res

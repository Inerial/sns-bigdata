import os
import codecs
import json
import numpy
import re
from collections import Counter


f = open('words.json','r', encoding='utf-8')
lines = f.readlines()

for i,line in enumerate(lines):
     lines[i] = json.loads(line)

add_day = {}
for line in lines:
    if line['date'] in add_day:
        add_day[line['date']] += Counter(line['data'])
    else:
        add_day[line['date']] = Counter(line['data'])


add_Month = {}
for line in lines:
    if line['date'][:6] in add_Month:
        add_Month[line['date'][:6]] += Counter(line['data'])
    else:
        add_Month[line['date'][:6]] = Counter(line['data'])


result = {}
temped = {}
for date in add_Month.keys():
    sum = len(list(add_Month[date].elements()))
    result[date] = {'etc':0}
    temped[date] = {'etc':0}
    for key in add_Month[date].keys():
        temp = 100*add_Month[date][key]/sum
        if temp < 0.001:
            result[date]['etc'] += add_Month[date][key]
            temped[date]['etc'] += temp
        else:
            result[date][key] = add_Month[date][key]
            temped[date][key] = temp

date = ['01','02','03','04','05']
year1 = '2014'
year2 = '2015'
mean1 = 0
total = 0
for key in temped[year1+date[0]].keys():
    if key in temped[year2+date[0]].keys():
        asdfasdf = abs(temped[year1+date[0]][key] - temped[year2+date[0]][key])
        mean1 += asdfasdf
        total += 1
mean1 /= total

mean2 = 0
for key in temped[year1+date[0]].keys():
    if key in temped[year1+'08'].keys():
        asdfasdf = abs(temped[year1+date[0]][key] - temped[year1+'08'][key])
        mean2 += asdfasdf
        if max < asdfasdf:
            max = asdfasdf
            qwer = key
mean2 /= len(temped[year1+date[0]].keys())

sum = 0
ans = {'month':[], 'all':[]}
for key in temped[year1+date[0]].keys():
    if key in temped[year2+date[0]].keys():
        asdfasdf = abs(temped[year1+date[0]][key] - temped[year2+date[0]][key])
        if asdfasdf < mean1/2:
            if key in temped[year1 + '08'].keys():
                qwerqwer = abs(temped[year1+date[0]][key] - temped[year1+'08'][key])
                if qwerqwer < mean2*3:
                    ans['all'].append(key)
                else:
                    ans['month'].append(key)
            else:
                ans['month'].append(key)


dates = ['201401','201402','201403','201404','201405','201406','201407','201408','201501','201502','201503','201504','201505']
means = {}
for now in dates:
    means[now] = {}
    for date in dates:
        if now != date:
            means[now][date] = 0
            total = 0
            for key in temped[now].keys():
                if key in temped[date].keys():
                    asdfasdf = abs(temped[now][key] - temped[date][key])
                    means[now][date] += asdfasdf
                    total += 1
            means[now][date] /= total

months = ['01','02','03','04','05']
years = ['2014', '2015']
ans = {'all':[]}
for now in dates:
    ans[now] = []
    tmp = temped[now].keys()
    for key in temped[now].keys():
        flag = 0
        if now[4:6] in months:
            if now[:4] == years[0]:
                num = 1
            else:
                num = 0
            if key in temped[years[num]+now[4:6]].keys():
                asdfasdf = abs(temped[now][key] - temped[years[num]+now[4:6]][key])
                if asdfasdf < means[now][years[num] + now[4:6]]/2:
                    for date in dates:
                        if (date != now) & (date != years[num]+now[4:6]):
                            if key in temped[date].keys():
                                qwerqwer = abs(temped[now][key] - temped[date][key])
                                if qwerqwer > means[now][date]:
                                    if key in ans[now]:
                                        pass
                                    elif flag == 0:
                                        ans[now].append(key)
                                else:
                                    flag = 1
                                    if key in ans[now]:
                                        ans[now].remove(key)
        else:
            for date in dates:
                if date != now:
                    if key in temped[date].keys():
                        qwerqwer = abs(temped[now][key] - temped[date][key])
                        if qwerqwer > means[now][date]:
                            if key in ans[now]:
                                pass
                            elif flag == 0:
                                ans[now].append(key)
                        else:
                            flag = 1
                            if key in ans[now]:
                                ans[now].remove(key)

for date in dates:
    print(date, ans[date])
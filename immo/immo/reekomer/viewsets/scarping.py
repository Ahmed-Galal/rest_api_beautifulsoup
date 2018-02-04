#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..scarping.util import Util
from ..scarping.schema import Schema



import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import *


def parseUrl(url, item_url):
    util = Util()
    soup = util.getUrl(url)
    data_list = []
    for item in soup.find_all('li', itemtype='http://schema.org/Offer'):
        print("=========item================")
        print(item)
        data_list.append(util.json_object(item, item_url))
    return data_list


@csrf_exempt
def ScarpingView(request):
    if request.method == 'GET':
        schema = Schema()
        json_schema = schema.getSchema()
        for key in json_schema:

            for loc in json_schema[key]['locations']:
                for city in json_schema[key]['allowed_cities']:
                    url = json_schema[key]['url'].replace('{LOCATION}', loc).replace('{SEARCHKEY}', city)
                    item_url = json_schema[key]['item_url'].replace('{LOCATION}', loc)
                    scarping_data = parseUrl(url, item_url)
                    if (key == "region"):
                        print(scarping_data)
                        print("--------------------------\n")
                        tablename = Region(
                            date=scarping_data['date'],
                            price=scarping_data['price'],
                            code_postal=scarping_data['postal_code'],
                            price_msquare=scarping_data['city'],
                            place=scarping_data['city'],
                            typeImo=scarping_data['city'],
                            size=scarping_data['postal_code'],
                            charac=scarping_data['postal_code'],
                            description=scarping_data['description'],
                            link=scarping_data['url'],
                            website=scarping_data['url'],
                            image=scarping_data['img'],
                            idannonce=scarping_data['postal_code'],
                            phone_number=scarping_data['postal_code'],
                        )
                        tablename.save()
                    # if (key == "immo"):
                    #     tablename = Immo(
                    #         date=scarping_data.date,
                    #         price=scarping_data.price,
                    #         code_postal=scarping_data.postal_code,
                    #         price_msquare=scarping_data,
                    #         place=scarping_data.city,
                    #         typeImo=scarping_data.city,
                    #         size=scarping_data.postal_code,
                    #         charac=scarping_data.postal_code,
                    #         description=scarping_data.description,
                    #         link=scarping_data.url,
                    #         website=scarping_data.url,
                    #         image=scarping_data.img,
                    #         idannonce=scarping_data.postal_code,
                    #         phone_number=scarping_data.postal_code,
                    #     )
                    # if (key == "immeuble"):
                    #     tablename = Immeuble(
                    #         date=scarping_data.date,
                    #         price=scarping_data.price,
                    #         code_postal=scarping_data.postal_code,
                    #         price_msquare=scarping_data,
                    #         place=scarping_data.city,
                    #         typeImo=scarping_data.city,
                    #         size=scarping_data.postal_code,
                    #         charac=scarping_data.postal_code,
                    #         description=scarping_data.description,
                    #         link=scarping_data.url,
                    #         website=scarping_data.url,
                    #         image=scarping_data.img,
                    #         idannonce=scarping_data.postal_code,
                    #         phone_number=scarping_data.postal_code,
                    #     )
                    # if (key == "habitation"):
                    #     tablename = Habitation(
                    #         date=scarping_data.date,
                    #         price=scarping_data.price,
                    #         code_postal=scarping_data.postal_code,
                    #         price_msquare=scarping_data,
                    #         place=scarping_data.city,
                    #         typeImo=scarping_data.city,
                    #         size=scarping_data.postal_code,
                    #         charac=scarping_data.postal_code,
                    #         description=scarping_data.description,
                    #         link=scarping_data.url,
                    #         website=scarping_data.url,
                    #         image=scarping_data.img,
                    #         idannonce=scarping_data.postal_code,
                    #         phone_number=scarping_data.postal_code,
                    #     )
                    # tablename.save()
        return JsonResponse({'ok': 'ok'})
    else:
        return JsonResponse({'error': 'not allowed'})

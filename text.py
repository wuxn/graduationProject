#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "register.settings")

import django
if django.VERSION >= (1,7):
    django.setup()

def main():
    from account.models import price,sqm,houseDetail
    f = open('houseDetail.txt')
    for line in f:
        houseId,imgUrl,houseTitle= line.split('****')
        houseDetail.objects.create(houseId=houseId,imgUrl=imgUrl,houseTitle=houseTitle)

if __name__ == "__main__":
    main()
    print('Done!')
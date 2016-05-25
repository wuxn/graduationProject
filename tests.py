
# Create your tests here.

#coding=utf-8
import json,sqlite3
from django.conf import settings
settings.configure()
from account.models import Person

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('select * from account_housedetail')
print type(c.fetchall())

data = json.dumps(Person.objects.all())

print type(data)
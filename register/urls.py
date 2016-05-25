from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'account.views.register'),
    url(r'^housedetail/(\d{1,2})/$', 'account.views.dynamicUrl'),
    url(r'area/(\d{1,2})/$','account.views.areaUrl'),
    url(r'^login/','account.views.data'),
    url(r'index/','account.views.index'),
    url(r'add/','account.views.add'),
    url(r'success/','account.views.success'),
    url(r'modify/','account.views.modify'),
    url(r'^others/$', 'account.views.getdata'),
    url(r'about', 'account.views.about'),
    url(r'contact', 'account.views.contact'),


)
#coding=utf-8
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from.models import User, houseDetail, area, price, sqm, houseResponsible, dataUser, File
from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger, EmptyPage
import sqlite3

# Create your views here.

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
context = {}

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='',max_length=100)
    password = forms.CharField(label='',widget=forms.PasswordInput())
    email = forms.EmailField(label='')

class UserFormLogin(forms.Form):
    username = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='', widget=forms.PasswordInput())

class fileForm(forms.Form):
    user = forms.CharField()
    headImg = forms.FileField()

def success(request):
    if request.method == 'POST':
        uf = fileForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['user']
            headImg = uf.cleaned_data['headImg']
            files = File()
            files.username = username
            files.headImg = headImg
            files.save()
            return HttpResponse('upload ok')
    else:
        uf = fileForm()
    return render_to_response('add-success.html',{'uf':uf})
class fileForm(forms.Form):
    headImg = forms.FileField()
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        ufl = UserFormLogin(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username})
        if ufl.is_valid():
            # 获取表单用户密码
            username = ufl.cleaned_data['username']
            password = ufl.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return render_to_response('register.html', {'username': username})
            else:
                return HttpResponseRedirect('/account/')
    else:
        uf = UserForm()
        ufl = UserFormLogin()
    data = houseDetail.objects.order_by('houseId')
    for d in data:
        d.imgUrl = d.imgUrl.name.split(",")[0].split("/")[-1]
    areadata = area.objects.all()
    pricedata = price.objects.all()
    sqmdata = sqm.objects.all()
    searchdata = request.GET.get("search",'s')
    context['uf'] = uf
    context['ufl'] = ufl
    context['areadata'] = areadata
    context['pricedata'] = pricedata
    context['sqmdata'] = sqmdata
    limit = 6
    paginator = Paginator(data, limit)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context['data'] = data
    c.execute('select * from account_housedetail where account_housedetail.houseAddress like "%' + searchdata + '%"')
    datas = []
    for i in c.fetchall():
        datas.append({'houseId': i[1], 'imgUrl': i[2].split(",")[0], 'houseTitle': i[3], 'housePrice': i[5]})
    if datas:
        context['data'] = datas
    else:
        context['data'] = data
    return render_to_response('register.html',context,context_instance=RequestContext(request))
def areaUrl(request,offset):
    offset = int(offset)
    adata = area.objects.get(areaId=offset)
    areaHouseId = adata.areaHouseId.split(",")
    temp = []
    for ahid in areaHouseId:
        hdata = houseDetail.objects.get(houseId=int(ahid))
        hdata.imgUrl = hdata.imgUrl.name.split(",")[0].split("/")[-1]
        temp.append(hdata)
    data = houseDetail.objects.all()
    for d in data:
        d.imgUrl = d.imgUrl.name.split(",")[0].split("/")[-1]
    areadata = area.objects.all()
    pricedata = price.objects.all()
    sqmdata = sqm.objects.all()
    currentUrl = request.path.split("/")[2]
    context = {}
    context['adata'] = adata
    context['temp'] = temp
    context['areadata'] = areadata
    context['pricedata'] = pricedata
    context['sqmdata'] = sqmdata
    context['currentUrl'] = currentUrl
    searchdata = request.GET.get("search",'s')
    c.execute('select * from account_housedetail where account_housedetail.houseAddress like "%' + searchdata + '%"')
    datas = []
    for i in c.fetchall():
        datas.append({'houseId': i[1], 'imgUrl': i[2].split(",")[0], 'houseTitle': i[3], 'housePrice': i[5]})
    if datas:
        context['temp'] = datas
    else:
        context['temp'] = temp
    return render_to_response('register.html',context,context_instance=RequestContext(request))
def dynamicUrl(request, offset):
    offset = int(offset)
    hdata = houseDetail.objects.get(houseId=offset)
    imgfst = hdata.imgUrl.split(",")[0]
    hdata.imgUrl = hdata.imgUrl.split(",")
    hrid = int(hdata.houseResponsibleId)
    rdata = houseResponsible.objects.get(responsibleId=hrid)
    searchdata = request.GET.get("search", 's')
    context['hdata'] = hdata
    context['imgfst'] = imgfst
    context['hrid'] = hrid
    context['rdata'] = rdata
    c.execute('select * from account_housedetail where account_housedetail.houseAddress like "%' + searchdata + '%"')
    datas = []
    for i in c.fetchall():
        datas.append({'houseId': i[1], 'imgUrl': i[2].split(",")[0], 'houseTitle': i[3], 'housePrice': i[5]})
    if datas:
        context['hdata'] = datas
    else:
        context['hdata'] = hdata
    return render_to_response('house-detail.html',{'imgfst':imgfst,'hrid':hrid,'rdata':rdata,'offset':offset,'hdata':hdata},context_instance=RequestContext(request))
# house data manage
def data(request):
    adminUn = request.POST.get('adminun','admin-login')
    adminPw = request.POST.get('adminpw','admin-login')
    adminUser = dataUser.objects.filter(adminUn__exact=adminUn, adminPw__exact=adminPw)
    if adminUser:
        successed = 9
        request.session['successed'] = successed
        print successed
        return HttpResponseRedirect('/index')
    else:
        return render_to_response('login.html')
    return render_to_response('login.html')

def index(request):
    successed = request.session.get('successed')
    if successed == 9:
        data = houseDetail.objects.order_by('houseId')
        for d in data:
            d.imgUrl = d.imgUrl.name.split(",")[0].split("/")[-1]
        areadata = area.objects.all()
        pricedata = price.objects.all()
        sqmdata = sqm.objects.all()
        searchdata = request.GET.get('search','s')
        context = {}
        context['areadata'] = areadata
        context['pricedata'] = pricedata
        context['sqmdata'] = sqmdata
        # c.execute('select * from account_housedetail where account_housedetail.houseAddress like "%' + searchdata + '%"')
        # datas = []
        # for i in c.fetchall():
        #     datas.append({'houseId': i[1], 'imgUrl': i[2].split(",")[0], 'houseTitle': i[3], 'housePrice': i[5]})
        # if datas:
        #     context['data'] = datas
        # else:
        limit = 6
        paginator = Paginator(data, limit)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        context['data'] = data
        did = request.GET.get('id')
        if did:
            houseDetail.objects.get(houseId=int(did)).delete()
        return render_to_response('index.html',context,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/login/")
def add(request):
    successed = request.session.get('successed')
    if successed == 9:
        if request.method == 'POST':
            imgf = fileForm(request.POST,request.FILES)
            if imgf.is_valid():
                headImg = imgf.cleaned_data['headImg']
                houseid = request.POST.get('houseid')
                housetitle = request.POST.get('housetitle')
                housede = request.POST.get('housede')
                housepri = request.POST.get('housepri')
                housearea = request.POST.get('housearea')
                housestyle = request.POST.get('housestyle')
                houseadd = request.POST.get('houseadd')
                houseyear = request.POST.get('houseyear')
                houserid = request.POST.get('houserid')
                housername = request.POST.get('housername')

                house = houseDetail()
                house.imgUrl = headImg
                house.houseId = houseid
                house.houseTitle = housetitle
                house.houseDescribe = housede
                house.housePrice = housepri
                house.houseArea = housearea
                house.houseStyle = housestyle
                house.houseAddress = houseadd
                house.houseYear = houseyear
                house.houseResponsibleId = houserid
                house.save()

            # housedata = houseDetail.objects.all()
            # c.execute("select houseResponsibleId from account_housedetail where account_housedetail.houseResponsibleId=" + houserid)
            # if c.fetchone():
                return HttpResponseRedirect('/index')
            # else:
            #     context['houserid'] = houserid
            #     context['housername'] = housername
            #     return render_to_response('house-add.html',context,context_instance=RequestContext(request))
        else:
            imgf = fileForm()
        return render_to_response('house-add.html',{'imgf':imgf})
    else:
        return HttpResponseRedirect('/login/')

def others(request):
    successed = request.session.get('successed')
    if successed == 9:
        return render_to_response('others.html')
def modify(request):
    # myclass.objects.all().update(aa='8888')
    successed = request.session.get('successed')
    if successed == 9:
        if request.method == 'POST':
            # houseid = request.POST.get('houseid')
            # hdata = houseDetail.objects.get(houseId=houseid)
            # if houseid != '':
            #     houseDetail.objects.get(houseId=houseid)
            context = {}
            mid = request.GET.get('id')
            mdata = houseDetail.objects.get(houseId=int(mid))
            houseid = request.POST.get('houseid')
            context['mid'] = mid
            context['mdata'] = mdata
            if mid == houseid:
                mdata


        return render_to_response('house-add.html',context)
    else:
        return HttpResponseRedirect("/login/")
def  getdata(request):
    limit = 6
    sqms = sqm.objects.all()
    paginator = Paginator(sqms, limit)
    page = request.GET.get('page')
    try:
        sqms = paginator.page(page)
    except PageNotAnInteger:
        sqms = paginator.page(1)
    except EmptyPage:
        sqms = paginator.page(paginator.num_pages)
    return render_to_response('others.html',{'sqms':sqms})

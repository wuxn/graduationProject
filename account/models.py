from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')

class houseDetail(models.Model):
    houseId = models.CharField(max_length=50)
    imgUrl = models.FileField(upload_to='./account/template/attach-files/images/')
    houseTitle = models.CharField(max_length=100)
    houseDescribe = models.CharField(max_length=200)
    housePrice = models.CharField(max_length=50)
    houseArea = models.CharField(max_length=50)
    houseStyle = models.CharField(max_length=50)
    houseAddress = models.CharField(max_length=200)
    houseYear = models.CharField(max_length=50)
    houseResponsibleId = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s' %(self.houseId,self.imgUrl,self.houseTitle,self.houseDescribe,self.housePrice,self.houseArea,self.houseStyle,self.houseAddress,self.houseYear,self.houseResponsibleId)

class houseAdmin(admin.ModelAdmin):
    list_display = ('houseId','imgUrl','houseTitle','houseDescribe','housePrice','houseArea','houseStyle','houseAddress','houseYear','houseResponsibleId')

class houseResponsible(models.Model):
    responsibleId = models.CharField(max_length=50)
    responsibleName = models.CharField(max_length=50)
    responsiblePhone = models.CharField(max_length=50)
    responsibleEmail = models.CharField(max_length=50)
    responsibleAddress = models.CharField(max_length=100)
    houseIds = models.CharField(max_length=100)

    def __unicode__(self):
        return self.responsibleId

class responsibleAdmin(admin.ModelAdmin):
    list_display = ('responsibleId','responsibleName','responsiblePhone','responsiblePhone','responsibleEmail','responsibleAddress','houseIds')

class area(models.Model):
    areaId = models.CharField(max_length=50)
    areaProvince = models.CharField(max_length=50)
    areaCity = models.CharField(max_length=50)
    areaDistrict = models.CharField(max_length=1000)
    areaHouseId = models.CharField(max_length=1000)

    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.areaId,self.areaProvince,self.areaCity,self.areaDistrict,self.areaHouseId)

class areaAdmin(admin.ModelAdmin):
    list_display = ('areaId','areaProvince','areaCity','areaDistrict','areaHouseId')

class price(models.Model):
    priceId = models.CharField(max_length=30)
    priceNum = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' %(self.priceId,self.priceNum)
class priceAdmin(admin.ModelAdmin):
    list_display = ('priceId','priceNum')

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    num1 = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age','num1')

class sqm(models.Model):
    sqmId = models.CharField(max_length=30)
    sqmNum = models.CharField(max_length=30)
    sqmUrl = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s %s' %(self.sqmId,self.sqmNum,self.sqmUrl)
class sqmAdmin(admin.ModelAdmin):
    list_display = ('sqmId','sqmNum','sqmUrl')

# house data manage
class dataUser(models.Model):
    adminId = models.CharField(max_length=50)
    adminUn = models.CharField(max_length=50)
    adminPw = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s %s %s' %(self.adminId,self.adminUn,self.adminPw)
class dataUserAdmin(admin.ModelAdmin):
    list_display = ('adminId','adminUn','adminPw')

class File(models.Model):
    username = models.CharField(max_length=50)
    headImg = models.FileField(upload_to= './upload/')

    def __unicode__(self):
        return self.username
class FileAdmin(admin.ModelAdmin):
    list_display = ('username','headImg')

class Aboutus(models.Model):
    abId = models.CharField(max_length=50)
    abTitle = models.CharField(max_length=200)
    abImgUrl = models.FileField(upload_to='./account/template/attach-files/images/aboutus')
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('abId', 'abTitle', 'abImgUrl')

admin.site.register(User,UserAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(houseDetail,houseAdmin)
admin.site.register(houseResponsible,responsibleAdmin)
admin.site.register(area,areaAdmin)
admin.site.register(price,priceAdmin)
admin.site.register(sqm,sqmAdmin)
admin.site.register(dataUser,dataUserAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Aboutus,AboutusAdmin)

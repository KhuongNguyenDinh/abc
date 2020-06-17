from django.db import models
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class SanPham(models.Model):
    id=models.AutoField(primary_key=True)
    ten_san_pham=models.CharField('Ten san pham', max_length=200, unique=True)
    hinh = models.ImageField('Hinh', upload_to='hinh_san_pham', blank=True)
    don_gia_ban = models.FloatField('Don gia')
    mo_ta_tom_tat = models.CharField('Tom tat', max_length=200)
    chi_tiet = models.TextField('Chi tiet')
    trang_thai = models.BooleanField('Trang thai',blank=True, default=True)
    def __str__(self):
        return self.ten_san_pham


class UserProfileInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = "profile_pics",blank = True)
    def __str__(self):
        return self.user.username
        
class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True','True'),
        ('False','False'),
    )
    product = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default = 1)
    ip = models.CharField(max_length=20, blank = True)
    status = models.CharField(max_length=10, choices=STATUS, default= 'New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']

from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Product(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productName = models.CharField(max_length=50,null=True,blank=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='../media/prod_images')


fields =['id','desc','price']


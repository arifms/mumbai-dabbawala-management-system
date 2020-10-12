from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=200)
    pincode=models.IntegerField()
   
class canteenItems(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    availability=models.BooleanField(default=False)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
class cart(models.Model):
    name=models.OneToOneField(canteenItems,on_delete="")
class orders(models.Model):
    product=models.ForeignKey(canteenItems,on_delete=models.SET_NULL,null="False")
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
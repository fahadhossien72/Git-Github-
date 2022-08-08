from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_pic=models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
	    return self.name
    
    @property
    def imgURL(self):
        try:
            img = self.profile_pic.url
        except:
            img = ''
        return img

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
	    return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
	    return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
		('Out for delivery','Out for delivery'),
		('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.product.name

        

    

    
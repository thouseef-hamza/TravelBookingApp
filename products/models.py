from django.db import models

# Create your models here.

class Product(models.Model):
    class ProductType(models.TextChoices):
        HALF_DAY="halfday","Half Day"
        FULL_DAY= "full_day","Full Day"
    product_name=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    description = models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    liked=models.IntegerField(null=True)

class Facility(models.Model):
    name=models.CharField(max_length=50)

class Room(models.Model):
    name=models.CharField(max_length=50)

class ProductDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_detail")
    description=models.TextField(null=True)
    facilities=models.ManyToManyField(Facility,null=True)
    rooms=models.ManyToManyField(Room,null=True)

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_reviews")
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=70,null=True)
    email=models.EmailField()
    review=models.TextField(null=True)

class Booking(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_bookings")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70, null=True)
    email = models.EmailField(null=True)
    phone_number=models.CharField(max_length=20)

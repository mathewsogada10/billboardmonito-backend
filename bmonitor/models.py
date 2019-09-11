from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=40)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name


class MediaAgency(models.Model):
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.client.name + " - "+self.name


class BrandAgency(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    agency = models.ForeignKey(MediaAgency, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    contract = models.CharField(default='ACTIVE', max_length=10)

    def __str__(self):
        return self.agency.name+" - "+self.brand.client.name+" - "+self.brand.name


class BillBoard(models.Model):
    description = models.CharField(max_length=100)
    boardType = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    #imagePath = models.CharField(max_length=50)
    latittude = models.DecimalField(
        max_digits=30, decimal_places=20, blank=True)
    longitude = models.DecimalField(
        max_digits=30, decimal_places=20, blank=True)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    state = models.CharField(max_length=20)
    street = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class BillBoardBrand(models.Model):
    brandAgency = models.ForeignKey(BrandAgency, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)
    billboard = models.ForeignKey(BillBoard, on_delete=models.CASCADE)
    recommendation = models.CharField(max_length=100)

    def __str__(self):
        return str(self.billboard) + " " + str(self.brandAgency)


class Image(models.Model):
    description = models.CharField(max_length=30)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    fileContent = models.FileField(upload_to='Files')
    board = models.ForeignKey(BillBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Competitor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    distance = models.IntegerField()
    avInShops = models.CharField(max_length=50)
    boardBrand = models.ForeignKey(
        BillBoardBrand, on_delete=models.CASCADE, blank=True)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.description


class Users(models.Model):
    #auth_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    agency = models.ForeignKey(
        MediaAgency, on_delete=models.CASCADE, null=True)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)
    lastUpdate = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.client.name


class BoardSupplier(models.Model):
    name = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

from django.db import models

class Location(models.Model):
    LocationName = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.LocationName
    

class Item(models.Model):
    itemName = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName
    
    
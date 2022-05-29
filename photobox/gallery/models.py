from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)  

    def __str__(self): 
        return self.title 


class Image(models.Model):
    caption=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    date_created=models.DateTimeField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self): 
        return self.caption



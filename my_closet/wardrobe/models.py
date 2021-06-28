
from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class OutfitTag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption 

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="images", null=True)
    tag = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    outfit_tag = models.ManyToManyField(OutfitTag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="outfits")
    clothing = models.ForeignKey(Clothing, null=True, on_delete=models.CASCADE, related_name="outfits")

    def __str__(self):
        return self.name
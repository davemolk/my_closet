
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

class Top(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    tag = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name()

class Bottom(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    tags = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name()


class Dress(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    tags = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name()

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    tags = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name()

class Outerwear(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    tags = models.ManyToManyField(Tag)
    sell = models.BooleanField(default=False)

    def __str__(self):
        return self.name()

class Outfit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    outfit_tag = models.ManyToManyField(OutfitTag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="outfits")

    def __str__(self):
        return self.name()

